ARG PYTHON_VERSION=3.9.5
FROM python:${PYTHON_VERSION}-slim-buster
ARG POETRY_VERSION=1.1.8
ENV PYTHONPATH=$PYTHONPATH:/usr/src/app/tests/shared/:/usr/src/app/tests/system/:/usr/src/app/
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==${POETRY_VERSION}"
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" \
    VIRTUAL_ENV="/opt/venv"

COPY pyproject.toml poetry.lock /usr/src/app/tests/unit/
WORKDIR /usr/src/app/tests/unit

RUN poetry install

ENTRYPOINT ["py.test", "-c", "pytest.cfg"]
