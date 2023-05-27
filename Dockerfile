FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
EXPOSE 8000
RUN pip install -r requirements.txt
CMD pytest test_main.py && uvicorn main:app --host 0.0.0.0 --port 8000
