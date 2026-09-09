"""
list methods
 add
     append(object)       appends object at end of the list
     insert(index,object) add object at specified index
    
 remove
     pop(index = -1) removes the element at specified index
     remove(value)  remove the frst occurence of value frm list

     index(value)  returns index position of frst occurence of value
     count(value)  return frequency of value
     reverse()     reverse the list in place
     sort(reverse = True) sort list in ascending order

"""
colors = ["red","green","blue","red","violet","purple"]
   #         0      1      2     3     4        5

# add white to colors

colors.append("white")
print(colors)

# insert color

colors.insert(2,"orange")
print(colors)

# pop

colors.pop(4)
print(colors)

# remove

colors.remove("red")
print(colors)

# index 

blue_index = colors.index("blue")
print(blue_index)

# count

count = colors.count("violet")
print(count)

# reverse

colors.reverse()
print(colors)

# sort

colors.sort()
print(colors)

# sort(reverse = True)

colors.sort(reverse = True)
print(colors)