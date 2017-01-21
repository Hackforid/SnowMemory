# coding=utf-8

import asyncio
import aiosmtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "zhouquan@xueqiu.com"
mail_user = "zhouquan@xueqiu.com"
mail_password = "jkbbj921"
loop = asyncio.get_event_loop()

async def connect():
    smtp = aiosmtplib.SMTP(hostname="smtp.exmail.qq.com", port=587, loop=loop)
    await smtp.connect()
    await smtp.starttls()
    await smtp.login(mail_user, mail_password)
    return smtp

#smtp = loop.run_until_complete(connect())


async def send_register_code(recipient, code):
    message = MIMEText(code, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'SnowMemory邮箱验证'
    await send_email(recipient, message.as_string())

async def send_email(recipient, message):
    smtp = await connect()
    await smtp.sendmail(sender, [recipient], message)
