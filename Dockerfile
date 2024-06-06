FROM python:3.9.2-slim-buster
LABEL maintainer="elmorem@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./dev_requirements.txt /tmp/dev_requirements
COPY ./fowldata/ /fowldata
WORKDIR /fowldata
EXPOSE 8001

ARG DEV=false

RUN apt-get update \
    && apt-get -y install software-properties-common netcat gcc postgresql \
    && apt-get clean 

RUN apt-get update \
    && apt-get -y install binutils libgdal-dev libproj-dev proj-bin gdal-bin \
    python-gdal python3-gdal gdal==3.9.0 make cmake wget clang

# build and install geos

RUN wget https://download.osgeo.org/geos/geos-3.9.5.tar.bz2 \
    && tar xjf geos-3.9.5.tar.bz2 \ 
    && cd geos-3.9.5 \
    && mkdir build \
    && cd build \
    && cmake \
        -DCMAKE_BUILD_TYPE=Release .. \
        -DCMAKE_INSTALL_PREFIX=/usr/local \
    && make \
    && ctest \
    && make install
    
# build and install proj
# this one we aren't going to build from source proj-bin should cover it



RUN pip install --upgrade pip

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
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
