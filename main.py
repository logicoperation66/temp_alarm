import requests
import re
import smtplib, ssl

port = 465 # For ssl
password = 'cl9s8Zm4'
sender_email = "piecwawrzyniak@gmail.com"
reciver_email = "adamwawrzyniak5@gmail.com"
message = """Temperatura krytyczna"""


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("piecwawrzyniak@gmail.com", password=password)
    server.sendmail(sender_email, reciver_email, message)


def get_temp():
    s = requests.session()
    url = "http://192.168.0.11"
    response = s.get(url=url)
    html = response.text
    temp = re.search(r'<span id="temperaturec">(.*?)</span>', html).group(1)
    return temp

print(get_temp)
temp = get_temp()
print(temp)