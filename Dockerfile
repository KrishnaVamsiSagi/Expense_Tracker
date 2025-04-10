FROM python:3.12-slim

WORKDIR /app

COPY data.json .
COPY app.py .
COPY requirements.txt .


COPY templates/ ./templates/
COPY static/ ./static/


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
