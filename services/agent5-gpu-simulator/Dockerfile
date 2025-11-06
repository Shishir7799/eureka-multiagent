FROM nvidia/cuda:12.0-runtime-ubuntu22.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY main.py .
ENV PORT=8080
EXPOSE 8080
CMD ["python", "main.py"]

