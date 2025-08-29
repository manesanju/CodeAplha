def get_bot_response(user_input):
    """
    Function to generate chatbot responses based on user input
    Uses if-elif statements to match patterns and return appropriate responses
    """
    # Convert input to lowercase for easier matching
    user_input = user_input.lower().strip()
    
    # Greeting responses
    if user_input in ["hello", "hi", "hey", "greetings"]:
        return "Hi there! 😊 How can I help you today?"
    
    elif user_input in ["good morning", "morning"]:
        return "Good morning! ☀️ Hope you're having a great day!"
    
    elif user_input in ["good evening", "evening"]:
        return "Good evening! 🌙 How was your day?"
    
    # How are you responses
    elif user_input in ["how are you", "how are you doing", "what's up", "whats up"]:
        return "I'm doing great, thank you for asking! 🤖 How about you?"
    
    elif user_input in ["i'm good", "im good", "i'm fine", "im fine", "good", "fine"]:
        return "That's wonderful to hear! 😄 What brings you here today?"
    
    elif user_input in ["i'm bad", "im bad", "not good", "terrible", "awful"]:
        return "I'm sorry to hear that. 😟 Is there anything I can help you with?"
    
    # Name and identity
    elif user_input in ["what's your name", "whats your name", "who are you"]:
        return "I'm a friendly chatbot! 🤖 You can call me ChatBot. What's your name?"
    
    elif user_input.startswith("my name is") or user_input.startswith("i'm ") or user_input.startswith("im "):
        name = user_input.replace("my name is", "").replace("i'm", "").replace("im", "").strip()
        if name:
            return f"Nice to meet you, {name.title()}! 👋"
        else:
            return "Nice to meet you! 👋"
    
    # Age questions
    elif user_input in ["how old are you", "what's your age", "whats your age"]:
        return "I'm timeless! ⏰ I was created recently but I don't age like humans do."
    
    # Weather (simple responses since we can't check real weather)
    elif "weather" in user_input:
        return "I can't check the weather for you, but I hope it's nice! ☀️🌤️"
    
    # Help and capabilities
    elif user_input in ["help", "what can you do", "commands"]:
        return """I can chat with you about various topics! Try saying:
• Hello, hi, good morning
• How are you, what's up
• What's your name, who are you
• Tell me a joke
• Help, bye
Just talk to me naturally! 💬"""
    
    # Jokes
    elif user_input in ["tell me a joke", "joke", "make me laugh"]:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! ⚛️",
            "Why did the Python programmer break up? They had too many arguments! 🐍",
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"
        ]
        import random
        return random.choice(jokes)
    
    # Time questions
    elif "time" in user_input:
        return "I don't have access to real-time data, but you can check your system clock! ⏰"
    
    # Thank you responses
    elif user_input in ["thank you", "thanks", "thx"]:
        return "You're very welcome! 😊 Happy to help!"
    
    # Compliments
    elif user_input in ["you're awesome", "youre awesome", "you're cool", "youre cool"]:
        return "Aww, thank you! 😊 You're pretty awesome yourself!"
    
    # Programming related
    elif "python" in user_input and "programming" in user_input:
        return "Python is amazing! 🐍 It's perfect for beginners and powerful for experts too!"
    
    elif "programming" in user_input or "coding" in user_input:
        return "Programming is such a useful skill! 💻 Are you learning to code?"
    
    # Goodbye responses
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! 👋 It was nice chatting with you. Have a great day!"
    
    # Default response for unrecognized input
    else:
        default_responses = [
            "I'm not sure I understand that. Can you try rephrasing? 🤔",
            "That's interesting! Tell me more about it. 💭",
            "I don't know much about that topic. What else would you like to chat about? 🗣️",
            "Hmm, I'm still learning! Try asking me something else. 🤖"
        ]
        import random
        return random.choice(default_responses)

def main():
    """Main chatbot function with conversation loop"""
    print("🤖 SIMPLE CHATBOT")
    print("=" * 20)
    print("Hi! I'm a friendly chatbot. Type 'help' to see what I can do.")
    print("Type 'bye' to exit the conversation.")
    print("=" * 20)
    
    # Main conversation loop
    while True:
        # Get user input
        user_message = input("\nYou: ")
        
        # Check if user wants to exit
        if user_message.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            print("Bot:", get_bot_response(user_message))
            break
        
        # Get and display bot response
        bot_response = get_bot_response(user_message)
        print("Bot:", bot_response)

# Run the chatbot
if __name__ == "__main__":
    main()