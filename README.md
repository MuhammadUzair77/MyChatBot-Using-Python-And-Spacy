# MyChatBot

**MyChatBot** is an interactive chatbot built using Python and the SpaCy NLP library. This chatbot demonstrates natural language processing capabilities, including token analysis, named entity recognition (NER), and conversational AI.

## Features

- **Conversational Responses**: Provides context-aware responses based on predefined topics.
- **Natural Language Processing (NLP)**: Utilizes SpaCy to process user inputs, including token identification (nouns, verbs) and named entity recognition (NER).
- **Dynamic Interactions**: Generates varied responses using random selection for a more engaging conversation.
- **Entity Recognition**: Extracts named entities from user inputs and displays their types (e.g., PERSON, DATE, ORG).
- **Customizable Topics**: Easily modify or expand conversation topics and responses in the chatbot's code.

## How It Works

1. **Message Processing**:
   - The chatbot processes user inputs with SpaCy's `en_core_web_sm` model.
   - It identifies key parts of speech (nouns, verbs) and entities.

2. **Conversation Flow**:
   - Matches user input to predefined topics and provides relevant responses.
   - Falls back to a default response if the input doesn't match any topic.

3. **Entity Recognition**:
   - Displays entities from user messages (e.g., names, dates, locations).

4. **Interactive Chat**:
   - Users can chat with the bot through a simple command-line interface.

## Requirements

- Python 3.6 or higher
- SpaCy library
- SpaCy language model `en_core_web_sm`

Install dependencies:
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

### Example Interaction
```plaintext
User: Hello
Bot: Hi, how are you?

User: My name is Uzair
Bot: Nice name!
Entities found:
('Uzair', 'PERSON')

User: What's the date today?
Bot: I didn't understand that.
Entities found:
('today', 'DATE')
```

Type `quit` to exit the chat.

## Customization

- Add new conversation topics and responses in the `conversation_topics` dictionary.
- Enhance NLP features using SpaCy's additional functionalities.

