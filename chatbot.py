import nltk
import random

# Install nltk and download necessary resources (if not already done)
nltk.download("punkt")
nltk.download("wordnet")

from nltk.chat.util import Chat, reflections

# Define responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?", "Hi there, %1! How can I assist you?"],
    ],
    [
        r"what is your name?",
        ["I am a chatbot.", "My name is ChatGPT, your friendly chatbot."],
    ],
    [
        r"how are you?",
        ["I'm doing well, thanks for asking!", "I'm just a computer program, but I'm here to help."],
    ],
    [
        r"(.*) (good|great|fine)",
        ["That's good to hear!", "Awesome! How can I assist you today?"],
    ],
    [
        r"(.*) (sorry|apologize)",
        ["No need to apologize. How can I help you?", "It's okay. How can I assist you today?"],
    ],
    [
        r"quit",
        ["Goodbye!", "It was nice chatting with you. Have a great day!"],
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you please rephrase that?", "Can you provide more details?"],
    ],
]

# Create and initialize the chatbot
chatbot = Chat(pairs, reflections)

# Start the chat
print("Hello! I'm your chatbot. Type 'quit' to exit.")
chatbot.converse()
