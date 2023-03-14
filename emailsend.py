import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

with open('customerinfo.txt', 'r') as f:
    customerinfo = f.readlines()  # read contents of the file as a list of strings

# Set up the email
msg = MIMEMultipart()
msg['From'] = 'enter email'
msg['To'] = ", ".join(customerinfo)  # join the list of strings with commas to create a single string
msg['Subject'] = 'test'

# Add text to the email
body = 'Embedded links and photo attachment test,try to visit the link'
msg.attach(MIMEText(body, 'plain'))

# Add an image to the email
with open('sms.png', 'rb') as f:
    img_data = f.read()
img = MIMEImage(img_data, name='sms.png')
msg.attach(img)

# Add a link to the email
html = '<html><body><p>Click <a href="https://aeropost.com/site/en/courier?gtw=GEO&lang=en">here</a> to visit our website.</p></body></html>'
part = MIMEText(html, 'html')
msg.attach(part)

# Connect to Gmail's SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'enter email here'
smtp_password = 'enter app password'
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Send the email
text = msg.as_string()
server.sendmail(msg['From'], customerinfo, text)
server.quit()
