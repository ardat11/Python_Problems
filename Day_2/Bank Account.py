def withdraw():
    global balance

    while True:

        request = int(input("Enter the amount of money you want to withdraw"))
        if request <= balance:
            balance = balance - request
            print("money withdrawn successfully")
            print("available balance:", balance)
            break
        else:
            print("Insufficient balance for request")

def deposit():
    global balance

    while True:
        req = int(input("Enter the amount of money you want to deposit"))
        balance = balance + req
        print("Money deposited succesfully. Available balance:", balance)



balance = int(input("Enter your balance"))

while True:
    ask = input("press W to withdraw, D to deposit money.").lower()
    if ask == "w":
        withdraw()
        break

    elif ask == "n":
        deposit()
        break

    else:
        print("invalid request")











