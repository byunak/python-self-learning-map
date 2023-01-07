### This code will allow user to convert temperature values between Celcius and Fahrenheit.

# This code below greets the user and asks for the conversion type
print("Hello! Please select the type of conversion you want to make")
selected_conversion = int(input("Type 1 if you want to convert from Celcius to Fahrenheit or type 2 if you want to convert from Fahrenheit to Celcius: "))


# This code below asks for the Celcius or Fahrenheit input depended on the previous input. Then do the conversion with given calculation algorithm. Prints the solution out.
if selected_conversion == 1:
    print("")
    celcius = float(input("Please enter the temperature as Celcius: "))
    celc_to_fahr = ((celcius *(9/5) )+32)
    print(celcius, "Celcius degree is equal to, ", celc_to_fahr, " Fahrenheit degrees")
elif selected_conversion == 2:
    print("")
    fahrenheit = float(input("Please enter the temperature as Fahrenheit: "))
    fahr_to_celc = ((fahrenheit-32)*5/9)
    print(fahrenheit, "Fahrenheit degree is equal to, ", fahr_to_celc, " Celcius degrees")    
# This code below handles possible errors such as if user inputs another number
elif selected_conversion > 2:
    print("")
    print("You should pick 1 or 2 to continue the conversion process")
    print("")
    selected_conversion = int(input("Type 1 if you want to convert from Celcius to Fahrenheit or type 2 if you want to convert from Fahrenheit to Celcius."))
elif selected_conversion < 1:
    print("")
    print("You should pick 1 or 2 to continue the conversion process")
    print("")
    selected_conversion = int(input("Type 1 if you want to convert from Celcius to Fahrenheit or type 2 if you want to convert from Fahrenheit to Celcius."))


# I have realized that error handling here is weak because I did not think of every error possible. 
# For example, I forgot to check for false input for the second question. I also forgot to check if user inputs a letter instead of numbers
# Better error handling would be sth. like | if selection_conversion is != 1 or != 2 