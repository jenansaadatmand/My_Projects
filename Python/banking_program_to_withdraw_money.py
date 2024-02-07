# A banking program to withdraw money from an ATM, and display current balance. 
# Make the program report a message if the balance falls below the threshold limit of $50
print()

def withdraw_money(current_balance, amount): # Function takes two parameters
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance  # functions returns a value


balance = withdraw_money(100,80)  # Provide two positional arguments, which are preset earlier in the function's definition 

if balance <= 50:
    print("We need to make a deposit")
else:
    print("Nothing to see here!")
