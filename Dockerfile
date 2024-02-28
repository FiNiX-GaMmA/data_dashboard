# app/Dockerfile

FROM python:3.9-slim
LABEL authors="AryaroopMajumder"

RUN python3 -m pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel

COPY . /var/www

WORKDIR /var/www

RUN ls -l  # to see the file contents

RUN pip3 install -r ./requirements.txt

EXPOSE 8007

HEALTHCHECK CMD curl --fail http://localhost:8007/_stcore/health


ENTRYPOINT ["streamlit", "run", "streamlit.py", "--server.port=8007", "--server.address=0.0.0.0"]