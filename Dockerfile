FROM python:3.10

WORKDIR /app

RUN pip install --upgrade pip 

COPY . /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["sh","/app/entrypoint.sh"]