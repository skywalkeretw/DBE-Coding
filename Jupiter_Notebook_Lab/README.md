# Jupiter Notebook Lab

Guide to setup simple Python Jupiter Notebook Lab

## Requirements:
- [Docker](https://docs.docker.com/get-docker/)
- Windows Users: Run Docker in PowerShell if you want to follow the Guide

## Setup for Windows, Mac and Linux
1. Open a terminal and navigate to your project directory (space where you want to store your notebooks)  
    **Linux/MacOS (Should Work in Windows PowerShell)**
    ```bash
        cd your/Work/dir
    ```

1. Run Jupiter Notebook inside a Docker Container mounting the current directory you are in and exposing the Port `10000` 
    ** **
    ```bash
        docker run -it --rm -p 10000:8888 -v ${PWD}:/home/jovyan/work jupyter/datascience-notebook:b418b67c225b
    ```

1. Open your Browser at http://localhost:10000 to use Jupiter Notebook. The Tokken for login is displayed inside the Termianl. Congratulations you now have a running Jupiter Notebook lab.

## FAQ

**Q: How Do I install Pip Modules?**  
*A: If you need to install any missing python modules run the following command inside the Notebook:*
```bash
    !pip install <module>
```

**Q: Where Are my Notebooks Stored?**  
*A: All your Notebook will be stored in the Directory you started the Docker Container at.*

**Q: Can I use git bash on Windows instead of PowerShell?**  
*A: Yes if you prefix `winpty` to your docker command*
```bash
    winpty docker run -it --rm 10000:8888 ...
```

