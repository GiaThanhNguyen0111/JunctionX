import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Define the intents
intents = {
    'greeting': ['hello', 'hi', 'hey'],
    'goodbye': ['bye', 'goodbye', 'see you later'],
    'order': ['I want to order', 'Can I order', 'I would like to order'],
    'payment': ['How can I pay', 'What payment methods do you accept']  
}

# Define the responses for each intent
responses = {
    'greeting': 'Hello! How can I assist you today?',
    'goodbye': 'Goodbye! Have a nice day!',
    'order': 'Sure, what would you like to order?',
    'payment': 'We accept credit cards and PayPal. Which one would you like to use?'
}

# Define the function to preprocess user input
def preprocess_input(input):
    # Tokenize the input
    tokens = word_tokenize(input.lower())
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if not token in stop_words]
    
    # Remove punctuation and numbers
    filtered_tokens = [token for token in filtered_tokens if token.isalpha()]
    
    # Join the filtered tokens back into a string
    preprocessed_input = ' '.join(filtered_tokens)
    
    return preprocessed_input

# Define the function to recognize intents and extract information
def get_intent(input):
    preprocessed_input = preprocess_input(input)
    
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in preprocessed_input:
                return intent
            
    return None

# Define the main function for the chatbot
def chatbot():
    print('Welcome to the chatbot!')
    while True:
        # Get user input
        user_input = input('> ')
        
        # Get the intent
        intent = get_intent(user_input)
        
        # Respond based on the intent
        if intent is None:
            print('I am sorry, may I help you?')
        else:
            response = responses[intent]
            print(response)

# Run the chatbot
chatbot()
