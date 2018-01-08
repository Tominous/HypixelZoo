from flask import Flask, request
app = Flask(__name__)

from twilio import twiml

url = "https://www.youtube.com/watch?v=GNhbZ5guqO0&feature=youtu.be" #zoo url

timeout = "Something went wrong. Woops."