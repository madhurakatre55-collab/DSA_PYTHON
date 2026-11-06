# operations on a arrays 

# 1.inseration 
#2.deletion
#3.searching
from collections.abc import MutableSequence
from array import array as _array


val = _array('i', [1, 2, 3, 4, 5])
print(val.typecode)
print(len(val))
print(val.itemsize)

val.reverse() # reverse array
val.insert(2,10) # 2-index,10-valve insert at a index do not delete element
print(val)
val.append(6)  # at the end adds element 6 valve
print(val)

val[2] =100 # update element at index 2
print(val)

val.pop(3) # deltes from exact index 3-index
print(val)

val.remove(100) # removes the first occurrence of value 100
print(val)


