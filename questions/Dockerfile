FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5002

COPY . /app

RUN pip install -r ./requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5002"]
