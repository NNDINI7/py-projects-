def show_balance(balance):
    print(f"your balance is ${float(balance):.2f}")

def deposit():
    amount = float(input ("enter an amount to be deposited = "))
    if amount < 0 :
        print("That is not a valid amount")
        return 0 
    else:
        return amount 

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn ="))
    if amount > balance:
        print("Insufficient funds ")
        return 0
    elif amount<0:
        print("Amount must be greater than 0")
    else:
        return amount 


def main():
    balance =0
    is_running = True

    while is_running:
       print("Banking Program")
       print("_____________________________________________")
       print("1. show balance")
       print("2. deposit")
       print("3. withdraw")
       print("4. exit")
       print("__________________________________________")
       choice = input("Enter your choice = ")
       if choice == '1':
          show_balance(balance)
       elif choice=='2':
          balance += deposit()
       elif choice=='3':
          balance -= withdraw(balance)
       elif choice=='4':
          is_running=False
       else: 
         print("invalid choice !!")
         print("_________________________________________")
    print("Thank You Have a Nice Day")

if __name__ == '__main__':
   main()

    