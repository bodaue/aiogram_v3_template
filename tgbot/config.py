from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings as _BaseSettings
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8",
    )


class CommonConfig(BaseSettings, env_prefix="COMMON_"):
    bot_token: SecretStr
    admins: list[int]


class PostgresConfig(BaseSettings, env_prefix="POSTGRES_"):
    host: str
    port: int
    user: str
    password: SecretStr
    db: str

    enable_logging: bool = False

    def build_dsn(self) -> str:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.db,
        ).render_as_string(hide_password=False)


class RedisConfig(BaseSettings, env_prefix="REDIS_"):
    use_redis: bool = False

    host: str
    port: int
    password: str


class Config(BaseModel):
    common: CommonConfig
    redis: RedisConfig
    postgres: PostgresConfig


def create_config() -> Config:
    return Config(common=CommonConfig(), redis=RedisConfig(), postgres=PostgresConfig())
