FROM debian:latest
COPY *.py ./
ENTRYPOINT [ "python", "./entrypoint.py"]
