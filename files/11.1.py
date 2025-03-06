def read_file(keys):
    try:
        with open(keys, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file '{keys}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = "keys.txt"
read_file(file_name)

