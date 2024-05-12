# OpenAI Example

```python
import openai
import os

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
  # Create a list to store all the messages for context
  messages = [
    {"role": "system", "content": "You are a helpful assistant."},
  ]

  # Keep repeating the following
  while True:
    # Prompt user for input
    message = input("User: ")

    # Exit program if user inputs "quit"
    if message.lower() == "quit":
      break

    # Add each new message to the list
    messages.append({"role": "user", "content": message})

    # Request gpt-3.5-turbo for chat completion
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    # Print the response and add it to the messages list
    chat_message = response['choices'][0]['message']['content']
    print(f"Bot: {chat_message}")
    messages.append({"role": "assistant", "content": chat_message})

if __name__ == "__main__":
  print("Start chatting with the bot (type 'quit' to stop)!")
  chatbot()
```

## Note

1. Setup the initial context for the conversation by using `system` role.
2. Keep the complete conversation in the database and this needs to be provided to the bot.
3. Use `user` and `assistant` roles to identify the conversation.
4. Use `gpt-4-turbo` model.
