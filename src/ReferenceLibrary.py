from stub_io import StubIO
from reference_handler import ReferenceHandler
from file_handler import FileHandler
from app import App

class ReferenceLibrary:
    def __init__(self, io, file_handler, reference_handler):
        self._io = StubIO()
        self._reference_handler = ReferenceHandler()
        self._file_handler = FileHandler()
        self._app = App(
            self._io,
            self._file_handler,
            self._reference_handler
        )

    def run_application(self):
        self._app.run()
    
    def input(self, value):
        self._io.add_input(value)
    
    def output_should_contain(self, value):
        outputs = self._io.outputs
        if not value in outputs:
            raise AssertionError(
                f'Output \"{value}\" is not in {str(outputs)}'
            )

    def add_book_reference(self, inputs):
        self._reference_handler.generate_book_reference_object(inputs)

    
    #def reference_key_should_be(self, expected):
        
        




