import requests
import re
import smtplib, ssl
from dotenv import load_dotenv
import os 

load_dotenv()

port = 465   # SMTP port
password = os.getenv("PASSWORD")
sender_email = os.getenv('ADMIN_EMAIL')
reciver_email = os.getenv('RECIVER_EMAIL')
url = os.getenv('URL')


def get_temp(url):
    s = requests.session()
    response = s.get(url=url)
    html = response.text
    temp = re.search(r'<span id="temperaturec">(.*?)</span>', html).group(1)
    s.close()
    return temp

def send_mail(text):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(f"{sender_email}", password=password)
        server.sendmail(sender_email, reciver_email, text)
    return 0


if __name__ == "__main__":
    temp = get_temp(url)
    if float(temp) > 68:
        massage = f"UWAGA!!! Temperatura pieca rosnie {temp}"
        send_mail(massage)

