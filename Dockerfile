FROM python:3.12-slim
ENV PATH "/app:${PATH}"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . .

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]