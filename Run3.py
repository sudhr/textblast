import pandas as pd
import json
from twilio.rest import Client
import random

# Load data from CSV and JSON files
df = pd.read_csv("output.csv")
with open("content_templates.json", "r") as f:
    templates = json.load(f)

# Retrieve Twilio credentials (replace with your actual credentials)
account_sid = "AC0f8cd91456efae0fa8456ffacb651f84"
auth_token = "2687030f54735cd10bf935ebc5ac0a84"

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Get recipient phone number and address
    recipient_phone_number = row["Phone 1"]
    address = row["Property Address"]

    # Choose a random phone number from your Twilio account
    random_phone_number = random.choice(client.incoming_phone_numbers.list())
    sender_phone_number = random_phone_number.phone_number

    # Choose a random message template
    random_template = random.choice(templates)
    message_body = random_template["body"]

    # Replace variables in the message template with recipient data
    message_body = message_body.replace("{{first_name}}", row["First Name"])
    message_body = message_body.replace("{{last_name}}", row["Last Name"])
    message_body = message_body.replace("{{city}}", row["Property City"])
    message_body = message_body.replace("{{address}}", address)

    # Send the text message
    message = client.messages.create(
        body=message_body,
        from_=sender_phone_number,
        to=recipient_phone_number
    )

    print(f"Message sent to {recipient_phone_number} (SID: {message.sid})")

# The above script is fully functional and textblasts all contacts in output.csv