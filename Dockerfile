FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install --upgrade pip
RUN pip install -e .

ENTRYPOINT ["project-scaffolder"]