# -*- coding=utf-8 -*-
import sys

import asyncio
import aiosmtplib
from email.mime.text import MIMEText
from email.header import Header
from kit.config import config

mail_config = config['mail']
sender = mail_config['address']
mail_user = mail_config['address']
mail_password = mail_config['password']
loop = asyncio.get_event_loop()

async def connect():
    smtp = aiosmtplib.SMTP(hostname=mail_config['smtp'], port=mail_config.get('port', 587), loop=loop)
    await smtp.connect()
    await smtp.starttls()
    await smtp.login(mail_user, mail_password)
    return smtp

async def send_register_code(recipient, code):
    message = MIMEText(code, 'plain', _charset='utf-8')
    message['From'] = Header(sender, 'utf-8')
    message['To'] = Header(recipient, 'utf-8')
    message['Subject'] = Header('SnowMemory邮箱验证', 'utf-8')
    await send_email(recipient, message.as_string().encode('utf-8'))

async def send_email(recipient, message):
    print(message)
    print(sys.getdefaultencoding())
    smtp = await connect()
    await smtp.sendmail(sender, [recipient], message)
