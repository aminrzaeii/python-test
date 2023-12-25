#amin rezaei
#bakery project

#my list
breadList = ["barbari", "lavash", "taftoon", "sangak", "shirmal"]
#bread dict
breads = {
    "barbari": 1300,
    "lavash": 200,
    "taftoon": 1700,
    "sangak": 5000,
    "shirmal": 8000
}
bread1 = 0
bread2 = 0
bread3 = 0
bread4 = 0
bread5 = 0
#Information about the buyer
name = input("What's your name, dear? ")
phoneNumber = input("Please enter your phone number: ")
print("Give me your card, please.")

password1 = int(input("Please enter your password: "))
password2 = int(input("Please enter your password again: "))

while password1 != password2:
    print("Passwords is not correct")
    password2 = int(input("Please try again: "))

self_checkout = "notdefined"

while self_checkout != "done":
    if self_checkout == "notdefined":
        self_checkout = input("Enter the type of bread you want: ")
    else:
        self_checkout = input("Please enter your next bread: ")

    while self_checkout not in breads:
        if self_checkout == "done":
            break
        self_checkout = input("Please choose from the available breads: ")

    if self_checkout == "done":
        break

    num = int(input(f"How many {self_checkout} do you want? "))
    if self_checkout == "barbari":
        bread1 += breads["barbari"] * num
        print(f"The total cost is {bread1}.")
    elif self_checkout == "lavash":
        bread2 += breads["lavash"] * num
        print(f"The total cost is {bread2}.")
    elif self_checkout == "taftoon":
        bread3 += breads["taftoon"] * num
        print(f"The total cost is {bread3}.")
    elif self_checkout == "sangak":
        bread4 += breads["sangak"] * num
        print(f"The total cost is {bread4}.")
    elif self_checkout == "shirmal":
        bread5 += breads["shirmal"] * num
        print(f"The total cost is {bread5}.")

total = bread1 + bread2 + bread3 + bread4 + bread5
print("Your items have been entered.")
print(f"So your total is {total}.")
