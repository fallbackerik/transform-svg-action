FROM python:latest
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "python", "./entrypoint.py"]
