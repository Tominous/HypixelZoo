from flask import Flask, request
app = Flask(__name__)

from twilio import twiml

url = "https://www.youtube.com/watch?v=GNhbZ5guqO0&feature=youtu.be" #zoo url

timeout = "Something went wrong. Woops."

def play(tune):
    if tune is None:
        return

    response = twiml.Response()

    gather = response.gather(numDigits = 1, timeout = 10)
    gather.playt(url)

    return response