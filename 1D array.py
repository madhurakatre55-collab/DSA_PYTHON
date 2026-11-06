from array import array as _array
import array
#1 D array
x = int(input("enter u need 1d(1) or 2d(2) array:"))
if x == 1:
val =[1,2,3,4,5]

print("Original array",val)

#insertion
print("performing insertion")
val.insert( 1,20)
print("Array after insertion ",val)
val.append(60)
print("After after append",val)
val[3] = 30
print("Array after insertion",val)


#delection
val.pop(4)
print("Array after delection/pop",val)

val.remove(60)
print("removed element 60",val)

#searching
i =int(input("enter element to secarsh in array:"))
if i in val:
    print("element found")
else:
    print("element not found")
else:   
#2 D array3

val2 = [[1,2,3],[4,5,6],[7,8,9]]
print("original 2d array:",val2)

#insertion
val2[0][1] = 20

print("after insertion",val2)

#delection
val2.pop(2)
#full row deledted
print("after pop 2 d",val2)

del val2[1][1] #deletes 5 from 2d array
print("after delection",val2)

#seacrhingl̥
n = int(input("enter the value to seacrh"))
for row in val2:
    if n in row:
        print("element found")
        break
else:
    print("not found")