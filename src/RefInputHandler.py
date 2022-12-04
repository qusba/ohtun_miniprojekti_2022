class RefInputHandler:

    def __init__(self, references):
        self.references = references

    def set_references(self, references):
        self.references = references

    def does_this_key_already_exist(self, references):
        for reference in references:
            key = reference.get_key()
            if self.new_key == key:
                #True = there is already a key like this
                return True
            #False = There is no such key yet
            return False