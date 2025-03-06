def generate_file_not_found_exception():
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)

# Call the function
generate_file_not_found_exception()
