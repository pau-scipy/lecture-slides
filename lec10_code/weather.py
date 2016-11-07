import random

def weather_message(temp, low, med):
   if temp < low:
      msg = "wear wool trousers"
   elif temp < med:
      msg = "wear trousers"
   else:
      msg = "wear shorts"
   return msg

def predict_tomorrow_temp(current_temp):
   change = random.choice(range(-1, 2))
   new_temp = current_temp + change
   return new_temp

temp = 10
for day in range(1, 8):
    print("Day " + str(day))
    print("Today's temp is:" + str(temp))
    temp = predict_tomorrow_temp(temp)
    print("Tomorrow will be:" + str(temp))

