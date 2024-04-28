from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from icalendar import Calendar, Event
from datetime import datetime, timedelta

class CreateEvent(Action):
    def name(self) -> Text:
        return "action_create_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        summary = tracker.get_slot("eventname")
        time = tracker.get_slot("timeslot")
        cal = Calendar()
        event = Event()
        start_time = datetime.fromisoformat(time)
        event.add('summary', summary)
        event.add('dtstart', start_time)

        # Set end time to one hour after the start time (default thing)
        end_time = start_time + timedelta(hours=1)
        event.add('dtend', end_time)
        
        cal.add_component(event)
        
        with open('event.ics', 'wb') as f:
            f.write(cal.to_ical())

        return []


class SendEvent(Action):
    def name(self) -> Text:
        return "action_send_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        subject = "Add event"
        load_dotenv()
        sender = os.getenv('USER_EMAIL_ADDRESS')
        password = os.getenv('USER_EMAIL_PASSWORD')
        body = " "

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = sender

        # Attach body
        msg.attach(MIMEText(body, 'plain'))

        # Attach file
        filename = "event.ics"  
        attachment = open(filename, "rb")

        # Create a MIMEBase object
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

        # Encode the attachment and add headers
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")

        # Add attachment to message
        msg.attach(part)

        # Connect to SMTP server and send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, sender, msg.as_string())

        dispatcher.utter_message(text= "Check your email for the event link!")

        return [
            ]