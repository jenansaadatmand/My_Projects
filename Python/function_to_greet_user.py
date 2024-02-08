# A function to greet users, when entering their names

name = input("Enter your name:")
def hello(name):
    print("Hello, ", name.title())

hello(name)