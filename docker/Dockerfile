#baesimage for your container check hub.docker.com for more base images and tags
FROM ubuntu:latest

# Update installed Packages
RUN apt update && \
    apt upgrade -y

#copy programm into container
COPY app.sh app.sh

ENTRYPOINT [ "./app.sh" ]