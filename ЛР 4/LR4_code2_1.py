"""Задание 1 комплект 2"""

import smtplib
from email.mime.text import MIMEText # используется для создания текстовых и многочастных сообщений
from email.mime.multipart import MIMEMultipart # используется для создания текстовых и многочастных сообщений

email = 'nomelnik3570@mail.ru'
password = '3NhdTqgWKwnZmtMUWpnQ'

mms = MIMEMultipart() # создание многочастного сообщения
mms['From'] = email
mms['To'] = 'melnik3570@gmail.com'
mms['Subject'] = 'Hehehe' # тема письма

word = 'Hi, how are you?\nI see you'

mms.attach(MIMEText(word, 'plain')) # прикрепление текста к сообщению

smtpob = smtplib.SMTP('smtp.mail.ru', 587)
smtpob.starttls()
smtpob.login(email, password)
smtpob.send_message(mms)
smtpob.quit()