def is_palindrome(word):
    result = word[::-1]
    return result

is_palindrome("tan")

assert is_palindrome("dad")== True,"testcase 1 failed"
assert is_palindrome("tan") == False,"testcase 2 failed"
assert is_palindrome("malayalam")== True,"testcase 3 failed"