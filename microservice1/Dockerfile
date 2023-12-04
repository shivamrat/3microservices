# Dockerfile for Microservice1

FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY microservice_1.py /app

CMD ["python", "microservice_1.py"]

