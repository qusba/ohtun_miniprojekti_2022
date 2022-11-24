from sqlalchemy import null
from refclasses.bookref import Bookref

class ReferenceHandler:
    def __init__(self,io, references):
        self.io = io
        self.references = references

    #For every different ref object we need 
    #different method because of the different
    #fields in references
    def generate_book_reference_object(self):
        return null

    def print_references(self):
        self.io.write("Refe printti tänne")