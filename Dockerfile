FROM python:3.7.3-alpine3.9 AS base

RUN pip install -U pip

# Build Stage
FROM base AS build

RUN apk update && apk add --no-cache --upgrade \
    build-base \
    gcc

WORKDIR /wheels
COPY requirements.txt .

RUN pip wheel -r requirements.txt

# Execution Stage
FROM base

ENV PYTHONUNBUFFERED=1

COPY --from=build /wheels /wheels

RUN pip install -r /wheels/requirements.txt -f /wheels && \
    rm -rf /wheels && \
    rm -rf /root/.cache/pip/*

WORKDIR /app

COPY sqlalchemy_customtypes_test sqlalchemy_customtypes_test

ENTRYPOINT ["python"]
CMD ["-m", "sqlalchemy_customtypes_test"]
