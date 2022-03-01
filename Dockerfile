FROM ubuntu:20.04

LABEL maintainer="Josh Teng <joshteng@me.com>"

RUN apt-get update -y && apt-get install -y python3-pip python3-dev wget

RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz

RUN tar -xvzf ta-lib-0.4.0-src.tar.gz && cd ta-lib && ./configure --prefix=/usr && make && make install

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# CMD ["python3", "start.py"]

# docker build -t joshteng/m1test .
# docker push joshteng/m1test
