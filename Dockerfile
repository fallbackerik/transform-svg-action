FROM debian:latest
RUN apt update && apt install python-is-python3
COPY *.py ./
ENTRYPOINT [ "python", "./entrypoint.py"]
