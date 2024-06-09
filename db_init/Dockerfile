FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app
COPY ../init_data /app
COPY ../init_data /app/db_init/init_data

RUN pip install -r ./requirements.txt

CMD ["python", "./initial_db.py"]
