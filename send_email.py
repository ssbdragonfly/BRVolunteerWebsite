import json
import smtplib
from email.mime.text import MIMEText

with open('form_data.json', 'r') as file:
    data = json.load(file)

name = data['name']
email = data['email']
phone = data['phone']
message = data['message']

to = "bishtshaurya314@gmail.com"
subject = "New Volunteer Inquiry"
body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "filler"
smtp_password = "filler"
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = smtp_username
msg['To'] = to
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, to, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
