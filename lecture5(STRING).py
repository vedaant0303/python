# STRING
#  Accessing the elements in String
var="vedaant"
print(var)

#Functions of String
stg="simpler"
print(len(stg))
print(stg[5])

# Methods in String
#1 UPPERCASE
v="vedaant and pradnya"
print(v.upper())
#2 LOWERCASE
print(v.lower())
#3 FIND
print(v.find("p"))
#4 INDEX
print(v.index("p"))
#5 SPLIT
print(v.split())
#6 REPLACE
print(v.replace("vedaant","samant"))
#7 RPARTITION
print(v.rpartition("and"))

# CONCATICATION
stg1="good"
stg2="morning"
stg= stg1+" "+stg2
print(stg)

s1="hey"
s2="there"
s3="all"
s="{},{},{}!!".format(s1,s2,s3)
print(s)

