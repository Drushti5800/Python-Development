import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from tkinter import Tk, Text, Scrollbar, Entry, Button, END
import nltk.data

# Download necessary data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Function to calculate similarity
def get_similarity(user_input, bot_keywords):
    user_words = set(word_tokenize(user_input.lower()))
    max_similarity = 0
    for keyword in bot_keywords:
        synsets_keyword = wordnet.synsets(keyword)
        for word in user_words:
            synsets_word = wordnet.synsets(word)
            for synset1 in synsets_keyword:
                for synset2 in synsets_word:
                    similarity = synset1.wup_similarity(synset2) or 0
                    max_similarity = max(max_similarity, similarity)
    return max_similarity

# Enhanced response function
def chatbot_response(user_input):
    # Knowledge base
    responses = {
        "greeting": (["hello", "hi", "hey"], "Hello! How can I assist you today?"),
        "farewell": (["bye", "goodbye"], "Goodbye! Have a great day!"),
        "thanks": (["thanks", "thank you"], "You're welcome! Glad to help."),
        "how_are_you": (["how", "are", "you"], "I'm just a bot, but I'm here to help!"),
        "default": ([], "I'm sorry, I didn't understand that. Could you rephrase?"),
    }
    
    # Match response based on similarity
    max_similarity = 0
    selected_response = responses["default"][1]
    
    for intent, (keywords, response) in responses.items():
        similarity = get_similarity(user_input, keywords)
        if similarity > max_similarity:
            max_similarity = similarity
            selected_response = response
    
    return selected_response

# GUI for Chatbot
class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("500x600")
        
        # Chat log display
        self.chat_log = Text(root, bg="light gray", state="normal", wrap='word', font=("Arial", 12))
        self.chat_log.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Scroll bar for chat log
        scrollbar = Scrollbar(self.chat_log)
        scrollbar.pack(side="right", fill="y")
        self.chat_log['yscrollcommand'] = scrollbar.set
        
        # Input field
        self.user_input = Entry(root, font=("Arial", 14))
        self.user_input.pack(padx=10, pady=5, fill="x")
        self.user_input.bind("<Return>", self.send_message)
        
        # Send button
        send_button = Button(root, text="Send", font=("Arial", 12), command=self.send_message)
        send_button.pack(pady=5)
    
    # Display user and bot messages
    def send_message(self, event=None):
        user_text = self.user_input.get().strip()
        if not user_text:
            return
        
        self.chat_log.insert(END, f"You: {user_text}\n")
        bot_response = chatbot_response(user_text)
        self.chat_log.insert(END, f"Bot: {bot_response}\n\n")
        self.chat_log.see(END)
        self.user_input.delete(0, END)

# Main Function
if __name__ == "__main__":
    root = Tk()
    chatbot_gui = ChatBotGUI(root)
    root.mainloop()




















"""import numpy as np
import nltk
import string
import random

f=open('chatbot.txt','r',error='ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower() #convert text to lowercase
nltk.download('punkt') #Using the punkt tokenize
nltk.download('wordnet') #Using the WordNet dictionary
sent_tokens = nltk.sent_tokenize(raw_doc) #convert doc to list of sentences
word_tokens = nltk.word_tokenize(raw_doc) #convert doc to list of words"""