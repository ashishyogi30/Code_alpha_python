def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I don't understand that."
    
print("=== Welcome to Basic Chatbot ===")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot:", response)

    if "bye" in user_input.lower():
        break
