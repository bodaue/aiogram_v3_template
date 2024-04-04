from pydantic import SecretStr, BaseModel
from pydantic_settings import BaseSettings as _BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env.dist", env_file_encoding="utf-8")


class CommonConfig(BaseSettings, env_prefix='COMMON_'):
    bot_token: SecretStr
    admins: list[int]


class DbConfig(BaseSettings, env_prefix='DB_'):
    driver: str
    username: str
    password: SecretStr
    host: str
    port: int

    name: str
    echo: bool = False

    def build_dsn(self) -> str:
        return URL.create(drivername=self.driver,
                          username=self.username,
                          password=self.password.get_secret_value(),
                          host=self.host,
                          port=self.port,
                          database=self.name).render_as_string(hide_password=False)


class Config(BaseModel):
    common: CommonConfig
    db: DbConfig


def create_app_config() -> Config:
    return Config(
        common=CommonConfig(),
        db=DbConfig()
    )


config = create_app_config()
