import requests
import re

def get_temp(url):
    s = requests.session()
    response = s.get(url=url)
    html = response.text
    temp = re.search(r'<span id="temperaturec">(.*?)</span>', html).group(1)
    s.close()
    return temp