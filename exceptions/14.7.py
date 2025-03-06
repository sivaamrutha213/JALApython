def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("This is the finally block, and it always executes.")

def main():
    divide(10, 2)  
    divide(10, 0)  


main()
