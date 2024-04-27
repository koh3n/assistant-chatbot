# Setup
**Requirements**
- Python 3.9+ (I used 3.9.19)
- Docker
- [WeatherAPI key](https://www.weatherapi.com/)
  
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
- View real time weather information + 7 day forecase for all major cities

# Integration
- Weather information from [WeatherAPI](https://www.weatherapi.com/)

# Escalation to Human Assistance
- This could be implemented as a fallback action when the bot's confidence in predicting a response falls below a certain threshold
- Currently the fallback action is to not reply and listen again for the user's next input. This could be changed to send a message or email to a human assistant with the details of the conversation.
- However, from a functional standpoint this might not be the most useful feature as the user would most likely be able to do the task their self.
  
# Understanding User Queries
- The model is able to understand when the user wants to use one of the features
- The training data for these intents can be found in data/nlu/*
  
# Improvements/ Unfinised Features
