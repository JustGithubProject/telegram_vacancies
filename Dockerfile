FROM python:3.10-alpine

WORKDIR /app

RUN apk update && \
    apk add --no-cache postgresql-dev gcc musl-dev

COPY . .
RUN pip install -r requirements.txt

CMD ["cd", "bot"]
CMD ["python", "bot/main.py"]