from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str
    port: int = 27017


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_mongo_storage: bool


@dataclass
class Miscellaneous:
    pass


@dataclass
class Config:
    tg_bot: TgBot
    misc: Miscellaneous = None
    db: DbConfig = None


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=env.list('ADMINS', subcast=int),
            use_mongo_storage=env.bool("USE_MONGO_STORAGE")
        ))
