text = "england won by 6 wickets with 3 balls remaining.england leads the series with 2-1"

alpha_count = 0
digit_count = 0
special_character = 0

for ch in text:
    if ch.isalpha():
        alpha_count = alpha_count + 1
    elif ch.isdigit():
        digit_count = digit_count + 1
    else:
        special_character = special_character + 1
print("alphacount = ",alpha_count)
print("digitcount = ",digit_count)
print("specialcharacter = ",special_character)

