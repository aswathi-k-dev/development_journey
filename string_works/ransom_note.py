note = "hen"
magazine = "chicken"
for char in note:
    if char  not in magazine:
        print("not a ransom_note")
        break
else:
    print("ransomnote")