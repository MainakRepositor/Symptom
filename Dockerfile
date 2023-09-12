# app/Dockerfile

FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy all files to the docker app
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit","run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
