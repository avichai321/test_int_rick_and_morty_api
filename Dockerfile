FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENV app=python
CMD [ "python" , "rick_and_morty_rest_api.py" ]