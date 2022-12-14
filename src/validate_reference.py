class ValidateReference:
    def __init__(self):
        pass

    def does_this_key_already_exist(self, input_key, references):
        for reference in references:
            key = reference.get_key()
            if input_key == key:
                return True
        return False

    def is_input_empty(self, user_input):
        if user_input.strip() == "":
            return True
        return False

    def is_input_a_number(self, user_input):
        return user_input.isdigit()

    def is_number_positive(self, user_input):
        return int(user_input) >= 0
