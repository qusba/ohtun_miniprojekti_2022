class ValidateReference:

    def __init__(self, input):
        self.new_key = input

    def does_this_key_already_exist(self, references):
        for reference in references:
            key = reference.get_key()
            if self.new_key == key:
                #True = there is already a key like this
                return True
            #False = There is no such key yet
            return False