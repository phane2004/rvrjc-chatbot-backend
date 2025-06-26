import json
import random

def get_response(user_input):
    user_input = user_input.lower().strip()

    with open("intents.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    fallback_responses = []

    for intent in data["intents"]:
        if intent["tag"] == "fallback":
            fallback_responses = intent["responses"]
            continue

        for pattern in intent["patterns"]:
            if pattern.lower() in user_input or user_input in pattern.lower():
                return random.choice(intent["responses"])

    if fallback_responses:
        return random.choice(fallback_responses)
    else:
        return "Sorry, I didn't understand that. Please ask something else."
