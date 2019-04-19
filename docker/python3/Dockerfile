FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DISPLAY host.docker.internal:0.0

# CMD [ "python", "./your-daemon-or-script.py" ]

# https://hub.docker.com/_/python/