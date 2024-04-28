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

**2) Create .env file in root**

- use the env.txt boilerplate, located in root 

**3) Run action server in new terminal**

rasa run action

**4) Run Duckling server in new terminal**

docker run -p 8000:8000 rasa/duckling

**5) Train model and run Rasa server in new terminal**

rasa train
rasa shell

# Functionality
- **Schedule events**
  - The bot parses your message for the date, time and name of the event
  - It then creates an event and sends it to your email, allowing you to easily add to your Google Calendar or any other calendar application
- **Send emails**
  - The bot parses your message for the email address of the recipient
  - It then prompts you to enter a message body for the email and sends it after you have confirmed.
- **View real time weather information + 7 day forecast for all major cities**
  - The bot parses your message for the city and returns the 7 day forecast, with weather conditions and low/high temperatures
- **View the latest news articles on topics of your choice**
  - Once you have asked the bot information about the news, it asks you for a specific topic and returns recent articles relevant to your topic
  - The bot displays the article title as well as a link to the full article    
- **Set custom reminders (sends a SMS to your phone)**
  - The bot parses your message for the time and date of the reminder
  - After it has collected data on what the reminder is about, it waits until the specified time and sends a SMS message to your mobile phone reminding you of whatever you specified earlier

# Integration
- Events scheduled through the icalendar Python Library
- Emails sent via mtlplib Python Library
- Weather information from [WeatherAPI](https://www.weatherapi.com/)
- News from [NewsAPI](https://newsapi.org/)
- Reminder sent through SMS via [Twilio](https://www.twilio.com/en-us)
  - Custom async logic to handle delay in sending reminder notifications

# Escalation to Human Assistance
- This could be implemented as a fallback action when the bot's confidence in predicting a response falls below a certain threshold.
- Currently the fallback action is to not reply and listen again for the user's next input. This could be changed to send a message or email to a human assistant with the details of the conversation.
- However, from a functional standpoint this might not be the most useful feature as the user would most likely be able to do the task their self.
  
# Understanding User Queries
- The model is able to understand when the user wants to use one of the features
- The training data for these intents can be found in data/nlu/*
  
# Improvements
- Given more time I would have directly used Google's APIs for Gmail, Google Messages and Google Calendar to handle the email, reminders and scheduling, respectively. 
- All time related activites (scheduling/ setting reminders) are all hardcoded to Vancouver time (PDT). Adding in user settings where users can select their time zones would be beneficial.
- MORE TRAINING DATA!!! I made all the training data myself (with the help of chatGPT) so the model definitely isn't as perfect as it could be.
- The bot is unable to run while waiting for a reminder notification to be sent.

# Unfinised Features
- Unfortunately I didn't have enough time to finish all the requested functionality features. Here are the ones I missed.
1) **General knowledge**
  - There are a couple paths I could take with this but I think the best one would be integrating the bot with a LLM such as OpenAI. This avoids having to train the bot and deal with tons and tons of training data.
  - I think a smart way to implement this would be as a fallback action (since human assistance isn't that useful in this scenario as mentioned earlier)
    - Once the bot is unsure of how to reply, it sends the last seen message to the LLM for processing and returns the result.
      
2) *Managing to-do lists**
  - I would probably just integrate this with Google Tasks, since everything else is using Google services.
    
3) **Offering recommendations (e.g., restaurants)**
  - Restaurant recommendations would require user location so there would need to be permisions required there, dependant on how the chatbot is implemented.
  - After the location is gathered, I would use Google Maps API to search for relevant restaurants near the user.

# Evaluation
