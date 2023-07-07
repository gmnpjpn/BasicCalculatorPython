try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))

    option = 0

    while option != 6:
        print("""
        Choose an option:

        1) +
        2) -
        3) *
        4) /
        5) Change values
        6) Exit
        """)

        option = int(input())

        if option == 1:
            print()
            print("Resultado: ", number1, " + ", number2, " = ", number1+number2)
        
        elif option == 2:
            print()
            print("Resultado: ", number1, " - ", number2, " = ", number1-number2)
        
        elif option == 3:
            print()
            print("Resultado: ", number1, " - ", number2, " = ", number1*number2)

        elif option == 4:
            print()
            print("Resultado: ", number1, " - ", number2, " = ", number1/number2)

        elif option == 5:
            print()
            number1 = int(input("Choose the first number: "))
            number2 = int(input("Choose the second number"))

except Exception:
    print("An exception happened")