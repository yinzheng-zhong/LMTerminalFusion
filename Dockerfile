FROM ubuntu:latest

ENV PYTHONUNBUFFERED=1

# install python
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir openai colorama requests python-dotenv
