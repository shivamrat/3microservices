# Dockerfile for Microservice3

FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY microservice_3.py /app

CMD ["python", "microservice_3.py"]

