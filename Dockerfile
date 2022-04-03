FROM falprojects/fal-userbot:buster
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Fal-Userbot https://github.com/falprojects/Fal-Userbot /home/Fal-Userbot/ \
    && chmod 777 /home/Fal-Userbot \
    && mkdir /home/Fal-Userbot/bin/
WORKDIR /home/Fal-Userbot/
COPY ./sample_config.env ./config.env* /home/Fal-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
