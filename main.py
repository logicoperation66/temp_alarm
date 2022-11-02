import requests
import re
import pywhatkit


s = requests.session()
url = "http://192.168.0.11"
response = s.get(url=url)


s = response.text
temp = re.search(r'<span id="temperaturec">(.*?)</span>', s).group(1)
print(temp)

if temp > '65':
    pywhatkit.sendwhatmsg_instantly('+48510306985', 'testowa wiadomosc', 10)
else:
    pywhatkit.sendwhatmsg_instantly('+48510306985', 'testowa wiadomosc elsa', 10)