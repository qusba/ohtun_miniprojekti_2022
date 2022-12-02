from stub_io import StubIO
from reference_handler import ReferenceHandler
from file_handler import FileHandler
from app import App

class ReferenceLibrary:
    def __init__(self):
        file = open("src/storage/testing_storage.csv","w")
        file.close()

        self._file_handler = FileHandler("src/storage/testing_storage.csv")
        self.stub_io = StubIO()
        self._reference_handler = ReferenceHandler(self.stub_io,self._file_handler)

    def run_application_with_inputs(self):
        app = App(self.stub_io,self._file_handler,self._reference_handler)
        app.run()
    
    def print_references(self):
        self._reference_handler.print_references()
    
    def user_input(self,value):
        self.stub_io.input_value(value)
    
    def output_should_contain(self, value):
        outputs = self.stub_io.get_outputs()
        if not value in outputs:
            raise AssertionError(
                f'Output \"{value}\" is not in {str(outputs)}'
            )
    




    
    #def reference_key_should_be(self, expected):
        
        




