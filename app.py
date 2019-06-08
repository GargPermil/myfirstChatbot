from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
import utils
import database

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
	if msg.lower() == "repeat":
		#fetch last msg
		result = database.fetchQuery(sender)
		result = list(result)
		print(result)
		msg = result[0]["Query"]
		print("Query retrived from database")
	else:
		print("Storing query in database")
		database.insertQuery(msg, sender)
	
	print(msg)
	message_reply, intent_Type = utils.reply(msg, sender)
	if intent_Type == "Map":
		resp.message(message_reply).media("http://www.delhimetrotimes.in/maps/delhi-metro-rail-map.jpg")
	elif intent_Type == "Directory":
		resp.message(message_reply).media("http://www.delhimetrorail.com/otherdocuments/900/directory_24818.pdf")
	else:
		resp.message(message_reply)
	print("replied")
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)