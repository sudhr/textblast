from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Extract data from the incoming request
    sender_number = request.form['msisdn']
    message_body = request.form['text']

    # Process the incoming message (e.g., interact with OpenAI)
    # For now, let's just print the details
    print(f"Received message from {sender_number}: {message_body}")

    # Respond with an empty string to acknowledge receipt
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
