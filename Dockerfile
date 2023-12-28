FROM mcr.microsoft.com/devcontainers/python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /app/

COPY ./entrypoint.sh /
RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
EXPOSE 8000