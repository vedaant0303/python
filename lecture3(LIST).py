# LIST => List is a colection of elements which can be of different data type

# Creating a List
num=[1,2,3,4,5]
print(num)

letter=["a","b","c","d"]
print(letter)

mix=[1,2,"get","simpler","python",11,3]
print(mix)

matrix=[[1,2,3],[4,5,5]]
print(matrix)

# Accessing the elements of a list
print(mix)
print(mix[3])
print(mix[-2])
print(mix[0:4])
print(mix[:3])
print(mix[::4])
print(mix[::-1])

# Operations on list
z=[0]*100
print(z)

print(letter)
print(mix)
con=letter+mix
print(con)

x=list("veDAnt & pradnya")
print(x)

# Methods in list
print(num)
#num.append(11)
#print(num)
print(letter)
num.extend(letter)
num.insert(0,"hello")
print(num)
val=[1000,11,7,10,44]
val.sort()
print(val)

# Built in functions in list
y=[9,17,14,4,90,55]
print(len(y))
print(max(y))
print(min(y))
print(sum(y))
print(sum(y)/len(y))

