FROM tensorflow/tensorflow

# install dependancies
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Copy html templates into container
COPY templates/ templates/
# Copy python application into container
COPY main.py /main.py

RUN mkdir /static

# expose Application on port 8080 to be able to access the webapp
EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ]