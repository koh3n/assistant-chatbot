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

# custom_actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from dotenv import load_dotenv
import os
import requests

class ClearSlotAction(Action):
    def name(self) -> Text:
        return "action_clear_email"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Clear the slot named 'slot_name'
        return [
            SlotSet("email", None),
            SlotSet("body", None)
            ]
    
class ClearBody(Action):
    def name(self) -> Text:
        return "action_clear_body"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Clear the slot named 'slot_name'
        return [
            SlotSet("body", None)
            ]


class WeatherAction(Action):
    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Make an HTTP GET request
        api_key = os.getenv("WEATHER_API_KEY")
        city = tracker.get_slot("city")
        response = requests.get("http://api.weatherapi.com/v1/forecast.json?key=" + api_key + "&q=" + city + "&days=8&aqi=no&alerts=no")

        # handle response
        if response.status_code == 200:
            data = response.json()  

            forecast = "Sure! Here is the 7 day forecast for " + city

            # parsing through the json to get relevant data
            forecast0 = ("Today, on " + 
            data['forecast']['forecastday'][0]['date'] + 
            ", the weather in " + 
            city + 
            " is " +
            data['forecast']['forecastday'][0]['day']['condition']['text'] + 
            " with a high of " +
            str(data['forecast']['forecastday'][0]['day']['maxtemp_c']) + 'C' +
            ' and a low of ' +
            str(data['forecast']['forecastday'][0]['day']['mintemp_c']) + 'C')

            forecast1= ("On " + 
            data['forecast']['forecastday'][1]['date'] + 
            ", the weather in " + 
            city + 
            " is " +
            data['forecast']['forecastday'][1]['day']['condition']['text'] + 
            " with a high of " +
            str(data['forecast']['forecastday'][1]['day']['maxtemp_c']) + 'C' +
            ' and a low of ' +
            str(data['forecast']['forecastday'][1]['day']['mintemp_c']) + 'C')

            forecast2= ("On " + 
            data['forecast']['forecastday'][2]['date'] + 
            ", the weather in " + 
            city + 
            " is " +
            data['forecast']['forecastday'][2]['day']['condition']['text'] + 
            " with a high of " +
            str(data['forecast']['forecastday'][2]['day']['maxtemp_c']) + 'C' +
            ' and a low of ' +
            str(data['forecast']['forecastday'][2]['day']['mintemp_c']) + 'C')

            forecast3 = ("On " + 
            data['forecast']['forecastday'][3]['date'] + 
            ", the weather in " + 
            city + 
            " is " +
            data['forecast']['forecastday'][3]['day']['condition']['text'] + 
            " with a high of " +
            str(data['forecast']['forecastday'][3]['day']['maxtemp_c']) + 'C' +
            ' and a low of ' +
            str(data['forecast']['forecastday'][3]['day']['mintemp_c']) + 'C')

            forecast4= ("On " + 
            data['forecast']['forecastday'][4]['date'] + 
            ", the weather in " + 
            city + 
            " is " +
            data['forecast']['forecastday'][4]['day']['condition']['text'] + 
            " with a high of " +
            str(data['forecast']['forecastday'][4]['day']['maxtemp_c']) + 'C' +
            ' and a low of ' +
            str(data['forecast']['forecastday'][4]['day']['mintemp_c']) + 'C')

            forecast5 =("On " + 
            data['forecast']['forecastday'][5]['date'] + 
            ", the weather in " + 
            city + 
            " is " +
            data['forecast']['forecastday'][5]['day']['condition']['text'] + 
            " with a high of " +
            str(data['forecast']['forecastday'][5]['day']['maxtemp_c']) + 'C' +
            ' and a low of ' +
            str(data['forecast']['forecastday'][5]['day']['mintemp_c']) + 'C')

            forecast6 = ("On " + 
            data['forecast']['forecastday'][6]['date'] + 
            ", the weather in " + 
            city + 
            " is " +
            data['forecast']['forecastday'][6]['day']['condition']['text'] + 
            " with a high of " +
            str(data['forecast']['forecastday'][6]['day']['maxtemp_c']) + 'C' +
            ' and a low of ' +
            str(data['forecast']['forecastday'][6]['day']['mintemp_c']) + 'C')

            forecast7 = ("On " + 
            data['forecast']['forecastday'][7]['date'] + 
            ", the weather in " + 
            city + 
            " is " +
            data['forecast']['forecastday'][7]['day']['condition']['text'] + 
            " with a high of " +
            str(data['forecast']['forecastday'][7]['day']['maxtemp_c']) + 'C' +
            ' and a low of ' +
            str(data['forecast']['forecastday'][7]['day']['mintemp_c']) + 'C')




            dispatcher.utter_message(text=forecast)
            dispatcher.utter_message(text=forecast0)
            dispatcher.utter_message(text=forecast1)
            dispatcher.utter_message(text=forecast2)
            dispatcher.utter_message(text=forecast3)
            dispatcher.utter_message(text=forecast4)
            dispatcher.utter_message(text=forecast5)
            dispatcher.utter_message(text=forecast6)
            dispatcher.utter_message(text=forecast7)
        else:
            dispatcher.utter_message(text="Failed to fetch data from the API")

        return []
