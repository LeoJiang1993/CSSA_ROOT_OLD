from email.header import Header
import smtplib
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives


class EmailAccount:
    def __init__(self, account_name, address, password):
        self.account_name = account_name
        self.address = address
        self.password = password


def send_email(email_account, destination, message, subject):
    # todo alternative的发件地址
    msg = EmailMultiAlternatives(
        to=[destination],
        subject=subject,
        body=message
    )
    msg.attach_alternative(message, "text/html")
    msg.send()
    # # Email Server
    # smtp_server = '203.205.128.15'
    # ssl_port = '465'
    # # Generate Email
    # msg = MIMEText(message, 'plain', 'utf-8')
    # msg['From'] = email_account.account_name + ' <' + email_account.address + '>'
    # msg['To'] = destination
    # msg['Subject'] = Header(subject, 'utf-8').encode()
    # # Send Email
    # server = smtplib.SMTP_SSL_PORT(smtp_server, ssl_port)
    # server.set_debuglevel(1)
    # server.login(email_account.address, email_account.password)
    # server.sendmail(email_account.address, [destination], msg.as_string())
    # server.quit()

