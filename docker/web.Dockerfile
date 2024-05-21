FROM python:3.11

WORKDIR /app

COPY . .

RUN  pip install pipenv  \
    && pipenv requirements > requirements.txt \
    && pip install -r requirements.txt


EXPOSE 8000

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]