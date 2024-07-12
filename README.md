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

1. Clone the repository:
   ```sh
   git clone https://github.com/bodaue/aiogram_v3_template.git
2. Install the dependencies:
   ```sh
   poetry install
3. Set up your environment variables (.env)

    - Rename .env.example to .env
    - Configure it

4. Run database migrations
    ```sh
   poetry run alembic upgrade head

5. Run the bot:
   ```sh
   poetry run python -m tgbot
   