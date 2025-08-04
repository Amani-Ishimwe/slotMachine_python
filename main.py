def deposit():
    while True:
        amount = input("What Would You Like To Deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("The amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount      

def main():
    balance = deposit()



main()    