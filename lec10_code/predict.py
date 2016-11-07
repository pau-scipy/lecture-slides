import weather 

today = 10
tomorrow = weather.predict_tomorrow_temp(today)
print("Tomorrow will be:" + str(tomorrow))
msg = weather.weather_message(tomorrow, 5, 15)
print(msg)
