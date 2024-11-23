import spacy
import random
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokens import Span

# Load the English language model
nlp = spacy.load("en_core_web_sm")

class ChatBot:
    def __init__(self, name):
        self.name = name
        self.conversation_topics = {
            "hello": ["Hi, how are you?", "Hello! How can I assist you?", "Hey, what's up?"],
            "how are you": ["I'm fine, thanks!", "I'm good, thanks!", "I'm just a chatbot, I don't have feelings, but thanks for asking!", "I'm good.", "I'm fine.", "Just fine."],
            "what is your name": ["My name is MyChatBot", "You can call me Chatti", "I'm MyChatBot, nice to meet you!"],
            "my name is": ["Nice name!", "Great name!", "Unique name!"],
            "thanks":["yor're welcome", "Sure", "no worries", "don't mention it", "my pleasure"],
            "how's your day": ["It's going well, thanks!", "I'm just a chatbot, I don't have days.", "I'm always ready to help, thanks for asking!"],
            "oh sad": ["Sorry to hear that.", "Is there anything I can do to help?", "I'm here to listen if you need to talk."],
            "yeah": ["I'm glad you're excited!", "How can I help you today?", "What's on your mind?"],
            "ummmmhh": ["I'm here to help if you need anything.", "Is there something on your mind?", "How can I assist you today?"],
            "oh ok": ["Is there anything else I can help you with?", "Let me know if you need anything else.", "I'm here if you need me."],
            "let's talk": ["What would you like to talk about?", "I'm all ears, what's on your mind?", "How can I help you today?"],
            "my day": ["Yeah, we can talk about it or anything else you want to talk about. I'm here to hear you.", "How was your day? I'm here to listen.", "What happened today? I'm all ears."],
            "default": ["I didn't understand that.", "Can you please rephrase?", "I'm not sure what you mean."]
        }
        self.matcher = Matcher(nlp.vocab)

    def respond(self, message):
        doc = nlp(message)
        message_text = doc.text.lower()
        for token in doc:
            if token.pos_ == "NOUN":
                print(f"Found noun: {token.text}")
            elif token.pos_ == "VERB":
                print(f"Found verb: {token.text}")
        for topic, responses in self.conversation_topics.items():
            if topic in message_text:
                return random.choice(responses)
        return random.choice(self.conversation_topics["default"])

    def entity_recognition(self, message):
        doc = nlp(message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

def main():
    chatbot = ChatBot("MyChatBot")
    print("Welcome to the chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        print("Bot:", chatbot.respond(user_input))
        entities = chatbot.entity_recognition(user_input)
        if entities:
            print("Entities found:")
            for entity in entities:
                print(entity)

if __name__ == "__main__":
    main()



