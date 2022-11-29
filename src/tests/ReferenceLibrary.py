from reference_handler import ReferenceHandler

class ReferenceLibrary:
    def __init__(self, io, file_handler):
        self._reference_handler = ReferenceHandler(io, file_handler)

    
    def add_book_reference(self, inputs):
        self._reference_handler.generate_book_reference_object(inputs)

    
    #def reference_should_be(self, expected, imputs):
        #key_expected = expected
        




