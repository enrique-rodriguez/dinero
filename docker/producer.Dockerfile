FROM python:3.11

WORKDIR /app

COPY . .

RUN  pip install pipenv  \
    && pipenv requirements > requirements.txt \
    && pip install -r requirements.txt

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

CMD ["python", "producer.py"]