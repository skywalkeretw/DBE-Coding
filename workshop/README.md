# Workshop

## Requirements

- Git [install guide](git/README.md) (windows users should have git bash)
- Docker [install guide](docker/README.md)

## Git

1. Setting up access to GitHub using `ssh` instead of `user/password`

1. Clone this repository
    ```bash
    git clone git@github.com:skywalkeretw/DBE-Coding.git
    ```

1. Checkout a branche and add your user name to the `contributors.md`
    
    Checkout:
    ```bash
    git checkout -b <Your branch name>
    ```

    Edit file: `contributors.md`

    Add the file to your commit:
    ```bash
    git add contributors.md
    ```

    commit your change:
    ```bash
    git commit -m "Added <your name> as contributor"
    ```

    push your changes to github:
    ```bash
    git push origin <your branch name>
    ```

    Open a pull request on the github website with your change

    Go to `master` branch
    ```bash
    git checkout master
    ```

    Pull the changes from `master`
    ```bash
    git pull origin master
    ```

## Docker 

1. Run the hello world Docker image
    ```bash
    docker run hello-world:latest
    ```
2. Build the docker container from inside the docker folder and run it
    
    Build
    ```bash
    docker build -t hello .
    ```

    Run
    ```bash
    docker run hello
    ```

## Linux

1. Run the linux test env Container you can build it yourself or just run it from docker hub

    ```bash
    docker run -it lukeroy/dbe-learn-linux:latest
    ```