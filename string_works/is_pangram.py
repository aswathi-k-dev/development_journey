def is_pangram(text):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabets:
        if char not in text.lower():
            print("FALSE")
            break
    else:
        print("TRUE")
is_pangram("the quick brown fox jumps over lAzy dog")