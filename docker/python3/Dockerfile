FROM python:3

WORKDIR /usr/src/app

COPY Dockerfile mycerts.crt* /usr/local/share/ca-certificates/
RUN rm /usr/local/share/ca-certificates/Dockerfile \
    && update-ca-certificates

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


# CMD [ "python", "./your-daemon-or-script.py" ]

# https://hub.docker.com/_/python/

# Install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y   libnss3-tools \
                            fonts-liberation \
                            libappindicator3-1 \
                            libasound2 \
                            libatk-bridge2.0-0 \
                            libatspi2.0-0 \
                            libgtk-3-0 \
                            libnspr4 \
                            libnss3 \
                            libx11-xcb1 \
                            libxtst6 \
                            lsb-release \
                            xdg-utils \
                            fonts-migmix



WORKDIR /tmp
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb
RUN touch /usr/local/share/ca-certificates/mycerts.crt \
    && csplit -f cert- /usr/local/share/ca-certificates/mycerts.crt '/-----BEGIN CERTIFICATE-----/' '{*}' \
    && rm /tmp/cert-00  \
    && mkdir -p $HOME/.pki/nssdb && certutil -d $HOME/.pki/nssdb -N  \
    && for file in $(find . -name 'cert-*' -printf '%f\n'); do certutil -d $HOME/.pki/nssdb -A -t "C,C,C" -n "$file" -i $file ;done

# install chromedriver
# RUN wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip \
RUN site=https://chromedriver.storage.googleapis.com \
    && wget $site/$(wget -q -O - $site/LATEST_RELEASE_$(google-chrome-stable --product-version | cut -d "." -f 1))/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/

WORKDIR /usr/src/app
ENV DISPLAY host.docker.internal:0.0
RUN echo 'alias python3d="python3 -m ptvsd --host 0.0.0.0 --port 3210 --wait "' >> ~/.bashrc

