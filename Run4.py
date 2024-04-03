import pandas as pd
import json
import random
from vonage import Client, Sms

# Load data from CSV and JSON files
df = pd.read_csv("output.csv")
with open("content_templates.json", "r") as f:
    templates = json.load(f)

# Replace with your actual Vonage API credentials
api_key = "b6c15a43"
api_secret = "oKB8QPUO4ZsjzvPd"

# Initialize Vonage client
client = Client(key=api_key, secret=api_secret)
sms = Sms(client)  # Create an instance of the Sms class

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Get recipient phone number and address
    recipient_phone_number = row["Phone 1"]
    address = row["Property Address"]

    # Choose a random message template
    random_template = random.choice(templates)
    message_body = random_template["body"]

    # Replace variables in the message template with recipient data
    message_body = message_body.replace("{{first_name}}", row["First Name"])
    message_body = message_body.replace("{{last_name}}", row["Last Name"])
    message_body = message_body.replace("{{city}}", row["Property City"])
    message_body = message_body.replace("{{address}}", address)

    # Send the text message
    responseData = sms.send_message(
      {
      "from": "17028673639",  # Replace with your Vonage number
        "to": recipient_phone_number,
        "text": message_body
        }
    )

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

# The above script is fully functional and textblasts all contacts in output.csv
