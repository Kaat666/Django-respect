FROM python:3
SHELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR ./Django-respect
COPY ./requirements.txt /Django-respect
RUN pip install -r /Django-respect/requirements.txt
COPY . /Django-respect/