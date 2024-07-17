FROM python:3.12-slim as base
ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PATH "/app:${PATH}"
WORKDIR /app

# Create requirements.txt file
FROM base as poetry
RUN pip install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry export -o /requirements.txt --without-hashes

# Install requirements
FROM base as common
COPY --from=poetry /requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]