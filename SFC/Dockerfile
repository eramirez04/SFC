FROM python:3.14-slim 

WORKDIR /app

COPY requeriments.txt .

RUN pip install --no cache--dir -r requeriments.txt


COPY . . 

EXPOSE 8000


CMD [ "gunicorn" , "--bind", "0.0.0.0:8000", "SFC.wsgi:application"]