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
    gather.play(url)

    return response

@app.route("/", methods = ['GET', 'POST'])
def generate():
    menu = "Welcome to the Hypixel Zoo please press a number!"

    for idx, song in enumerate(url):
        if song is None:
            continue

            menu += "To listen to the song please press any button!"

            return menu

        if __name__ == "__main__":
            app.run()