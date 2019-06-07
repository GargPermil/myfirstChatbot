from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
import utils


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/sms", methods=["POST"])
def sms():
	"""Respond to incoming calls with a simple text message."""
	# Fetch the message
	msg = request.form.get('Body')
	sender = request.form.get('From')
	print("reading message")
	# Create reply
	resp = MessagingResponse()
	resp.message(utils.fetch_reply(msg, sender)).media("http://www.delhimetrotimes.in/maps/delhi-metro-rail-map.jpg")
	print("replied")
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
