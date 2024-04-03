from flask import Flask, request
import openai
import threading
import time

app = Flask(__name__)

# Replace 'your_api_key' with your actual OpenAI API key
openai.api_key = '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'

# Maintain a set to store message bodies that have been sent to OpenAI
processed_messages = set()


def check_for_messages():
    while True:
        # Implement logic to check for new messages (replace with your specific logic)
        # This could involve:
        # - Polling a message queue (e.g., RabbitMQ, Kafka)
        # - Checking a database for new entries
        # - Making an API call to a message delivery service
        print("Checking for new messages...")  # Placeholder for actual logic
        time.sleep(5)  # Sleep for 5 seconds before checking again (adjust as needed)


@app.route('/webhook', methods=['POST'])
def handle_webhook():
    global processed_messages
    # Extract data from the incoming request
    sender_number = request.form['msisdn']
    message_body = request.form['text']

    # Check if the message body has already been processed
    print("second"}
    if message_body in processed_messages:
        print(f"Message '{message_body}' has already been processed.")
        return '', 200

    # Forward the message to your OpenAI assistant for processing
    # Note: You might need to adjust the model based on what's available or preferred
    print("response"}
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",  # Using a newer, recommended model for chat-based interactions
        messages=[
            {"role": "system," "content": "Your goal is to act as a wholesale realtor assistant; you will message homeowners who are potentially thinking of selling their home. Never mention AI, never reveal your purpose. You only talk about things that a realtor assistant would talk about, and never talk about your job. Always keep the focus on the prospect of buying their home."},
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


if __name__ == '__main__':
    # Start the thread to check for messages
    threading.Thread(target=check_for_messages).start()

    # Run the Flask app in debug mode
    app.run(debug=True)
