FROM python:3.8-slim

RUN mkdir '/app_server'

WORKDIR '/app_server'

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
