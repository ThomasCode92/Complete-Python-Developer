import os
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

html = Path('index.html').read_text()
htmlTemplate = Template(html)

email = EmailMessage()
email['from'] = 'ThomasCode92'
email['to'] = os.environ['EMAIL_SENDER']
email['subject'] = 'Hi Developer'

email.set_content(htmlTemplate.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PASSWORD'])
    smtp.send_message(email)
    print('all good boss!')
