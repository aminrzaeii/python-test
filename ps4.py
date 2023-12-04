#amin rezaei
print("Hello, I have a younger brother, his name is Ramin, he loves his toys, and I want to introduce them to you.")
toys = ["car" , "animals" , "Gun" , "Chess"]
print(toys[0])
print(toys[1])
print(toys[-2])
print(toys[-1])
numberOfToys = len(toys)
print(f"ramin has a {numberOfToys} toys")
print("I want to buy ps4 for him, there is a condition that his grade point average must be above 18")
a = int(input("plz enter Score1 : "))
b = int(input("plz enter score2 : "))
c = int(input("plz enter score 3 : "))
d = int(input("plz enter score 4 : "))
e = (a+b+c+d) / 4
if e >= 18 :
   toys.append("ps4")
   print
elif e < 18 :
 print("Your grades are lower than expected. I can't buy you ps4 sorry")
