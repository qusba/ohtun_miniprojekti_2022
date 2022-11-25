from refclasses.bookref import Bookref

class ReferenceHandler:
    def __init__(self,io,fileHandler):
        self.io = io
        self.fileHandler = fileHandler
        self.references = self.fileHandler.read_book_refs_from_file()

    #For every different ref object we need
    #different method because of the different
    #fields in references
    def generate_book_reference_object(self, inputs):
        #Generate ref <- Todo
        #After that send the ref to filehandler for storing
        #(In this model all references are
        # written to the file when new one is added)
        book_object = Bookref(inputs[0],inputs[1],int(inputs[2]),inputs[3])
        self.references.append(book_object)
        self.fileHandler.write_book_refs_to_file(self.references)


    def print_references(self):
        for reference in self.references:
            self.io.write(reference.__str__())