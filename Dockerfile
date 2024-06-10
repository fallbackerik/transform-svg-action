FROM debian:latest
RUN sudo apt update && sudo apt install python-is-python3
COPY *.py ./
ENTRYPOINT [ "python", "./entrypoint.py"]
