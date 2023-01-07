### A terminal calculator that works for a single operation

# This code below creates a function to define what kind of operation is selected by user
def calculation(selected_operation, number_1, number_2):
    if selected_operation == 1:
        return number_1 + number_2
    elif selected_operation ==2: 
        return number_1 - number_2
    elif selected_operation ==3: 
        return number_1 / number_2
    elif selected_operation ==4: 
        return number_1 * number_2
    else:
        return False

# While loop starts the calculation process by asking the type of operation. 
# If error happens or operation is completed code loops back to here
while True:
    
    # Prints out the possible operation options
    print("Please select an operation to start calculating...")
    print("1- Addition")
    print("2- Subtraction")
    print("3- Division")
    print("4- Multiplication")
    try:
    # Asks for input to determine what operation is chosen by user
        selected_operation = int(input())
        if selected_operation < 1 or selected_operation > 4:
            print("Invalid input. Please enter a number between 1-4 to select an operation.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number between 1-4 to select an operation.")
        continue

    try:
        number_1 = int(input("Please enter the first number to calculate: "))
        number_2 = int(input("Please enter the second number to calculate: "))
        result =  calculation(selected_operation,number_1,number_2)
        print("Result is ", result)
        print("")
        print("")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue