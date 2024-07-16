FROM python:3.12-slim as base
ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PATH "/app/scripts:${PATH}"
WORKDIR /app

# Create requirements.txt file
FROM base as poetry
RUN pip install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry export -o /requirements.txt --without-hashes

FROM base as common
COPY --from=poetry /requirements.txt .
# Create venv, add it to path and install requirements
RUN python -m venv /venv
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "-m", "tgbot"]