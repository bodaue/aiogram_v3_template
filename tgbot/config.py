from pydantic import SecretStr, BaseModel
from pydantic_settings import BaseSettings as _BaseSettings, SettingsConfigDict


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env.dist", env_file_encoding="utf-8")


class CommonConfig(BaseSettings, env_prefix='COMMON_'):
    bot_token: SecretStr
    admins: list[int]


class Config(BaseModel):
    common: CommonConfig


def create_app_config() -> Config:
    return Config(
        common=CommonConfig(),
    )


config = create_app_config()
