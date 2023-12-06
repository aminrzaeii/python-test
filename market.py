#amin rezaei
#welcom to super market
print("hello to every body welcom to our super market Here are some of your usable foods for sale that you can choose and then buy")
list = ["milk" , "suger" , "oil" , "water" , "meat" , "chiken" , "sauce" , "coffee" , "rice" , "braed"]
print(list)
Price = {
     "milk" : 1000 ,
    "suger" : 2000 ,
    "oil" : "Not available" ,
    "water" : 5000 ,
    "meat" : 6000 ,
    "chiken" : "Not available" ,
    "sauce" : 8000 ,
    "coffee" : 9000 ,
    "rice" : 10000 ,
    "bread" : "Not available" 
}
a = str(input("Choose your required food : "))
if a == "milk" :
 print("the price of milk is" , Price["milk"])
elif a == "suger" :
 print("the price of milk is" , Price["suger"])
elif a == "oil" :
 print("sorry" , Price["oil"])
elif a == "water" :
 print("the price of water is" , Price["water"])
elif a == "meat" :
 print("the price of meat is" , Price["meat"])
elif a == "chiken" :
 print("sorry" , Price["chiken"])
elif a == "sauce" :
 print("the price of sauce is" , Price["sauce"])
elif a == "coffee" :
    print("the price of coffee is" , Price["coffee"])
elif a == "rice" :
    print("the price of rice is" , Price["rice"])
else :
 print("sorry" , Price["bread"])
