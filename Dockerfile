# So i thik what I want to do here is to pull in the base gdal image
# build out gdal and its dependencies.  The do a second stage where
# i add python anddependencies

FROM python:3.9-slim

LABEL maintainer="elmorem@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./dev_requirements.txt /tmp/dev_requirements
COPY ./fowldata/ /fowldata
WORKDIR /fowldata
EXPOSE 8000

RUN apt-get update -y && \
    apt-get install -y \
    binutils \
    gdal-bin \
    libproj-dev \
    git && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    pip install --upgrade pip && \
    apt-get install -y postgresql-client && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r dev_requirements.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user