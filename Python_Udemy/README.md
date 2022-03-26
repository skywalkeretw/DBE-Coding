# jupiter notebook
Jupiter notebooks can be run in Docker for a simplefied user experience

```bash
docker run -it --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work jupyter/datascience-notebook:b418b67c225b
```
can also be run in detatched mode 

Install packages in jupiter notebook inside cell

```bash
!pip install <module>
```