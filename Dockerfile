FROM debian:latest
RUN apt update
RUN apt install python-is-python3
COPY *.py ./
ENTRYPOINT [ "python", "./entrypoint.py"]
