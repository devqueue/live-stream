# conditionals

A = 5
B = 5

if A>B:
    print("a is greater")

elif A==B:
    print("a is equal to b") 

else:
    print("b is greater")


# Loops

# for loop 

for i in range(10+1):
    print(i)


# range(start,stop, step)

# While loop

i = 0
while i<11:
    print(i)
    i+=1    

# break and continue

i = 0

while i<10:
    print(i)
    i+=1
    if i==8:
        break




# strings
'''
traverse
operations
manupilation
function/ methods
'''
A = "World"
B = "hello"
# for ch in A:
#     print(ch, "~", end="")


print(B+A) # concatination
print(A*4) 
print("h" in B)

# functions

A.isalpha()
A.isdigit()
A.isupper()
A.islower()
A.isalnum()
A.isspace()

A.capitalize() # capitalize the first letter in the str
A.lower() 
A.upper()

A.rstrip()
A.lstrip()


# Lists 
LIST = [1,2,3,4,56]
LIST2 = [1,2,3,4,55]
print(LIST+LIST2)  # concatination
print(LIST*4)
# [start:stop:step]

print(LIST[-1:1:-1])

# functions on a list 
#  Add values in a list
LIST.append(90)
LIST.insert(0, 91)
print(LIST)

# remove
LIST.pop(0)
print(LIST)

LIST.remove(56)
print(LIST)

# Tupple

T = (1,2,3,1,5)

print(T.count(1))

# dictionary

D = {
    "name":"haziq",
    "age":16,
    "email":"abs@gmail.com"
}

D["key"] = "value"

D.pop("age")

print(D)

print("haziq" in D.values())

print(len(D))