# Aiogram Bot Template (v3)

#### A scalable template for building Telegram bots using aiogram 3.x and sqlalchemy 2.x

## Features

- Built with [aiogram](https://github.com/aiogram/aiogram)
- Database management with [SQLAlchemy](https://www.sqlalchemy.org/)
  and [asyncpg](https://github.com/MagicStack/asyncpg)
- Database migrations with [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- Data storage for FSM with [redis-py](https://github.com/redis/redis-py)

## System dependencies

- Python 3.12+
- Poetry

## Installation

### Via [Docker](https://www.docker.com/)
- Set up environment variables (.env)
    - Rename .env.example to .env
    - Configure it
- Run docker-compose
  ```sh
  docker-compose up -d

### Via systemd
- Set up environment variables (.env)
    - Rename .env.example to .env
    - Configure it
- Install the dependencies:
   ```sh
   poetry install

- Run database migrations
    ```sh
   poetry run alembic upgrade head

- Run the bot:
   ```sh
   poetry run python -m tgbot
