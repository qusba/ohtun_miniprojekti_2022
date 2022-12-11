# pylint: disable=C0103
from stub_io import StubIO
from reference_handler import ReferenceHandler
from file_handler import FileHandler
from validate_reference import ValidateReference
from app import App


class ReferenceLibrary:
    def __init__(self):
        with open("src/storage/testing_storage.csv", "w") as file:
            file.close()

        self._file_handler = FileHandler("src/storage/testing_storage.csv")
        self.stub_io = StubIO()
        self._reference_handler = ReferenceHandler(
            self.stub_io, self._file_handler)
        self.reference_validator = ValidateReference()

    def run_application_with_inputs(self):
        app = App(self.stub_io, self._file_handler,
                  self._reference_handler, self.reference_validator)
        app.run()

    def print_references(self):
        self._reference_handler.print_references(self._file_handler.read_book_refs_from_file())

    def user_input(self, value):
        self.stub_io.input_value(value)

    def output_should_contain(self, value):
        outputs = self.stub_io.get_outputs()
        if not value in outputs:
            raise AssertionError(
                f'Output \"{value}\" is not in {str(outputs)}'
            )