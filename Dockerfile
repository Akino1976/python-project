ARG PYTHON_VERSION=3.9.5
FROM python:${PYTHON_VERSION}-slim-buster as python-base
ENV PYTHONPATH=$PYTHONPATH:/usr/local
WORKDIR /usr/src/app/
COPY . /usr/src/app/

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  PATH="$PATH:/runtime/bin" \
  PYTHONPATH="$PYTHONPATH:/runtime/lib/python3.9/site-packages" \
  POETRY_VERSION=1.1.8

FROM python-base as builder-base
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    unzip \
    python-dev \
    && apt-get clean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry export --without-hashes --no-interaction --no-ansi -f requirements.txt -o requirements.txt
RUN pip install --prefix=/runtime --force-reinstall -r requirements.txt

FROM python-base as production
COPY --from=builder-base /runtime /usr/local

ENTRYPOINT [ "python" ]
CMD [ "run_jobs.py" ]
