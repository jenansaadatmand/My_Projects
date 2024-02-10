# Work with arguments in functions, you will construct a fuel report that requires information from several fuel locations throughout the rocket ship
# Create a fuel report generation function
# Your spaceship has three tanks: Main, External and Hydrogen. 
# You want to create an app to display the amount of fuel in each tank, and the average amount of fuel between the three tanks. 
# Because you wish to reuse this code in other projects, you want to create a function with the logic.
# Create a function named generate_report. The function will take three parameters named main_tank, external_tank and hydrogen_tank. When run, the function will display output which resembles the following:

def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report: 
            Main tank: {main_tank}  
            External tank: {external_tank} 
            Hydrogen tank: {hydrogen_tank}"""  # use """ """ for long paragraph on multiple lines formatting
    print(output)    
generate_report("main_tank", "external_tank", "hydrogen_tank")
print()

# Run the function: With the function created, add the code to run the function with the following values:
# Main tank: 80
# External tank: 70
# Hydrogen tank: 75
generate_report(80, 70, 75)
print()
