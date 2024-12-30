# DICTIONARIES

# Creating the dictionari
d1={}
print(d1)
print(type(d1))

d2={1:"vedaant",2:"pradnya",3:"ambolkar",4:"samant"}
print(d2)

d3={"name":"vedaant","age":18,"city":"mumbai"}
print(d3)

d4=dict({"name":"vedaant","age":18,"city":"mumbai"})
print(d4)

d5={"name":{"first name":"vedaant","last name":"ambolkar"} ,"age":18,"city":"mumbai"}
print(d5)

#Adding elements
d={}
d[0]="vedaant"
print(d)

d[1]="pradnya"
print(d)

# Accessing the elements in dictionary
D={0:"vedaant",1:"ambolkar",2:"pradnya",3:"samant",4:{"last1":"ambolkar","last2":"samant"}}
print(D)
print(D[0])
print(D[4])

# Deleting elements in the dictionary
print(D)
D.pop(4)
print(D)

D.popitem()
print(D)

# Built in functions in dictionary
V={0:"vedaant",1:"ambolkar",2:"pradnya",3:"samant",4:{"last1":"ambolkar","last2":"samant"}}
print(V)
print(V.values())
print(V.keys())
V.clear()
print(V)

# Dictionary Methods

student={
    "name": "vedaant ambolkar",
    "subject and marks": {
        "phy":39,
        "chem":45,
        "maths":69,
}
}
print(student)
print(student.keys())                  #(1)=> returns all key
print(len(list(student.keys())))       # TYPE CAST INTO LIST
print(tuple(student.keys()))           # TYPE CAST INTO TUPLE

print(student.values())                #(2)=> returns all values
print(list(student.values()))          # TYPE CASTING INTO LIST
print(len(list(student.values())))

print(student.items())                #(3)=>  returns all (key, values) pairs as tuples
print(list(student.items()))
pairs=list(student.items())
print(pairs[1])

# print(student["name2"])        #Error
print(student.get("name2"))  # no error => None  {(4)=> accesing key value from the dictionary}

student.update({"city": "mumbai", "hobbe": "drawing"})      #(5)=> updating dictionart to form a new one 
print(student)



# SETS IN PYTHON
#  Creating a set
s=set([1,2,3,4])
print(s)
print(type(s))

s.add("v")
print(s)

''''fs=frozenset([1,2,3,4,5,6,7]) # Frozen set we can not add the element 
print(fs)
fs.add("f")
print(fs)'''

s1=set([1,5,6,7,2,4])
s2=set([5,4,6,4,3,9])
S=s1.union(s2)
print(S)

v=s1.difference(s2)
print(v)


#SETS IN PYTHONE => stes is the collection of the unorderd items, each element in the set must be unique and immutable.
collection_set={1,2,3,4,5,6,7,8,9, "hi", "heloooo"}
print(collection_set)
print(type(collection_set))
print(len(collection_set))
a=set() #empty set; syntax
print(type(a))


# SETS METHODS
coll=set()
coll.add(1)
coll.add(2)   #(1) ADD AN ELIMENT IN SET
coll.add(3)
coll.add(4)                        # SET IS AN MUTABLE FUNCTION
                                   # ELEMENT OF SET ARE IMMUTABLE => LIST CAN NOT BE ADDED 
coll.add("vedaant")                                               #=> TUPLS CAN BE ADDED 

coll.remove(1)  # (2) REMOVE AN ELEMENT IN SET 
print(coll)

coll.clear()  # (3) EMPTIES THE SET 
print(len(coll))

coll1={"vedaant", "ambolkar", 18, 3.14}
print(coll1.pop())  #(4) IT WILL REMOVE RANDOM VALUE FROM THE SET 

set1={1,2,3}
set2={7,8,9,3}          
print(set1.union(set2))  # (5) SET UNION METHODE
print(set1.intersection(set2)) # (6) SET INTERSECTION METHODE 