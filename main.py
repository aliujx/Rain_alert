import requests
from twilio.rest import Client

api_key = "b81cecf54e9b4a6d795c67569b2fbf47"

account_sid = 'ACc122e21170c90bce6b70249ec57b1c3b'
auth_token = 'f2f1cbc266bfc7653c8872819d6e50e7'

parameters = {
    "lat": 36.917301,
    "lon": 31.102301,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

weather_code = []
responce = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
responce.raise_for_status()
weather_data = responce.json()
weather_condition = weather_data["hourly"]

will_rain = False

for hour in weather_condition[:13]:
    if hour["weather"][0]["id"] < 600:
        will_rain = True
        weather_code.append(hour["weather"][0]["id"])
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Today's a rainy weather!\nTake an umbrella!",
        from_='+19793644765',
        to='+905515945600'
    )

    print(message.sid)