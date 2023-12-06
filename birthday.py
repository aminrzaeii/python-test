#amin rezaei
print("I have a list of my friends along with their birthdays that I can tell you any one you want")
list = ["ali" , "amir" , "reza" , "amin" , "ramin"]
print(list)
BD = {
      "ali" : "july" ,
      "amir" : "may" ,
      "reza" : "August" ,
      "amin" : "September" ,
      "ramin" : "December"
}
a = str(input("Which birthday do you want? : "))
if a == "ali" :
 print("ali's birthday is " , BD["ali"])
elif a == "amir" :
 print("amir's birthday is" , BD["amir"])
elif a == "reza" :
 print("reza's birthday is" , BD["reza"])
elif a == "amin" :
 print("amin's birthday is " , BD["amin"])
else :
 print("ramin's birthday is" , BD["ramin"])
