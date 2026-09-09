""" 
tuple
define : tp = (10,20)
mutable : no
duplicates : yes
ordered : yes
methods : count(value),index(value)

"""

tp = (10,20,30,30)
print(type(tp))

print(tp)

# count
print(tp.count(30))
# index
print(tp.index(20))

tp = (10, )
print(type(tp))