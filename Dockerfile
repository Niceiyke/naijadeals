FROM python:3.10-slim

WORKDIR /djangoapp

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./priceFinder/ /djangoapp/
