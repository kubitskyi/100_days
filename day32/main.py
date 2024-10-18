import os
from dotenv import load_dotenv
import smtplib
import ssl


load_dotenv()
mail_server = os.getenv('MAIL_SERVER')
my_email = os.getenv('MAIL_USERNAME')
my_password = os.getenv('MAIL_PASSWORD')
my_port = os.getenv('MAIL_PORT')
test_email = "wiyeja1188@scarden.com"

#  context = ssl.SSLContext(ssl.PROTOCOL_TLS)

with smtplib.SMTP_SSL(host=mail_server, port=my_port) as connection:
    print(connection.ehlo())
    # connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=test_email, msg="Hello World!")
    
# connection.close()
