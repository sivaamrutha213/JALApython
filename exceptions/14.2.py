def handle_exception():
    try:
        result = 10 / 0  # This will cause a ZeroDivisionError
        print(result)
    except ZeroDivisionError:
        print("An arithmetic error occurred: Division by zero is not allowed.")
handle_exception()
