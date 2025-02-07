# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import requests
from typing import Any, Text, Dict, List

# Action 1: Confirm Payment (χωρίς API)
class ActionConfirmPayment(Action):
    def name(self):
        return "action_confirm_payment"

    def run(self, dispatcher, tracker, domain):
        message = "✅ Your payment has been processed successfully! Enjoy your coffee. ☕"
        dispatcher.utter_message(text=message)
        return []

# Action 2: Suggest Coffee Based on Weather (API OpenWeatherMap)

class ActionSuggestCoffeeBasedOnWeather(Action):
    def name(self) -> Text:
        return "action_suggest_coffee_based_on_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_key = "f3d4eba9b4969077383320d1fd4e2d91"  # Σωστό API Key
        city = "Athens"

        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": "metric"}

        try:
            response = requests.get(url, params=params)
            print(f"Status code: {response.status_code}")  # Εμφάνιση του status code
            response.raise_for_status()
            weather_data = response.json()
            print(weather_data)  # Εμφάνιση της απάντησης API

            if "main" not in weather_data:
                dispatcher.utter_message(text=f"Could not find weather data for {city}.")
                return []

            temperature = weather_data["main"]["temp"]

            if temperature < 15:
                message = f"🌡️ The temperature in {city} is {temperature}°C. I recommend a hot coffee like Espresso or Cappuccino! ☕"
            else:
                message = f"🌞 The temperature in {city} is {temperature}°C. How about an iced coffee like Freddo Espresso or Cold Brew? 🧊☕"

        except requests.exceptions.RequestException as e:
            message = f"⚠ I couldn't fetch the weather data. Error: {str(e)}"

        dispatcher.utter_message(text=message)
        return []

 #api spoonacular-- recipe

import requests
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

class ActionSuggestCoffeeRecipes(Action):
    def name(self):
        return "action_suggest_coffee_recipes"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        api_key = "8addf37a74b9438fbd2c269c76402436"
        query = "coffee"
        url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number=3&apiKey={api_key}"

        try:
            response = requests.get(url)
            data = response.json()

            if data.get("results"):
                recipes = [recipe["title"] for recipe in data["results"]]
                message = f"Here are some popular coffee recipes: {', '.join(recipes)}."
            else:
                message = "I couldn't find any coffee recipes at the moment."

        except Exception as e:
            message = f"An error occurred: {e}"

        dispatcher.utter_message(text=message)
        return []


