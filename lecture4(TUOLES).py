# TUPLES => Tuples are collections of immutable heterogenous python objects
# Creating a tuple

emp=()
print(type(emp))
print(emp)

num=(1,2,3,4,5)
print(num)

city=("mumbai","pune","banglore","delhi")
print(city)

# Accessing the elements in tuple 
print(city)
print(city[1])
print(city[-1])
#CONCATENATION
print(city)
print(num)
print(city+num)
#NESTING
nest=(city,num)
print(nest)
#REPETATION
rep=("pradnya", )*100
print(rep)
#SLICING
print(num)
print(num[1:])
print(num[::-1])
#UNPACKING
a=tuple("veDANt & pradnya")
print(a)

# Built in fuctions in tuple
num1=(3,5,2,2,2,6,5,8,9,19)
print(num1)
print(num1.count(2))
print(sum(num1))
print(max(num1))
print(min(num1))

# NESTING TUPLES IN A LIST
lis=[(1,2,3),(4,5,6),(7,8,9)]
print(lis)


