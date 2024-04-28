from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from dotenv import load_dotenv
import os
import requests
import smtplib
from email.mime.text import MIMEText
from gensim.summarization import summarize

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
    
class SendEmail(Action):
    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        subject = " "
        body = tracker.get_slot("secondary")
        recipient = tracker.get_slot("email") 
        load_dotenv()
        sender = os.getenv('USER_EMAIL_ADDRESS')
        password = os.getenv('USER_EMAIL_PASSWORD')

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipient, msg.as_string())


        return [
            ]
    
class SaveSecondary(Action):
    def name(self) -> Text:
        return "action_save_secondary"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Clear the slot named 'slot_name'
        temp = tracker.get_slot("body")
        return [
            SlotSet("secondary", temp),
            ]