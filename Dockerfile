FROM python:2.7.15-alpine3.8

COPY ./app /app
RUN pip install -r /app/requirements.txt

EXPOSE 5000

USER nobody
CMD /usr/local/bin/python /app/balance.py
