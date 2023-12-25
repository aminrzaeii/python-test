#amin rezaei
# calculator project in python

# This function adds two numbers
def jam(x , y):
    return x + y

# This function subtracts two numbers
def kam(x , y):
    return x - y

# This function multiplies two numbers
def zarb(x, y):
    return x * y

# This function divides two numbers
def taqsim(x, y):
    return x / y


print("Select operation.")
print("1.jam")
print("2.kam")
print("3.zarb")
print("4.taqsim")

while True:
    #  input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check 
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", jam(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", kam(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", zarb(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", taqsim(num1, num2))
        break
    else:
        print("Invalid Input")
