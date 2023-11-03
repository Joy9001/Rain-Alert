import os
import requests
from twilio.rest import Client

# Create your own api key from weatherapi.com
api_key = os.environ.get("API_KEY")

# Create your own sid and token from twilio.com
sid = os.environ.get("SID")
token = os.environ.get("TOKEN")
FROM_PHN = '++19369096017'
TO_PHN = '+910000000000'  # Write your own phone number with country code

API_ENDPOINT = "http://api.weatherapi.com/v1/forecast.json"
parameters = {
    "key": api_key,
    "q": (15.912900, 79.739990)
}

need_umbrella = False

data = requests.get(url=API_ENDPOINT, params=parameters)
data.raise_for_status()
weather_info = data.json()
weather_slice = weather_info["forecast"]["forecastday"][0]["hour"][:12]

for info in weather_slice:
    if info["will_it_rain"] == 1 or info["will_it_snow"] == 1:
        need_umbrella = True

if need_umbrella:
    client = Client(sid, token)
    message = client.messages.create(body="It may rain today. Bring an Umbrella ☔.", from_=FROM_PHN, to=TO_PHN)

    print(message.status)
