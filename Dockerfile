FROM postgres:12

RUN apt-get update && apt-get install -y \
    postgresql-plpython3-12 \
    python3-pip \
    pgxnclient && \
    pip3 install Faker && \
    pgxn install postgresql_faker
