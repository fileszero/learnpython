FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DISPLAY host.docker.internal:0.0

RUN echo 'alias python3d="python3 -m ptvsd --host 0.0.0.0 --port 3210 --wait "' >> ~/.bashrc

# CMD [ "python", "./your-daemon-or-script.py" ]

# https://hub.docker.com/_/python/