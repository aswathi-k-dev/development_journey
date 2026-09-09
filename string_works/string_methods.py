""" isalpha()
    isdigit()
    isalnum()
    count(char) 
    find()
    rfind()
    index(char) 
    startswith(substr)
    endswith(substr)
    replace(old,new)
    strip(value) => remove value frm both end
    lstrip(value) => remove value frm beginning
    rstrip(value) => remove value frm end
    """

'''
password = "yadhukk@2002"

if password.isalpha():

    print("password is an alphabet")

elif password.isdigit():

    print("password is a digit")

elif password.isalnum():

    print("password is alphanumeric")

else:

    print("special character")

"""   count(char)  """

text = "helloworld"
l_count = text.count("o")
print(l_count)


""" find """

print(text.find("l"))

""" rfind """

print(text.rfind("o"))

"""  index(char)  """

print(text.index("l"))
print(text.index("w"))   

""" startswith(substr) """

word = "python"
print(word.startswith("py"))

""" endswith(substr) """

print(word.endswith("on"))

"""  replace(old,new)  """

text = "i hate python"
new_text = text.replace("hate","love")
print(new_text)   '''
                          

"""  strip(value) """

text = "@hellooo@"

print(text.strip("@"))

""" lstrip(value)  """

print(text.lstrip("@"))

"""   rstrip(value)   """

print(text.rstrip("@"))
                        
                        

