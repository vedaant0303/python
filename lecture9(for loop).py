#FOR LOOP => For lop is used to iterate over a sequence which could be a list ,tuple ,arry or string
'''x=[1,4.5,"vedaant"]
print(x[0],x[1],x[2])'''
# by using for loop
'''x=[1,4.5,"vedaant"]
for i in x :

    print(i , end='')
print()'''

#print even number from 1 to 20
# 1 mathode
'''for i in range(1,21,2):
    print(i)'''
#2 mathode
'''for i in range(1,21):
    if i%2==0:
        print(i)'''
#print sum of even number from 1 to 20
'''sum=0
for i in range(0,21):
    if i%2==0:
        sum=sum+i
        print(sum)'''

# print the paterns
'''1
   12
   123
   1234
   12345
n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1, i + 1):
        print(j, end="")
    print()'''

# print patern
'''*
   **
   ***
   ****
n=int(input("enter the number of stars"))
for i in range(1, n+1):
    for j in range( i ):
        print("*", end="")
    print()'''

#print patern 
'''*
  ***
 *****
*******'''
n=int(input("enter the number"))
for i in range(1, n+1):
       print(" "*(n-1)+ "*"*i)
print()

# Number of rows
'''n = 4

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)'''
