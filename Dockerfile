FROM python:3.8

COPY requirements.txt /

RUN pip install -r requirements.txt

# Set the default directory where CMD will execute
WORKDIR /app

CMD bash
