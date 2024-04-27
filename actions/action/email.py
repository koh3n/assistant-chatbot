from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from dotenv import load_dotenv
import os
import requests

#clears both the email and body slot after the email is sent
class ClearSlotAction(Action):
    def name(self) -> Text:
        return "action_clear_email"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Clear the slot named 'slot_name'
        return [
            SlotSet("email", None),
            SlotSet("body", None)
            ]

#clears the body slot before the user inputs the body of the email    
class ClearBody(Action):
    def name(self) -> Text:
        return "action_clear_body"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Clear the slot named 'slot_name'
        return [
            SlotSet("body", None)
            ]