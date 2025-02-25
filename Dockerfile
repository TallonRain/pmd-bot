FROM python:3.12-alpine
LABEL org.opencontainers.image.source=https://github.com/TallonRain/pmd-bot
WORKDIR /stuff
COPY requirements.txt /stuff/requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]
ADD . /stuff
ENTRYPOINT ["python3", "main.py"]