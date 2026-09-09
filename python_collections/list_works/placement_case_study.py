# feb month placement count

placement_count = [10,15,22,9,17,18]
feb_month_placemnt_count = placement_count[1]
print(feb_month_placemnt_count)

# jan month update

placement_count[0] = 12
print(placement_count)

# count > 15

for count in placement_count:
    if count > 15:
        print(count)

# highest placement count without max()

max_count = placement_count[0]
for count in placement_count:
    if count > max_count:
        max_count = count
print("highest placement count = ",max_count)

# lowest placement count without min()

min_count = placement_count[0]
for count in placement_count:
    if count < min_count:
        min_count = count
print("lowest placement count = ",min_count)

# second highest placement count

first_max,second_max = 0,0
for count in placement_count:
    if count >first_max:
        second_max = first_max
        first_max = count
    elif count > second_max:
        second_max = count
print(second_max)
    
