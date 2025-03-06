class ExampleClass:
    def __init__(self):
        self.existing_field = "This field exists"

def generate_no_such_field_exception():
    instance = ExampleClass()
    print(instance.non_existent_field)
generate_no_such_field_exception()
