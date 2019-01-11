import json
from email.mime.text import MIMEText
import os
import smtplib
import time


instance_info_path = os.environ.get('INSTANCE_INFO_PATH', '/config/instance-info.json')
initial_delay = int(os.environ.get('INITIAL_DELAY', 86400))  # 1 day by default
notify_interval = int(os.environ.get('NOTIFY_INTERVAL', 604800))  # 1 week by default

smtp_server_credentials = {
    'server': os.environ.get('SMTP_SERVER'),
    'port': os.environ.get('SMTP_PORT', 465),
    'login': os.environ.get('SMTP_LOGIN'),
    'password': os.environ.get('SMTP_PASSWORD'),
    'sender': os.environ.get('SMTP_FROM')
}


def send_email(recipient, email_body):
    s = smtplib.SMTP_SSL(smtp_server_credentials['server'], smtp_server_credentials['port'])
    s.ehlo()
    s.login(smtp_server_credentials['login'], smtp_server_credentials['password'])
    s.set_debuglevel(1)

    msg = MIMEText(email_body)
    msg['Subject'] = "Check your instances"
    msg['From'] = smtp_server_credentials['sender']
    msg['To'] = recipient

    print "Sending..."
    print msg

    s.sendmail(smtp_server_credentials['sender'], recipient, msg.as_string())

    print "Message has been sent"


with open(instance_info_path) as f:
    instance = json.load(f)

instances = instance['InstanceIds']
instances.pop()

time.sleep(initial_delay)
region = instance['Region']
recipient = instance['Email']
email_body = "You have running instances in " + region + " region.\n"\
             "Instances: " + ', '.join(instances) + ".\n" \
             "Please check if they are still in use. Thank you.\n"

while True:
    send_email(recipient, email_body)
    time.sleep(notify_interval)
