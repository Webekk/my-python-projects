def add(number1, number2):
    return number1 + number2
def subtract(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1 * number2
def divide(number1, number2):
    if number2 == 0:
        raise ZeroDivisionError("You can't divide by zero")
    else:
        return number1 / number2

def main():
    print("WELCOME TO THE CALCULATOR!!!")
    print("Choose the operation you want to perform")
    while True:
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Quit (Q)")
        user_decision = input("Your choice: ")

        if user_decision == "+":
                add_result1 = float(input("Enter your first number: "))
                add_result2 = float(input("Enter your second number: "))
                result = add(add_result1, add_result2)
                print(f"The result is: {add_result1} + {add_result2} = {result}")

        elif user_decision == "-":
                subtract_variable1 = float(input("Enter your first number: "))
                subtract_variable2 = float(input("Enter your second number: "))
                result = subtract(subtract_variable1, subtract_variable2)
                print(f"The result is: {subtract_variable1} - {subtract_variable2} = {result}")

        elif user_decision == "*":
                multiply_variable1 = float(input("Enter your first number: "))
                multiply_variable2 = float(input("Enter your second number: "))
                result = multiply(multiply_variable1, multiply_variable2)
                print(f"The result is: {multiply_variable1} * {multiply_variable2} = {result}")

        elif user_decision == "/":
                division_variable1 = float(input("Enter your first number: "))
                division_variable2 = float(input("Enter your second number: "))
                result = divide(division_variable1, division_variable2)
                print(f"The result is: {division_variable1} / {division_variable2} = {result}")

        elif user_decision.lower() == "q":
            print("Thank you for using calculator")
            break
        else:
            print("Invalid input, please try again")

if __name__ == "__main__":
    main()
