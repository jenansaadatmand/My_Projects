# A Guessing game:
# Ask the user: "What's my favorite food?"
# If the user enters the name of your favorite food, output:"Yep! So amazing!"
# If the user does not enter the name of your favorite food, output: "Yuck! That's not it!"
# Regardless of what the user enters, output:"Thanks for playing!" 

user_input = input("What's my favorite food?")

favorite_food = "cookies"

if user_input == favorite_food:
    print("Yup! So amazing!")
else:
    print("Yuck! that's not it!")

print("Thanks for playing!")


# Solution 2:

guess = input("What's my favorite food?")

if guess == "cookies":
    print("Yup! So amazing!")
else: 
    print("Yuck! that's not it!")

print("Thanks for playing!")



# Solution 3: using not equal sign:

guess = input("What's my favorite food?")

if guess != "cookies":
    print("Yuck! that's not it!")
else: 
    print("Yup! So amazing!")

print("Thanks for playing!")