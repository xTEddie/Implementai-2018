FROM python:3.6

WORKDIR /app/server

COPY . /app/server/

RUN pip3 install -r /app/server/requirements/prod.txt

RUN python3 manage.py collectstatic --no-input

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
