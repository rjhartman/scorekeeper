FROM python:3.11-bookworm as deps

WORKDIR /api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM deps as appplication

ENV FLASK_APP app
ENV FLASK_RUN_HOST 0.0.0.0

COPY . .
CMD ["flask", "run"]
