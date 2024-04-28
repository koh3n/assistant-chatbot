from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from rasa_sdk.events import SlotSet
import datetime
import pytz
import time  
from twilio.rest import Client
from dateutil import parser

class ClearTime(Action):
    def name(self) -> Text:
        return "action_clear_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Clear the slot named 'slot_name'
        return [
            SlotSet("timeslot", None)
            ]
    
class ClearREminder(Action):
    def name(self) -> Text:
        return "action_clear_reminder"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Clear the slot named 'slot_name'
        return [
            SlotSet("reminder", None)
            ]

# class ReminderAction(Action):
#     def name(self) -> Text:
#         return "action_reminder"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         load_dotenv()
#         account_sid = os.getenv("TWILIO_SID")
#         auth_token = os.getenv("TWILIO_TOKEN")
#         user_number = os.getenv("USER_PHONE_NUMBER")
#         twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
#         body =  'Reminder Set!'  #tracker.get_slot("reminder")
#         timeslot = tracker.get_slot("timeslot")

#         scheduled_time = parser.isoparse(timeslot)
#         scheduled_time_pst = scheduled_time.astimezone(pytz.timezone('America/Los_Angeles'))
#         current_time = datetime.datetime.now(pytz.utc)
#         delay = (scheduled_time_pst - current_time).total_seconds()

#         if delay < 0:
#             dispatcher.utter_message(text="Time has already passed.")
#             return

#         dispatcher.utter_message(text="Reminder scheduled to be sent at:" + scheduled_time_pst)
   
#         time.sleep(delay)

#         client = Client(account_sid, auth_token)

#         message = client.messages.create(
#             to = user_number,
#             from_= twilio_number,
#             body = body
#         )

#         dispatcher.utter_message(text="Reminder sent successfully!")

#         return [SlotSet("timeslot", None),
#                 SlotSet("reminder", None)]

class ReminderAction(Action):
    def name(self) -> Text:
        return "action_reminder"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Starting reminder action...")

        load_dotenv()
        account_sid = os.getenv("TWILIO_SID")
        auth_token = os.getenv("TWILIO_TOKEN")
        user_number = os.getenv("USER_PHONE_NUMBER")
        twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
        
        if not all([account_sid, auth_token, user_number, twilio_number]):
            dispatcher.utter_message(text="Missing Twilio configuration. Please check your environment variables.")
            return []

        body = tracker.get_slot("reminder")
        timeslot = tracker.get_slot("timeslot")

        if not timeslot:
            dispatcher.utter_message(text="No timeslot provided.")
            return []

        try:
            scheduled_time = parser.isoparse(timeslot)
        except ValueError:
            dispatcher.utter_message(text="Invalid timeslot format.")
            return []

        scheduled_time_pst = scheduled_time.astimezone(pytz.timezone('America/Los_Angeles'))
        current_time = datetime.datetime.now(pytz.utc)
        delay = (scheduled_time_pst - current_time).total_seconds()

        if delay < 0:
            dispatcher.utter_message(text="Time has already passed.")
            return []

        dispatcher.utter_message(text="Reminder scheduled to be sent at: " + str(scheduled_time_pst))

        time.sleep(delay)

        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(
                to=user_number,
                from_=twilio_number,
                body=body
            )
        except Exception as e:
            dispatcher.utter_message(text=f"Error sending reminder: {str(e)}")
            return []

        dispatcher.utter_message(text="Reminder sent successfully!")

        return [SlotSet("timeslot", None),
                SlotSet("reminder", None)]

    
# class ReminderTest(Action):
#     def name(self) -> Text:
#         return "action_reminder_test"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         load_dotenv()
#         account_sid = os.getenv("TWILIO_SID")
#         auth_token = os.getenv("TWILIO_TOKEN")
#         user_number = os.getenv("USER_PHONE_NUMBER")
#         twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
#         body = tracker.get_slot("reminder")


#         client = Client(account_sid, auth_token)

#         message = client.messages.create(
#             to = user_number,
#             from_= twilio_number,
#             body = body
#         )

#         return []