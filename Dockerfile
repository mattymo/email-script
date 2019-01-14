FROM python:2.7

COPY . /email-script
WORKDIR /email-script
RUN pip install /email-script

CMD [ "python", "/email-script/emailscript/send_email.py" ]