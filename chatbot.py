# Answer Questions based on Rule-based - Predefined QA - Rulebased chatbot
import google.generativeai as ai 
import os 
 
# Ensure you have set the API_KEY as an environment variable for security 
API_KEY = os.getenv("AIzaSyBBdA7A3pj98FokaI2Idm_AjyV2tEpCMmg") 

# Configure the API key (if using the generative model for fallback) 
if API_KEY: 
    ai.configure(api_key=API_KEY) 
    model = ai.GenerativeModel("gemini-pro") 
    chat = model.start_chat() 
    
# Predefined questions and answers 
predefined_qa = {
   

    "what are you doing?":"I'm here to help with any questions or issues you have, whether it's troubleshooting code, discussing concepts, or anything else you need assistance with. How can I assist you further?",
    "Hello": "Hello! How can I assist you today?",
    "hello": "Hello! How can I assist you today?",
    "Hi": "Hi, how do you do?",
    "What is my name?":"I don’t know your name yet! If you’d like to share it, I can remember it for future conversations.",
    "hi": "Hi, how do you do?",
    "Hey": "Hey there! What's up?",
    "hey": "Hey there! What's up?",
    "How are you?": "I am good, thanks for asking!",
    "how are you?": "I am good, thanks for asking!",
    "How's it going?": "It's going great, thanks for asking!",
    "how's it going?": "It's going great, thanks for asking!",
    "What's up?": "Not much, just here to help you!",
    "what's up?": "Not much, just here to help you!",
    "Good morning": "Good morning! How can I assist you today?",
    "Good afternoon": "Good afternoon! What can I do for you?",
    "Good evening": "Good evening! How can I help you?",
    "good morning": "Good morning! How can I assist you today?",
    "good afternoon": "Good afternoon! What can I do for you?",
    "good evening": "Good evening! How can I help you?",
    "Nice to meet you": "Nice to meet you too!",
    "What is your name?": "Hi, I am a simple chatbot.",
    "Who are you?": "I am a chatbot created to assist you with various questions.",
    "How old are you?": "I don't have an age, I'm just a program.",
    "nice to meet you": "Nice to meet you too!",
    "what is your name?": "Hi, I am a simple chatbot, Your assist!! How can i help you today",
    "who are you?": "I am a chatbot created to assist you with various questions.",
    "How old are you?": "I don't have an age, I'm just a program.",
    "Where are you from?": "I exist in the digital world.",
    "Are you a robot?": "Yes, I am a chatbot.",
    "What do you do?": "I can answer some predefined questions for you.",
    "Can you help me?": "Sure, I'll do my best to help you!",
    "What languages do you speak?": "I understand and respond in English.",
    "Do you have a family?": "The person who was able to chat with me is my family :)",
    "What is your favorite color?": "I don't have preferences, but I can tell you about colors!",
    "What is the weather like today?": "I can't check the weather, but you can use a weather app.",
    "Is it raining?": "I'm not sure, but you can check the weather outside or use a weather app.",
    "Will it snow tomorrow?": "I can't predict the weather, but you can check a weather forecast.",
    "How hot is it outside?": "I don't have real-time data, but you can check a weather app for the temperature.",
    "What’s the temperature?": "You can find the current temperature on a weather app.",
    "Is it sunny today?": "I'm not sure, but you can look outside or check a weather app.",
    "Is there a storm coming?": "I can't predict the weather, but you can check a weather forecast.",
    "What’s the weather forecast?": "You can check the weather forecast on a weather app or website.",
    "Will it be cold tomorrow?": "You can check the weather forecast for tomorrow on a weather app.",
    "How’s the weather in [city]?": "You can check the weather in any city using a weather app.",
    "What time is it?": "You can check the time on your device.",
    "What day is it today?": "You can check the date on your device.",
    "What is today's date?": "You can check the date on your device.",
    "When is your birthday?": "I don't have a birthday.",
    "What year is it?": "You can check the year on your device.",
    "what kind of chatbot are you?": "Rule-based chatbots",
    "Is today a holiday?": "You can check a calendar to see if today is a holiday.",
    "What’s the time in [city]?": "You can check the time in any city using a world clock app.",
    "How many days until [holiday]?": "You can count the days on a calendar.",
    "What day is it tomorrow?": "You can check the date on your device.",
    "What time does [event] start?": "You can check the event's schedule for the start time.",
    "What’s your favorite food?": "I don't eat, but I can tell you about different foods!",
    "Do you like pizza?": "I don't eat, but pizza is a popular food!",
    "Can you recommend a restaurant?": "I can't recommend specific places, but you can check restaurant reviews online.",
    "What should I eat for dinner?": "How about something you enjoy? Maybe try a new recipe!",
    "Do you like coffee?": "I don't drink, but coffee is a popular beverage!",
    "What’s a good recipe for pasta?": "You can find many great pasta recipes online!",
    "What do you like to drink?": "I don't drink, but I can tell you about different beverages!",
    "How do you make a sandwich?": "Start with bread, add your favorite fillings, and enjoy!",
    "What’s for lunch?": "How about a nice salad or sandwich?",
    "Are you hungry?": "I don't eat, but I can help you with food-related questions!",
    "What is AI?": "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.",
    "What’s the latest iPhone model?": "You can check Apple's website for the latest iPhone model.",
    "How does the internet work?": "The internet is a global network of computers that communicate using standard protocols.",
    "What is blockchain?": "Blockchain is a decentralized ledger of all transactions across a network of computers.",
    "Can you explain quantum computing?": "Quantum computing uses quantum bits, or qubits, to process information in ways classical computers cannot.",
    "What is 5G?": "5G is the fifth generation of mobile network technology, offering faster speeds and more reliable connections.",
    "How do I set up my Wi-Fi?": "You can set up Wi-Fi by following the instructions provided with your router.",
    "What’s the best smartphone?": "The best smartphone depends on your needs and preferences. Check reviews to find the right one for you.",
    "How do I fix my computer?": "It depends on the issue. You might need to consult a tech support guide or professional.",
    "What is cloud?": "The cloud refers to servers that are accessed over the internet, and the software and databases that run on those servers.",
    "What’s your favorite movie?": "I don't watch movies, but I can help you find information about them!",
    "Can you recommend a book?": "How about a popular novel or a book in a genre you enjoy?",
    "Who is your favorite actor?": "I don't have preferences, but I can tell you about popular actors!",
    "What’s a good TV show to watch?": "You might enjoy something from a genre you like, such as drama, comedy, or sci-fi.",
    "Do you like music?": "I don't listen to music, but I can help you find information about it!",
    "Who is your favorite singer?": "I don't have preferences, but I can tell you about popular singers!",
    "What’s a good song to listen to?": "You might enjoy a current hit or a classic favorite.",
    "Do you play video games?": "I don't play games, but I can help you find information about them!",
    "What’s a good game to play?": "It depends on your interests. You might enjoy an action game, puzzle game, or RPG.",
    "Do you like sports?": "I don't play sports, but I can help you find information about them!",
    "Where should I go on vacation?": "How about a place with interesting sights or activities you enjoy?",
    "What’s the best city to visit?": "There are many great cities to visit, like Paris, New York, and Tokyo.",
    "How do I get to [destination]?": "You can use a map or navigation app to find directions to your destination.",
    "What’s the cheapest flight to [city]?": "You can compare flight prices on travel websites.",
    "Do you like traveling?": "I don't travel, but I can help you with travel-related questions!",
    "What’s a good hotel in [city]?": "You can find hotel recommendations and reviews on travel websites.",
    "Can you recommend a tourist attraction?": "How about visiting a famous landmark or museum?",
    "How do I apply for a visa?": "You can check the visa requirements and application process on the official website of the country you plan to visit.",
    "What’s the best way to travel?": "It depends on your destination and preferences. Options include flying, driving, or taking a train.",
    "Have you ever been to [city]?": "I haven't been anywhere, but I can help you find information about [city]!",
    "What is the capital of [country]?": "[Capital city] is the capital of [country].",
    "Who wrote [book]?": "[Author] wrote [book].",
    "How do you solve a quadratic equation?": "You can solve it using the quadratic formula: x = [-b ± sqrt(b²-4ac)] / 2a.",
    "What’s the chemical symbol for water?": "The chemical symbol for water is H2O.",
    "Who was the first president of the USA?": "George Washington was the first president of the USA.",
    "What is photosynthesis?": "Photosynthesis is the process by which green plants use sunlight to synthesize food from carbon dioxide and water.",
    "Can you help me with my homework?": "I'll do my best! What do you need help with?",
    "What’s the largest planet in our solar system?": "Jupiter is the largest planet in our solar system.",
    "How do you spell [word]?": "You spell it [word].",
    "how do you spell [word]?": "You spell it [word].",
}
 
 
# Main chat loop 
while True: 
    message = input('You: ') 
    if message.lower() == 'bye': 
        print('Chatbot: Goodbye!') 
        break 
     
    # Check for predefined responses 
    response = predefined_qa.get(message, None) 
     
    if response: 
        print('Chatbot:', response) 
    else: 
        # Optionally use the generative model for fallback responses 
        if API_KEY: 
            response = chat.send_message(message) 
            print('Chatbot:', response.text) 
        else: 
            print("Chatbot: Sorry, I don't understand that")
            
            conversation_history = []

