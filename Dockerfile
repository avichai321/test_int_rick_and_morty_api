FROM python:3
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
ENV app=python
ENTRYPOINT [ "python" , "rick_and_morty_rest_api.py" ]