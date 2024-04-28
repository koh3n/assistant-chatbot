from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta
from rasa_sdk.events import SlotSet

# fetches the recent news on topic
class ClearTopic(Action):
    def name(self) -> Text:
        return "action_clear_topic"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Clear the slot named 'slot_name'
        return [
            SlotSet("topic", None)
            ]
    
class NewsAction(Action):
    def name(self) -> Text:
        return "action_news"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Make an HTTP GET request
        load_dotenv()
        api_key = os.getenv("NEWS_API_KEY")
        topic = tracker.get_slot("topic")

        current_date = datetime.now()
        yesterday_date = current_date - timedelta(days=1)
        response = requests.get("https://newsapi.org/v2/everything?q=" + topic + "&from=" + str(yesterday_date) + "&sortBy=relevancy&pagesize = 1&apiKey=" + api_key)

        # handle response
        if response.status_code == 200:
            data = response.json()  
            newstext = "Sure! Here is the recent news on " + topic + ':\n'
            article0 = 'Title: ' + data['articles'][0]['title'] + '\n' + 'Read more at: ' + data['articles'][0]['url'] + '\n'
            article1 = 'Title: ' + data['articles'][1]['title'] + '\n' + 'Read more at: ' + data['articles'][1]['url'] + '\n'
            article2 = 'Title: ' + data['articles'][2]['title'] + '\n' + 'Read more at: ' + data['articles'][2]['url']+ '\n'


            dispatcher.utter_message(text=newstext)
            dispatcher.utter_message(text=' \n')
            dispatcher.utter_message(text=article0)
            dispatcher.utter_message(text=' \n')
            dispatcher.utter_message(text=article1)
            dispatcher.utter_message(text=' \n')
            dispatcher.utter_message(text=article2)

        else:
            dispatcher.utter_message(text="Failed to fetch data from the API")

        return []
    