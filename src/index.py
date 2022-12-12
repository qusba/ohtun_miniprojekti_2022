import os
from console_io import ConsoleIO
from file_handler import FileHandler
from reference_handler import ReferenceHandler
from validate_reference import ValidateReference
from app import App

def main():
    path_to_this_files_location = os.path.dirname(os.path.realpath(__file__))
    books_file_path = str(path_to_this_files_location+"/storage/book_references.csv")
    console_io = ConsoleIO()
    filehandler = FileHandler(books_file_path)
    referencehandler = ReferenceHandler(console_io, filehandler)
    referencevalidator = ValidateReference()
    app = App(console_io, filehandler, referencehandler, referencevalidator)
    app.run()

if __name__ == "__main__":
    main()