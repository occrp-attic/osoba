FROM python:2.7.9
MAINTAINER Smári McCarthy <smari@occrp.org>

# you will need need these docker images too:
# - postgres (expected to be called postgres_osoba
# consult README.md for more information

RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y \
    postgresql-client libpq-dev \
    gcc \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

#RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y autoremove
    
RUN mkdir -p /usr/src/osoba
WORKDIR /usr/src/osoba

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/osoba/
RUN pip install -r requirements.txt

COPY . /usr/src/osoba/
RUN mkdir -p /var/log/osoba/

EXPOSE 5000
CMD ["python", "app.py"]
