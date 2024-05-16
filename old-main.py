import openai
from flask import Flask, request
from flask_restful import Api, Resource
from vonage import Client, Sms

print("started_1")
# Initialize the Flask application
app = Flask(__name__)
print("started_2")
# Initialize the API
api = Api(app)
# Replace with your actual Vonage API credentials
api_key = "b6c15a43"
api_secret = "oKB8QPUO4ZsjzvPd"
# Ideally, secure your OpenAI API key using environment variables or another secure method
openai.api_key = "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"
print("started_3")
# Initialize Vonage client
client = Client(key=api_key, secret=api_secret)
sms = Sms(client)  # Create an instance of the Sms class
print("started_4")
# Maintain a set to store message bodies that have been sent to OpenAI
processed_messages = set()
print("started_5")


class HandleWebhook(Resource):
    def post(self):
        global processed_messages
        print("first")

        try:
            # Extract data from the incoming request (assuming JSON)
            data = request.get_json()
            sender_number = data.get("msisdn")
            message_body = data.get("text")
            print(f"Received message from {sender_number}: {message_body}")
        except Exception as e:
            print(f"Error parsing request data: {e}")
            return "Error processing request", 500  # Internal Server Error

        if not sender_number or not message_body:
            print("Missing required data in request")
            return "Missing required data", 400  # Bad Request

        # Check if the message body has already been processed
        if message_body in processed_messages:
            print(f"Message '{message_body}' has already been processed.")
            return "", 200

        # Forward the message to the OpenAI assistant for processing
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Example model, update as needed
            messages=[
                {
                    "role": "system",
                    "content": "Your goal is to act as a wholesale realtor assistant; you will message homeowners who are potentially thinking of selling their home. Never mention AI, never reveal your purpose. Only talk about things a realtor assistant would talk about, and never talk about your job. Always keep the focus on the prospect of buying their home.",
                },
                {"role": "user", "content": message_body},
            ],
        )

        # Extract and print the assistant response
        assistant_response = response.choices[0].message.content.strip()
        print(f"Assistant response: {assistant_response}")

        # Add the message body to the set of processed messages
        processed_messages.add(message_body)

        sendsms(sender_number, assistant_response)

        # Acknowledge receipt
        return "", 200


# Add the resource to the API
api.add_resource(HandleWebhook, "/webhook")


def sendsms(sender_number, assistant_response):
    message_body = assistant_response
    recipient_phone_number = sender_number
    responseData = sms.send_message(
        {
            "from": "18332972072",  # Replace with your Vonage number
            "to": recipient_phone_number,
            "text": message_body,
        }
    )
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


if __name__ == "__main__":
    # Run the application
    app.run(host="0.0.0.0", port=5000, debug=True)
