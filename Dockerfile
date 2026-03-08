FROM docker.io/google/cloud-sdk:emulators

RUN apt-get update && apt-get install -y python3-pip netcat-openbsd
RUN pip3 install flask google-cloud-spanner --break-system-packages

WORKDIR /app
COPY . .
EXPOSE 8080

CMD ["./entrypoint.sh"]
