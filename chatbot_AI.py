import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from tkinter import Tk, Text, Scrollbar, Entry, Button, END

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Function to calculate similarity between user input and bot keywords
def get_similarity(user_input, bot_keywords):
    user_words = set(word_tokenize(user_input.lower()))
    max_similarity = 0
    for keyword in bot_keywords:
        for word in user_words:
            keyword_synsets = wordnet.synsets(keyword)
            user_synsets = wordnet.synsets(word)
            for syn1 in keyword_synsets:
                for syn2 in user_synsets:
                    similarity = syn1.wup_similarity(syn2) or 0
                    max_similarity = max(max_similarity, similarity)
    return max_similarity

# Chatbot Response Logic
def chatbot_response(user_input):
    responses = {
        "greeting": (["hello", "hi", "hey"], "Hello! How can I assist you today?"),
        "farewell": (["bye", "goodbye"], "Goodbye! Have a great day!"),
        "nationality": (["nationality", "what is the nationality of india"], 
                        "The nationality of India is referred to as 'Indian.' People from India are called Indians."),
        "culture": (["tell me about indian culture", "culture of india"], 
                    "Indian culture is diverse and rich, characterized by traditions, festivals, languages, and art."),
        "symbols": (["national symbols", "symbols of india"], 
                    "India's national symbols include:\n- National Animal: Tiger\n- National Bird: Peacock\n- National Flower: Lotus"),
        "independence": (["independence day", "when did india gain independence"], 
                         "India gained independence on August 15, 1947."),
        "languages": (["languages", "what languages are spoken in india"], 
                      "India has 22 officially recognized languages, including Hindi and English."),
        "default": ([], "I'm sorry, I didn't understand that. Could you rephrase?"),
    }
    
    max_similarity = 0
    selected_response = responses["default"][1]
    
    for intent, (keywords, response) in responses.items():
        similarity = get_similarity(user_input, keywords)
        if similarity > max_similarity and similarity > 0.2:  # Ensure a minimum similarity threshold
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
