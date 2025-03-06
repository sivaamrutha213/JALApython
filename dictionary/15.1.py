students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "Daisy",
    105: "Edward"
}
students[106] = "Fiona"
students[107] = "George"

# Print the updated dictionary
print("After adding values:", students)
students[103] = "Charlotte"
students[105] = "Eddie"

# Print the updated dictionary
print("After updating values:", students)
student_name = students[102]
print("Accessed value:", student_name)
nested_students = {
    "Class A": {
        101: "Alice",
        102: "Bob"
    },
    "Class B": {
        103: "Charlie",
        104: "Daisy"
    }
}

# Print the nested dictionary
print("Nested dictionary:", nested_students)
class_a_students = nested_students["Class A"]
class_b_students = nested_students["Class B"]

print("Values in Class A:", class_a_students)
print("Values in Class B:", class_b_students)
class_a_keys = nested_students["Class A"].keys()
print("Keys in Class A:", class_a_keys)
del students[104]

# Print the updated dictionary after deletion
print("After deleting a value:", students)
# Step 1: Create a dictionary with at least 5 key-value pairs
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "Daisy",
    105: "Edward"
}

# Step 1.1: Adding values to the dictionary
students[106] = "Fiona"
students[107] = "George"
print("After adding values:", students)

# Step 1.2: Updating values in the dictionary
students[103] = "Charlotte"
students[105] = "Eddie"
print("After updating values:", students)

# Step 1.3: Accessing the value in the dictionary
student_name = students[102]
print("Accessed value:", student_name)

# Step 1.4: Create a nested dictionary
nested_students = {
    "Class A": {
        101: "Alice",
        102: "Bob"
    },
    "Class B": {
        103: "Charlie",
        104: "Daisy"
    }
}
print("Nested dictionary:", nested_students)

# Step 1.5: Access the values of the nested dictionary
class_a_students = nested_students["Class A"]
class_b_students = nested_students["Class B"]
print("Values in Class A:", class_a_students)
print("Values in Class B:", class_b_students)

# Step 1.6: Print the keys present in a particular dictionary
class_a_keys = nested_students["Class A"].keys()
print("Keys in Class A:", class_a_keys)

# Step 1.7: Delete a value from the dictionary
del students[104]
print("After deleting a value:", students)
