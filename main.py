from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    """Handles incoming WhatsApp messages"""
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()
    message = response.message()

    # Simple auto-response logic
    if "hi" in incoming_msg or "hello" in incoming_msg:
        message.body("Hello! How can I assist you today?")
    elif "support" in incoming_msg:
        message.body("For support, reply with your issue or visit our website.")
    else:
        message.body("I'm an AI bot. Type 'help' for assistance.")

    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
