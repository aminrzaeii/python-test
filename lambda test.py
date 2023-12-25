#amin rezaei
#Lambda test in Python

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

add = lambda x , y : x + y
print( add(4 , 6))

name = lambda firstName , lastName : firstName + lastName
firstName = input("first name : ")
lastName = input(" last name : ")
print(name(firstName , lastName))

team = lambda yearOfBirth , now : now - yearOfBirth 
now = int(input("What year is it now? : "))
yearOfBirth = int(input("What year were you born? : "))
print("Your age is equal to" , team(yearOfBirth ,  now))
