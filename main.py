from dotenv import load_dotenv
import os
from esp_graber import get_temp
from pb_sender import pb_sender
import time

load_dotenv()

url = os.getenv('URL')


if __name__ == "__main__":
    while True:
        temp = get_temp(url)
        if float(temp) >= 70:
            text = "Uwaga! Temp. rośnie"
            pb_sender(text, temp)
            time.sleep(30)
        elif float(temp) < 68:
            time.sleep(30)
            continue
        else:
            text = "Wystapił jakis błąd"
            pb_sender(text, temp)
            time.sleep(30)
        continue