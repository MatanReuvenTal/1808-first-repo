FROM python:3.9
RUN apt update && apt  install -y curl
WORKDIR /apps
COPY requirements.txt .
RUN pip install -r requirements.txt --quiet
COPY main.py .
CMD ["python", "main.py"]
