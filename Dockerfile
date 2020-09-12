FROM alpine:latest
RUN apk -U upgrade; \
apk add python3; \
apk add py3-pip; \
apk add curl; \
apk add vim; \
pip install sleeper-api-wrapper; \
ln -s /usr/bin/python3 /usr/bin/python 

COPY . /usr/src/ff_optmzr
WORKDIR /usr/src/ff_optmzr
