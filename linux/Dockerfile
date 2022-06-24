FROM ubuntu:22.04

RUN apt update \ 
    && apt upgrade -y \
    && apt install -y \
    vim \
    nano \
    ssh \
    htop

ENV PATH="$PATH:/usr/games/"

COPY info /usr/local/bin/info

COPY info.txt info.txt

ENTRYPOINT ["/bin/bash"]