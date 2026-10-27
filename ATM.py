print("Welcome to my Access bank ATM")
User = input("username: ")
Accountnumber = input("account number: ")
password = input("password: ")
username = "Godwin"
password = "Godwin@2026"
account_number = "1234567890"
if User == username and password == password and Accountnumber == account_number:
    print("welcome back")
else:
    print("invalid credentials or account number: ")

user_input = input("what do you want to do? (withdraw, deposit, check balance): ")
balance = 255858599
if user_input == "withdraw":
    amount = int(input("enter amount to withdraw: "))
    if amount > balance:
        print("insufficient funds")
    else:
        balance -= amount 
        print("withdrawal successful. new balance is: ", balance)

    if user_input  == "deposit":
        amount = int(input('enter amount you to send in'))
        amount += balance
        print("transactions succesful")
    else:
        print("invalid amount")   
         