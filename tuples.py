"""
Tuples: immutable List
tuple cannot be changed in any way once it has been created
"""

emptyTuple = ()
t = (1,2,3,4,56.7,34.6)

print("Tuple : ",t)
print("Tuple type() : ",type(t)) #return lowest index of that object
print("Tuple length : ",len(t)) #return lowest index of that object
print("Tuple[0] : ",t[0]) #return lowest index of that object
print("Tuple[5] : ",t[5]) #return lowest index of that object

#del(t)

#try assigning
t[0]=100 
print(t) #Error: 'tuple' object does not support item assignment
quit()