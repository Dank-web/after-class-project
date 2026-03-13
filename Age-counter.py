try:
    age = int(input("Enter your age: "))

    #check if age is valid
    if age <= 0 or 120:
        print("Error: Invalid age entered.")
    else:
        print("Age entered is valid.")

        #check is age is even or odd
        if age % 2 == 0:
            print("The age is Even")
        else:
            print("The age is Odd.")

except ValueError:
    print("Error: Please enter a valid number for age.")