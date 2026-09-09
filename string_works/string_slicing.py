text = "A man,a plan,a canal panama"
     #  012345678901234567890123456

     # extract canal

substr = text[17:22]
print(substr)

#extract plan

substr2 = text[9:13]
print(substr2)

# extract panama

substr3 = text[23:]
print(substr3)

#extract a man

substr4 = text[:5]
print(substr4)

copy_str = text[:]
print(copy_str)