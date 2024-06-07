FROM ubuntu:24.04

# Now project files
COPY ./requirements.txt /tmp/requirements.txt
COPY ./dev_requirements.txt /tmp/dev_requirements
COPY ./fowldata/ /fowldata
WORKDIR /fowldata
EXPOSE 8001

# BAsic BUilding blocks
RUN apt-get update \
    && apt-get -y install wget \ 
        python3.12 \
        python3-pip \
        python3.12-venv \
        cmake \
        make \
    && apt-get clean 
# software-properties-common

# Now PROJ
RUN apt-get -y install proj-bin

# NOW geos
RUN apt-get -y install geos-bin \
        libgeos++-dev \
        libgeos-dev \
        libsfcgal-dev
        
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
# NOW GDAL
RUN apt-get -y install gdal-bin \
        gdal-data \
        gdal-plugins \
        libgdal-dev \
        libgdal-grass \
        python3-gdal

ARG DEV=false
#  postgis
RUN apt-get -y install postgresql postgis

# now requirements
RUN python3 -m venv /py && \
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


# geos-config --version  3.12.1
# gdal-info --version 3.8.4
# proj --version
# psql --version
# pkg-config --modversion proj
# access psql  exec into container psql -U devuser -d devdb 
