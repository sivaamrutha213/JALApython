# Function to write text to a file
def write_to_file(keys, text):
    try:
        with open(filename, 'w') as file:  # 'w' mode opens the file for writing
            file.write(text)
        print(f"Text successfully written to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input from the user
filename = "keys.txt"  # Specify the filename
text_to_write = input("Ctrl+c:copy: ")

# Write the input text to the file
write_to_file(keys, Ctrl+c-copy)
