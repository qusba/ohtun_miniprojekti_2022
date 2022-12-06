class ValidateReference:
    def __init__(self):
        self.references = []

    def does_this_key_already_exist(self, input_key, references):
        for reference in references:
            key = reference.get_key()
            if input_key == key:
                # True = there is already a key like this
                return True
        # False = There is no such key yet
        return False

    #Other validations here?
