FROM ubuntu:latest

COPY . /tmp/

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \    
    pip3 install vaderSentiment

#CMD ["python3", "/tmp/my_first_example.py"]