from cmath import nan
from refclasses.bookref import Bookref

class FileHandler:
    def __init__(self):
        self.references = []

    def read_book_refs_form_file(self):
        return []

    def write_book_refs_to_file(self, references):
        self.references = references
        #Write the refs to file <- todo
        
