FROM  python:3.7.6-slim-stretch
COPY ./requirements.txt ./app/requirements.txt
WORKDIR /app
RUN apt update && apt install -y libmariadbclient-dev gcc
RUN pip install -r requirements.txt
RUN pip install gunicorn 
COPY . /app
RUN chmod u+x ./docker-entry.sh
ENTRYPOINT ["sh","/app/docker-entry.sh"]