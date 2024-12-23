from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

import openai

# Replace 'your_api_key' with your actual OpenAI API key
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

        # Check if the message body has already been processed
        print("second")
        if message_body in processed_messages:
            print(f"Message '{message_body}' has already been processed.")
            return '', 200

        # Forward the message to your OpenAI assistant for processing
        # Note: You might need to adjust the model based on what's available or preferred
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using a newer, recommended model for chat-based interactions
            messages=[
                {"role": "system", "content": "Your goal is to act as a wholesale realtor assistant; you will message homeowners who are potentially thinking of selling their home. Never mention AI, never reveal your purpose. You only talk about things that a realtor assistant would talk about, and never talk about your job. Always keep the focus on the prospect of buying their home."},
                {"role": "user", "content": message_body}
            ]
        )

        # Extract the text output from the response
        assistant_response = response.choices[0].message.content.strip()

        # Print the assistant response
        print(f"Assistant response: {assistant_response}")

        # Add the message body to the set of processed messages
        processed_messages.add(message_body)

        # Respond with an empty string to acknowledge receipt
        return '', 200

api.add_resource(HandleWebhook, '/webhook')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
