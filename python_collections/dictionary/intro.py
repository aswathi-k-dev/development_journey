"""
dictionary : {key:value}
define     : {"name":"lenovo12","brand":"lenovo","price":"70000"}
mutable    : Yes
ordered    : Yes
duplicates : duplicate key not allowed
methods    : keys()
             values()
             items()
             get(key)

"""
daily_calories = {"mon":1200,"tue":1500,
                  "wed":1400,"thur":2100,
                  "fri":1600,"sat":2300,
                  "sun":1680}

sat_consumed_calories = daily_calories["sat"]
print(sat_consumed_calories)

daily_calories["fri"] = 1700
print(daily_calories)

daily_calories["wed"]= 1200
print(daily_calories)

all_keys = daily_calories.keys()
print(all_keys)

for k in daily_calories.keys():
    print(k)

all_values = daily_calories.values()
print(all_values)

for v in daily_calories.values():
    print(v)

print("keys and values")

for k,v in daily_calories.items():
    print(k,v)

tue_calorie = daily_calories.get("tue")
print(tue_calorie)  

total_calorie = daily_calories.get("total")
print(total_calorie)  

daily_calories["total_calories"] = sum(daily_calories.values())
print(daily_calories)

total_cal = 0
for v in daily_calories.values():
    total_cal += v
print(total_cal)
daily_calories["total_calories"] = total_cal
print(daily_calories)