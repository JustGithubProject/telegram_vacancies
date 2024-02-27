FROM python:3.10-alpine

WORKDIR /app

RUN apk update && \
    apk add --no-cache postgresql-dev gcc musl-dev

COPY . .
RUN pip install -r requirements.txt

CMD ["alembic", "upgrade", "f2fddb7aa289"]
CMD ["alembic", "upgrade", "e8cf06ef45f8"]
CMD ["alembic", "upgrade", "1092f3b009ef"]
CMD ["cd", "bot"]
CMD ["python", "bot/main.py"]