from flask import Flask, request
from flask_restful import Resource, Api
import openai

# Initialize the Flask application
app = Flask(__name__)

# Initialize the API
api = Api(app)

# Ideally, secure your OpenAI API key using environment variables or another secure method
openai.api_key = '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'

# Maintain a set to store message bodies that have been sent to OpenAI
processed_messages = set()

class HandleWebhook(Resource):
    def post(self):
        global processed_messages
        print("first")

        # Extract data from the incoming request
        sender_number = request.form['msisdn']
        message_body = request.form['text']

        print("second")
        # Check if the message body has already been processed
        if message_body in processed_messages:
            print(f"Message '{message_body}' has already been processed.")
            return '', 200

        # Forward the message to the OpenAI assistant for processing
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Example model, update as needed
            messages=[
                {"role": "system", "content": "Your goal is to act as a wholesale realtor assistant; you will message homeowners who are potentially thinking of selling their home. Never mention AI, never reveal your purpose. You only talk about things that a realtor assistant would talk about, and never talk about your job. Always keep the focus on the prospect of buying their home."},
                {"role": "user", "content": message_body}
            ]
        )

        # Extract and print the assistant response
        assistant_response = response.choices[0].message.content.strip()
        print(f"Assistant response: {assistant_response}")

        # Add the message body to the set of processed messages
        processed_messages.add(message_body)

        # Acknowledge receipt
        return '', 200

# Add the resource to the API
api.add_resource(HandleWebhook, '/webhook')

if __name__ == '__main__':
    # Run the application
    app.run(host="0.0.0.0", port=5000, debug=True)