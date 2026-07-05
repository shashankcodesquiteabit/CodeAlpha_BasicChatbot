"""
Basic Rule-Based Chatbot
CodeAlpha Python Programming Internship

A simple chatbot that responds to user input using predefined rules.
Concepts used: if-elif, functions, loops, input/output.
"""

import random


def get_response(user_input):
    """
    Takes user input (string), matches it against known patterns,
    and returns an appropriate chatbot reply.
    """
    text = user_input.lower().strip()

    # Greetings
    if text in ("hello", "hi", "hey", "hii", "helo"):
        return random.choice(["Hi there!", "Hello!", "Hey! How can I help you today?"])

    # How are you
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    elif text in ("i am fine", "i'm fine", "good", "great", "doing well"):
        return "Glad to hear that! 😊"

    # Name
    elif "your name" in text:
        return "I'm a simple chatbot built with Python!"

    elif "my name is" in text:
        name = text.split("my name is")[-1].strip().title()
        return f"Nice to meet you, {name}!"

    # Help
    elif "help" in text:
        return "I can chat about greetings, how you're doing, my name, or jokes. Try saying 'hello' or 'tell me a joke'."

    # Jokes
    elif "joke" in text:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to therapy? It had too many issues to process!",
            "Why do Python programmers wear glasses? Because they can't C!",
        ]
        return random.choice(jokes)

    # Thanks
    elif text in ("thanks", "thank you", "thx"):
        return "You're welcome!"

    # Farewell
    elif text in ("bye", "goodbye", "exit", "quit", "see you"):
        return "Goodbye! Have a great day!"

    # Fallback
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def chat():
    """Runs the main chatbot loop."""
    print("=" * 50)
    print(" Simple Chatbot (type 'bye' or 'exit' to quit)")
    print("=" * 50)

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            print("Bot: Please type something!")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit", "see you"):
            break


if __name__ == "__main__":
    chat()
