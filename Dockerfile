FROM python:3
SHELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR .
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip3 install -r /requirements.txt
COPY . .