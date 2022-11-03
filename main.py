import requests
import re
import smtplib, ssl
from dotenv import load_dotenv
import os 

load_dotenv()

port = 465
password = os.getenv("PASSWORD")
sender_email = os.getenv('ADMIN_EMAIL')
reciver_email = os.getenv('RECIVER_EMAIL')

def get_temp():
    s = requests.session()
    url = "http://192.168.0.11"
    response = s.get(url=url)
    html = response.text
    temp = re.search(r'<span id="temperaturec">(.*?)</span>', html).group(1)
    return temp
    
temp = get_temp()
message = f"Temperature is high !!!{temp}"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(f"{sender_email}", password=password)
    server.sendmail(sender_email, reciver_email, message)


temp = get_temp()

