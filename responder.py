from flask import Flask, request
import openai

app = Flask(__name__)

# Set up OpenAI API client with your API key
openai.api_key = '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'

# Maintain a set to store message bodies that have been sent to OpenAI
processed_messages = set()

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    global processed_messages

    # Extract data from the incoming request
    sender_number = request.form['msisdn']
    message_body = request.form['text']

    # Check if the message body has already been processed
    if message_body in processed_messages:
        print(f"Message '{message_body}' has already been processed.")
        return '', 200

    # Forward the message to your OpenAI assistant for processing
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=message_body,
        max_tokens=150
    )

    # Extract the response from OpenAI
    assistant_response = response.choices[0].text.strip()

    # Print the assistant response
    print(f"Assistant response: {assistant_response}")

    # Add the message body to the set of processed messages
    processed_messages.add(message_body)

    # Respond with an empty string to acknowledge receipt
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
