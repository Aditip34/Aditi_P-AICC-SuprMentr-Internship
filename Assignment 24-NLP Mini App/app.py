# app.py

def chatbot():
    print("Chatbot (type 'exit' to stop)")
    
    while True:
        user = input("You: ").lower()
        
        if user == "hi":
            print("Bot: Hello!")
        elif "name" in user:
            print("Bot: I am a chatbot")
        elif user == "exit":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand")

chatbot()