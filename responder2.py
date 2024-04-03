import openai

# Set up OpenAI API client with the provided API key
openai.api_key = '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'

def ask_assistant(question):
    # Define the prompt to ask your assistant
    prompt = f"Ask asst_nEU3pVkOYEjB3OAFTLXSOT5T: {question}"

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=50
    )

    # Extract the response from OpenAI
    assistant_response = response.choices[0].text.strip()

    return assistant_response

if __name__ == '__main__':
    question = "hi, who are you?"
    assistant_response = ask_assistant(question)
    print("Assistant's response:", assistant_response)
