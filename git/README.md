# Git

## Installation
### Mac
git for Mac can be installed using homebrew
```bash
brew install git
```

### Windows
Insall Docker Desktop from the offical [website](https://git-scm.com/downloads)  
make sure to install git bash

### Linux (Ubuntu)
Use the package manager to install git
```bash
sudo apt update && sudo apt install git -y
```

---
## Usage
Git can be used over the CLI or over your Editor/IDE this guide will explain how to use the CLI

1. Create a new repository on the Github / Gitlab Website (Account is required) top right corner will be a `+` select `new repository` and follow the setup guide.
you now have a empty repositoy for your code.

1. Clone your  newly created repository or a other existing reposiory. Open a terminal window (Mac/linux) if you are using Windows install [GIT](https://git-scm.com/download/) make sure to select git bash (when the terminal is used windows users should use git bash if they want the same experience) the following code will clone this repository to clone a diffrent repository exchange the url with the repository url you want to clone
    ```bash
    git clone https://github.com/skywalkeretw/DBE-Coding.git
    ```

1. After the project navigate into the the project directory of the cloned project and start your coding
    ```bash
    cd <dir name>
    ```

---

Now that your project is setup you can start writing code and working with git

1. After you have added or changed your code you will need to add the changes you would like to comit.

    Use git status to see new, removed and changed files
    ```bash
    git status
    ```
    Select the files you want to commit:
    ```bash
    gtit add <file or dir name>
    ```
    You can also add everything:
    ```bash
    git add .
    ```
    if you added a file by mistake you can reset 
    ```bash
    git reset HEAD -- <file>
    ```

1. Now that you have your files you want to commit the next step is to commit them
    ```bash
    git commit -m "your message"
    ```
    if you dont youse the `-m`falg you will have to writte your commit message in the terminal editor of choice (default is vi/vim) 

1. Now that you have you commit you will need to push it to git
    ```bash
    git push origin <branch name>
    ````
    your default branch is `master` when working in teams it is better to create your own branches 

---

If you are working with branches it is important to know how to create and switch branches

- Create a new branch and switch to it
    ```bash
    git checkout -b <branch name>
    ```

- Change to an existing branch
    ```bash
    git checkout <branch name>
    ````

- Delete branch
    ```bash
    git branch -D <branch name>
    ````

---

To get updates from a branch run the pull command  
```bash
git pull origin <branch name>
```

usually you will be pulling from `master`