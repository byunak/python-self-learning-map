# Add a function for the temperature conversion: Instead of repeating the conversion logic in both the if and elif blocks, you could define a function to perform the conversion and call that function from both blocks. 
# This would make the code easier to read and maintain.

# Use a loop to handle invalid input: Instead of using an elif block to handle invalid input, you could use a while loop to keep prompting the user to enter a valid value until they do so. 
# This would make it easier for the user to correct their mistake and avoid having to run the script again.

# Use more descriptive variable names: Instead of using variables like selected_conversion, celcius, and fahrenheit, you could use more descriptive names like conversion_type, celsius_temp, and fahrenheit_temp. 
# This would make the code easier to understand and maintain.

# Add error handling: Currently, the script doesn't handle errors that might occur when the user enters invalid input (e.g. a letter instead of a number). 
# You could add error handling using try-except blocks to gracefully handle these cases and prevent the script from crashing.

def convert_temperature(temp, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return ((temp * 9/5) + 32)
    elif from_unit == "F" and to_unit == "C":
        return ((temp - 32) * 5/9)

print("Hello! Please select the type of conversion you want to make")

while True:
    try:
        conversion_type = int(input("Type 1 if you want to convert from Celcius to Fahrenheit or type 2 if you want to convert from Fahrenheit to Celcius: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if conversion_type == 1:
        try:
            celsius_temp = float(input("Please enter the temperature as Celcius: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        result = convert_temperature(celsius_temp, "C", "F")
        print(celsius_temp, "Celcius degree is equal to, ", result, " Fahrenheit degrees")
        break
    elif conversion_type == 2:
        try:
            fahrenheit_temp = float(input("Please enter the temperature as Fahrenheit: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        result = convert_temperature(fahrenheit_temp, "F", "C")
        print(fahrenheit_temp, "Fahrenheit degree is equal to, ", result, " Celcius degrees")
        break
    else:
        print("You should pick 1 or 2 to continue the conversion process")
