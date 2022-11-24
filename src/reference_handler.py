from sqlalchemy import null
from refclasses.bookref import Bookref

class ReferenceHandler:
    def __init__(self,io,fileHandler):
        self.io = io
        self.fileHandler = fileHandler
        self.references = self.fileHandler.read_book_refs_form_file()

    #For every different ref object we need 
    #different method because of the different
    #fields in references
    def generate_book_reference_object(self):
        #Generate ref <- Todo
        #After that send the ref to filehandler for storing
        #(In this model all references are
        # written to the file when new one is added)

        #self.references.append(#newRef)
        #self.fileHandler.write_book_refs_to_file(self.references)
        return null

    def print_references(self):
        self.io.write("Refe printti tänne")