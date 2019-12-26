FROM python:3.6-alpine
RUN apk add --no-cache python3-dev libstdc++ && \
    apk add --no-cache g++ && \
    apk add --no-cache ffmpeg && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip3 install numpy && \
    pip3 install pandas 

COPY bots/config.py /bots/
COPY bots/download.py /bots/
COPY bots/twitter_dl.py /bots/
COPY bots/img /bots/img/
COPY bots/output /bots/output/
COPY bots/pytube /bots/pytube/
COPY bots/Mention.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "Mention.py"]
