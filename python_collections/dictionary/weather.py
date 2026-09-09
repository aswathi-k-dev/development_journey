# store last one week weather

weather = {"mon":25.6,"tue":34.7,
           "wed":35.6,"thur":29,
           "fri":35,"sat":45,
           "sun":26}

#display tue weather
tue_weather = weather["tue"]
print(tue_weather)

#update
weather["sat"] = 29
print(weather)

all_keys = weather.keys()
print(all_keys)

for k in weather.keys():
    print(k)

for v in weather.values():
    print(v)