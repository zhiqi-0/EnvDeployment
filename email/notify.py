import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

import argparse

parser = argparse.ArgumentParser(description='email')
parser.add_argument('--sender', type=str, help='sender email')
parser.add_argument('--code', type=str, help='sender password')
parser.add_argument('--recver', type=str, help='recver email')
parser.add_argument('--msg', type=str, default='an email notification', help='sending message')

args = parser.parse_args()



sender = args.sender
code   = args.code
recver = args.recver

ret = True
try:
    msg = MIMEText(args.msg, 'plain', 'utf-8')
    msg['From'] = formataddr(["Notifier", sender])
    msg['To'] = formataddr(["EndUser", recver])
    msg['Subject'] = "Notification"

    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(sender, code)
    server.sendmail(sender, [recver, ], msg.as_string())
    server.quit()
except Exception:
    ret = False

if ret:
    print('successfully send out emails')
else:
    print('fail to send out email')
