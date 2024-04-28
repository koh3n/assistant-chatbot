# Setup
**Requirements**
- [Python 3.9+](https://www.python.org/downloads/) (I used 3.9.19)
- [Docker](https://www.docker.com/)
- [WeatherAPI key](https://www.weatherapi.com/)
- [NewsAPI key](https://newsapi.org/)
- [TwilioAPI Token and SID](https://www.twilio.com/en-us)
- [Gmail Account with generated app password](https://myaccount.google.com/u/1/apppasswords)
  
**1) Install dependencies**

pip install -r requirements.txt

**2) Run action server in new terminal**

rasa run action

**3) Run Duckling server in new terminal**

docker run -p 8000:8000 rasa/duckling

**4) Train model and run Rasa server in new terminal**

rasa train
rasa shell

# Functionality
- Schedule events
- Send emails
- View real time weather information + 7 day forecast for all major cities
- View the latest news articles on topics of your choice
- Set custom reminders (sends a SMS to your phone)

# Integration
- Weather information from [WeatherAPI](https://www.weatherapi.com/)
- News from [NewsAPI](https://newsapi.org/)
- Reminder sent through SMS via [Twilio](https://www.twilio.com/en-us)
  - Custom async logic to handle delay in sending reminder notifications

# Escalation to Human Assistance
- This could be implemented as a fallback action when the bot's confidence in predicting a response falls below a certain threshold
- Currently the fallback action is to not reply and listen again for the user's next input. This could be changed to send a message or email to a human assistant with the details of the conversation.
- However, from a functional standpoint this might not be the most useful feature as the user would most likely be able to do the task their self.
  
# Understanding User Queries
- The model is able to understand when the user wants to use one of the features
- The training data for these intents can be found in data/nlu/*
  
# Improvements/ Unfinised Features
- All time related activites (scheduling/ setting reminders) are all hardcoded to Vancouver time (PDT). Adding in user settings where users can select their time zones would be beneficial.
- MORE TRAINING DATA!!! I made all the training data myself (with the help of chatGPT) so the model definitely isn't as perfect as it could be.

# Evaluation
