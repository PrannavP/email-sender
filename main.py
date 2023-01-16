import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from credentials import my_email, my_password_key, receiver_email

email = my_email
password = my_password_key
send_to_email = receiver_email
subject = 'Testing'
message = 'This is me testing stuffs hehe'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()