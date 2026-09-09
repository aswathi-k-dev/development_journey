"""
set : st = {10,20}
define :{value,value},set()
ordered : unordered, indexing not supported
mutable : yes
duplicates : no
methods :
         add(value) : add value to set
         union(set)  
         intersection(set) 
         difference(set)   
         is_superset(set)
         is_subset(set)



"""
st = {10,20,30,30,40}
print(type(st))

st.add(100)
print(st)

set_1 = {10,20,30,40}
set_2 = {10,20,100,200,300}

# union set
union_set = set_1.union(set_2)
print("union set =",union_set)

# intersection set
intersection_set = set_1.intersection(set_2)
print("intersection set =",intersection_set)

# difference set
difference_set = set_1.difference(set_2)
print("difference set =",difference_set)

# super set and subset

set_a = {10,20,30,40,50}
set_b = {10,20,30}

print(set_a.issuperset(set_b))
print(set_b.issubset(set_a))




