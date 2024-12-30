# WHILE LOOP
val=int(input("Enter the multiple of 7"))
while val%7!=0:
    val=int(input("Enter the multiple of 7"))
    print(val,end="")
    print()
else:
    print("%d is multipal of 7"%val)

count=1
while count<=5:
     print("hellow", count)
     count += 1
print(count)

#print number from 1 to 5 and 5 to 1
i=1
while i <= 5:
     print(i)
     i+=1
j=5
while j>=1:
     print(j)
     j-=1


# Break => used to terminate the loop when encounter 
# Continue => terminates execution in the current iteration and continues execution of the loop with the next iteration 
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")

i=0
while i<=10:
     if(i%2 !=0):
          i+=1
          continue # sikip
     print(i)
     i+=1

#FOR LOOP
x="Hey there . how are you?"
for i in x:
    if i==".":
        break
    print(i)
    print(i,end="")

y=[1,13,56,4,6]
for i in y:
    if i>10:
        continue
    print(i)