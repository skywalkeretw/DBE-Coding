FROM ubuntu:22.04

RUN apt update \ 
    &&  apt upgrade -y \
    && apt install -y \
    vim \
    nano \
    ssh \
    htop


COPY info.txt info.txt

ENTRYPOINT ["/bin/bash"]