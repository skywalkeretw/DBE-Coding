# Docker 

## Installation
### Mac
Docker for Mac can be installed over the [website](https://www.docker.com/products/docker-desktop/) or using homebrew
```bash
brew install docker
```

### Windows
Insall Docker Desktop from the offical [website](https://www.docker.com/products/docker-desktop/)  
I recommend using windows power shell when working with Docker

### Linux
Use the install script from docker make sure curl is installed open the Terminal and runn the following command.
```bash
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
```

Install curl if not installed (ubuntu)
```bash
sudo apt update && sudo apt install curl -y
```

## Usage
Docker can be used in its simples way to run and build containers

### Run container from Docker Hub
This example will run the hello world example  to check if docker is working
```bash
docker run hello-world:latest
```
the output should be something like this
```bash
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete
Digest: sha256:13e367d31ae85359f42d637adf6da428f76d75dc9afeb3c21faea0d976f5c651
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### Build your Docker container
This is the simplest way to build a Docker container locally 
```bash
docker build -t <your tag name> .
```

## Dockerfile
The Dockerfile is the blueprint used for building your container

```Dockerfile
FROM <baseimage>

RUN <commands to run inside container>

EXPOSE <port you want to expose>

ENTRYPOINT <The command/script/programm you want to run>
```

There is a example dockerfile you can build inside this directory

1. Build the docker container from the directory
    ```bash
    docker build -t hello:latest .
    ```

2. After your container has been built run it
    ```bash
    docker run hello:latest
    ```