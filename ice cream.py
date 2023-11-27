#amin rezaei
#ice cream shop
print("Welcome to our ice cream shop. Here we have six types of ice cream to choose")
print("Our ice creams are in varieties (chocolate, strawberries, special, coffee, sour, and fruit) that you can choose.")
a = ("The price of chocolate 1$")
b = ("The price of strawberries 2$")
c = ("The price of special 3$")
d = ("The price of coffee ice cream 4$")
e = ("The price of ice sour cream 5$")
f = ("The price of fruit ice cream 6$")
buyer1 = str(input("Which type do you want? : "))
buyer2 = str(input("which type do you want? : "))
if buyer1 == "chocolate" and buyer2 == "special" :
 print(f"{a} and {b}")
elif buyer1 == "strawberries" and buyer2 == "chocolate" :
 print(f"{b} and {a}")
elif buyer1 == "special" and buyer2 == "strawberries" :
 print(f"{c} and {b}")
elif buyer1 == "coffee" and buyer2 == "sour" :
 print(f"{d} and {e}")
elif buyer1 == "sour" and buyer2 == "fruit" :
 print(f"{e} and {f}")
elif buyer1 == "fruit" and buyer2 == "coffee" :
    print(f"{f} and {d}")
elif buyer1 == "chocolate" and buyer2 == "chocolate" : 
    print(f"{a}")
elif buyer1 == "chocolate" and buyer2 == "strawberries" :
 print(f"{a} and {b}")
elif buyer1 == "chocolate" and buyer2 == "coffee" :
 print(f"{a} and {d}")
elif buyer1 == "chocolate" and buyer2 == "sour" :
 print(f"{a} and {e}")
elif buyer1 == "chocolate" and buyer2 == "fruit" :
 print(f"{a} and {f}")
elif buyer1 == "strawberries" and buyer2 == "strawberries" :
 print(f"{b}")
elif buyer1 == "strawberries" and buyer2 == "special" :
 print(f"{b} and {c}")
elif buyer1 == "strawberries" and buyer2 == "coffee" :
 print(f"{b} and {d}")
elif buyer1 == "strawberries" and buyer2 == "sour" :
 print(f"{b} and {e}")
elif buyer1 == "strawberries" and buyer2 == "fruit" :
 print(f"{b} and {f}")
elif buyer1 == "special" and buyer2 == "special" :
 print(f"{c}")
elif buyer1 == "special" and buyer2 == "chocolate" :
 print(f"{c} and {a}")
elif buyer1 == "special" and buyer2 == "coffee" :
 print(f"{c} and {d}")
elif buyer1 == "special" and buyer2 == "sour" :
 print(f"{c} and {e}")
elif buyer1 == "special" and buyer2 == "fruit" :
 print(f"{c} and {f}")
elif buyer1 == "coffee" and buyer2 == "chocolate" :
 print(f"{d} and {a}")
elif buyer1 == "coffee" and buyer2 == "strawberries" :
 print(f"{d} and {b}")
elif buyer1 == "coffee" and buyer2 == "special" :
 print(f"{d} and {c}")
elif buyer1 == "coffee" and buyer2 == "coffee" :
 print(f"{d}")
elif buyer1 == "sour" and buyer2 == "chocolate" :
 print(f"{e} and {a}")
elif buyer1 == "coffee" and buyer2 == "fruit" :
 print(f"{d} and {f}")
elif buyer1 == "sour" and buyer2 == "strawberries" :
 print(f"{c} and {b}")
elif buyer1 == "sour" and buyer2 == "special" :
 print(f"{e} and {c}")
elif buyer1 == "sour" and buyer2 == "coffee" :
 print(f"{e} and {d}")
elif buyer1 == "sour" and buyer2 == "sour" :
 print(f"{e}")
elif buyer1 == "fruit" and buyer2 == "chocolate" :
 print(f"{f} and {a}")
elif buyer1 == "fruit" and buyer2 == "srrawberries" :
 print(f"{f} and {b}")
elif buyer1 == "fruit" and buyer2 == "special" :
 print(f"{f} and {c}")
elif buyer1 == "fruit" and buyer2 == "coffee" :
 print(f"{f} and {d}")
else :
 print(f"{f}")
