from console_io import ConsoleIO
from file_handler import FileHandler
from reference_handler import ReferenceHandler
from validate_reference import ValidateReference
from app import App

def main():
    books_file_path = "src/storage/book_references.csv"
    console_io = ConsoleIO()
    filehandler = FileHandler(books_file_path)
    reference_handler = ReferenceHandler(console_io, filehandler)
    reference_validator = ValidateReference()
    app = App(console_io, filehandler, reference_handler, reference_validator)
    app.run()

if __name__ == "__main__":
    main()