# app/Dockerfile

FROM python:3.9-slim
LABEL authors="AryaroopMajumder"

RUN python3 -m pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel

COPY . /var/www

WORKDIR /var/www
RUN pip3 install -r ./requirements.txt

EXPOSE 8007

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8007", "--server.address=0.0.0.0"]