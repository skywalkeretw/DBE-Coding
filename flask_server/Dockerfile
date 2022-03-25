FROM python:3.8

COPY requirements.txt ./requirements.txt
COPY main.py ./main.py

RUN pip install -r requirements.txt
RUN mkdir /upload
EXPOSE 8080

CMD ["python", "./main.py"]
