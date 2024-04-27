# Setup
**Requirements**
- Python 3.9+ (I used 3.9.19)
- Docker
- [WeatherAPI key](https://www.weatherapi.com/)
- 
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
# Integration
# Escalation to Human Assistance
# Understanding User Queries
# Improvements/ Unfinised Features
