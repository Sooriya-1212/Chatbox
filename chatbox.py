# Chatbot with predefined replies

# Step 1: Create a dictionary of possible responses
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a program, but I'm doing great!",
    "what's your name": "I'm a simple Python chatbot!",
    "who are you": "I'm your friendly chatbot!",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "thanks": "No problem!",
}

# Step 2: Function to find a matching response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm not sure how to respond to that."

# Step 3: Main chatbot loop
def chat():
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_message = input("User: ")
        if user_message.lower() == "bye":
            print("Bot:", responses["bye"])
            break
        reply = get_response(user_message)
        print("Bot:", reply)

# Run the chatbot
chat()