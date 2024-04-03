import csv
import random
import json

# Replace these with your actual Twilio account credentials
account_sid = "AC0f8cd91456efae0fa8456ffacb651f84"
auth_token = "2687030f54735cd10bf935ebc5ac0a84"

# Read content templates (modify based on your chosen storage method)
with open("content_templates.json", "r") as f:
    content_templates = json.load(f)

# Function to send personalized SMS using Twilio API
def send_personalized_sms(first_name, phone_number, template_body):
    client = Client(account_sid, auth_token)

    # Personalize the message body with first name
    personalized_message = template_body.format(first_name=first_name)

    # Send the SMS using Twilio with chosen template content
    client.messages.create(
        from_="YOUR_TWILIO_PHONE_NUMBER",
        to=phone_number,
        body=personalized_message
    )

    print(f"Sent personalized SMS: {personalized_message} to {phone_number}")

# Read first names and phone numbers from CSV file
first_names = []
phone_numbers = []
with open("output.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        first_names.append(row["First Name"])
        phone_numbers.append(row["Phone 1"])

# Check if data was parsed correctly
if not first_names or not phone_numbers:
    print("Error: Couldn't find first names or phone numbers in the CSV file!")
    exit(1)

# Send personalized SMS for each recipient
for first_name, phone_number in zip(first_names, phone_numbers):
    # Randomly select and personalize a template
    selected_template = random.choice(content_templates)
    send_personalized_sms(first_name, phone_number, selected_template["body"])