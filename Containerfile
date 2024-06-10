FROM debian:latest
COPY *.py ./
CMD [ "python", "./entrypoint.py"]
