# Docker 

## Installation
### Mac
Docker for Mac can be installed over the [website](https://www.docker.com/products/docker-desktop/) or using homebrew
```bash
brew install docker
```
### Windows
Insall Docker Desktop [website](https://www.docker.com/products/docker-desktop/)
### Linux
Use the install script from docker make sure curl is installed
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