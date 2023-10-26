FROM python:3.11.1-alpine

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . /usr/src/app/

COPY ./api_file_manager/entrypoint.sh /usr/src/app/entrypoint.sh

RUN chmod +x /usr/src/app/entrypoint.sh

CMD ["./entrypoint.sh"]
