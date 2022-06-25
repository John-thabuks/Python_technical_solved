import math

#Creating the condition that will be infinate if True

while True:
    print("\nChoose your preferred math operation:\
        \n\n0 - Addition\
        \n1 - Subtraction\
        \n2 - Multiplication\
        \n3 - Division\
        \n4 - Modulo\
        \n5 - Raising to a power\
        \n6 - Square root\
        \n7 - Logarithm\
        \n8 - Sine\
        \n9 - Cosine\
        \n10 - Tangent\n")
    user_input = input("\nEnter your option from the menue: ")

#We need also a condition for checking if input entered is within our range
    #if not; we through an error (if/elif/else code-blocks)
    #NB// return type of input() is string...
    #Addition
    if user_input == '0':
        first_value = float(input("\nPlease enter your first value: "))
        second_value = float(input("\nPlease enter your second value: "))

        print(f"\nThe result is: {str(first_value + second_value)}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? (y/n) ")

        if forward_or_back_option == 'y':
            continue
        else:
            break
    
    #Subtraction
    elif user_input == '1':
        first_value = float(input("\nPlease enter your first value: "))
        second_value = float(input("\nPlease enter your second value: "))

        print(f"\nThe result is: {str(first_value - second_value)}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? y/n ")

        if forward_or_back_option == "y":
            continue
        else:
            break

    #Multiplication
    elif user_input == '2':
        first_value = float(input("\nPlease enter your first value: "))
        second_value = float(input("\nPlease enter your second value: "))

        print(f"\nThe result is: {str(first_value * second_value)}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? y/n")

        if forward_or_back_option == "y":
            continue
        else:
            break
    
    #Division
    elif user_input == '3':
        first_value = float(input("\nPlease enter your first value: "))
        second_value = float(input("\nPlease enter your second value: "))

        print(f"\nThe result is: {str(first_value / second_value)}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? y/n ")

        if forward_or_back_option == "y":
            continue
        else:
            break

    #Modulo
    elif user_input == '4':
        first_value = float(input("\nPlease enter your first value: "))
        second_value = float(input("\nPlease enter your second value: "))

        print(f"\nThe result is: {str(first_value % second_value)}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? y/n ")

        if forward_or_back_option == "y":
            continue
        else:
            break

    #Raising to a power
    elif user_input == '5':
        first_value = float(input("\nPlease enter your first value: "))
        second_value = float(input("\nPlease enter your second value: "))

        print(f"\nThe result is: {str(math.pow(first_value, second_value))}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? y/n ")

        if forward_or_back_option == "y":
            continue
        else:
            break

    #Square root
    elif user_input == '6':
        first_value = float(input("\nPlease enter your value to find the square root: "))

        print(f"\nThe result is: {str(math.sqrt(first_value))}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? y/n ")

        if forward_or_back_option == "y":
            continue
        else:
            break

    #Logarith
    elif user_input == '7':
        first_value = float(input("\nPlease enter your Log value: "))

        print(f"\nThe result is: {str(math.log(first_value,2))}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? y/n ")

        if forward_or_back_option == "y":
            continue
        else:
            break

    #Sine
    elif user_input == '8':
        first_value = float(input("\nPlease enter your Sin value: "))

        print(f"\nThe result is: {str(math.sin(math.radians(first_value)))}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? y/n ")

        if forward_or_back_option == "y":
            continue
        else:
            break

    #cosine
    elif user_input == '9':
        first_value = float(input("\nPlease enter your Cos value: "))

        print(f"\nThe result is: {str(math.cos(math.radians(first_value)))}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? y/n ")

        if forward_or_back_option == "y":
            continue
        else:
            break

    #Tangent
    elif user_input == '10':
        first_value = float(input("\nPlease enter your Tan value: "))

        print(f"\nThe result is: {str(math.tan(math.radians(first_value)))}\n")

        forward_or_back_option = input("\nDo you wish to go back to the main menu? y/n ")

        if forward_or_back_option == "y":
            continue
        else:
            break

    #Lets handle the invalid user inpits
    else:
        print("\nInvalid option!\n")
        continue 

     


    