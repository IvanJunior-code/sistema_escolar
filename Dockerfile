FROM alpine:3.18.3
WORKDIR /app
COPY sistema_escolar.py .
RUN apk add python3
ENTRYPOINT python3 sistema_escolar.py