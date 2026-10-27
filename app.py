import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS match confirmation."""
    msg_body = request.form.get('Body', '').strip().lower()
    resp = MessagingResponse()
    
    if "sell" in msg_body:
        resp.message("AgriRoute: Harvest registered! Searching for drivers along your route with empty cargo capacity...")
    elif "route" in msg_body:
        resp.message("AgriRoute: Logistics availability logged. We will match you with local farmers shortly.")
    else:
        resp.message("Welcome to AgriRoute. Text 'SELL [Crop] [Weight]' or 'ROUTE [RouteName]' to begin.")
        
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
