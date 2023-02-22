FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./src /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=80"]