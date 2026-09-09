attendance = ["p","p","a","a","o","o","h"]
attendance_set = set(attendance)
attendance_count = {}
for ch in attendance:
    attendance_count[ch] = attendance.count(ch)
print(attendance_count)