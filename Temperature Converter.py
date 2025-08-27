# Task 1
# Write a Python program that: Asks the user to input a
# temperature (e.g., 37C or 98F) Detects whether it's in Celsius
# or Fahrenheit Converts it to the other scale and prints the
# result
# 🛠 Concepts: input(), if/else, string slicing, float conversion
# 🎯 Goal: Practice input handling, basic conditions, and
# arithmetic


# Ask the user to input a temperature value (with unit at the end, like 37C or 98F)
temperature = input("Please Enter the Temperature (e.g., 37C or 98F): ")

# Extract the last character from the input string (which indicates the unit)
# .upper() makes sure it works for both lowercase and uppercase (e.g., 'c' or 'C')
text = temperature[-1].upper()

# Check if the unit is Fahrenheit
if text == "F":
    print("You entered the temperature in Fahrenheit.")

# Check if the unit is Celsius
elif text == "C":
    print("You entered the temperature in Celsius.")

# If it is neither 'C' nor 'F', then it's invalid input
else:
    print("Invalid input! Please enter temperature like 37C or 98F.")
