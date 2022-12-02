from stub_io import StubIO
from reference_handler import ReferenceHandler
from file_handler import FileHandler
from app import App

class ReferenceLibrary:
    def __init__(self, io, file_handler, reference_handler):
        self._file_handler = FileHandler("src/storage/testing_storage.csv")
        self._reference_handler = ReferenceHandler(self._file_handler)

    def run_application_with_parameters(self,parameters:list):
        stub_io = StubIO(parameters)
        app = App(stub_io,self._file_handler,self._reference_handler)
        self._app.run()
    
    def print_references(self):
        self._reference_handler.print_references()
    
    def output_should_contain(self, value):
        outputs = self._io.get_outputs()
        if not value in outputs:
            raise AssertionError(
                f'Output \"{value}\" is not in {str(outputs)}'
            )
    
    def clear_testing_file(self):
        file = open("src/storage/testing_storage.csv","w")
        file.close()




    
    #def reference_key_should_be(self, expected):
        
        




