FROM debian:latest
RUN apt update
RUN apt install python-is-python3 -y
COPY *.py /
ENTRYPOINT [ "python", "/entrypoint.py"]
