from pushbullet import PushBullet
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")


def pb_sender(text:str, temp:float):
    pb = PushBullet(access_token)
    push = pb.push_note(f"{text}", f"Temperatura: {temp}")
    return 0



