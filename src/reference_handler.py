from refclasses.bookref import Bookref


class ReferenceHandler:
    def __init__(self, io_object, filehandler):
        self.io_object = io_object
        self.filehandler = filehandler
        self.references = self.filehandler.read_book_refs_from_file()

    def get_references(self):
        return self.references

    # For every different ref object we need
    # different method because of the different
    #fields in references
    def generate_book_reference_object(self, inputs):
        self.references = self.filehandler.read_book_refs_from_file()
        # Generate ref
        # After that send the ref to filehandler for storing
        # (In this model all references are
        # written to the file when new one is added)
        book_object = Bookref(str(inputs[0]), inputs[1],
                                inputs[2], inputs[3],
                                int(inputs[4]), inputs[5])
        self.references.append(book_object)
        self.filehandler.write_book_refs_to_file(self.references)

    def print_references(self, references_to_print):
        for reference in references_to_print:
            self.io_object.write(str(reference))

    def sort_refs_to_alphabetical_order_by_author_surname(self):
        self.references = self.filehandler.read_book_refs_from_file()
        sorted_references = sorted(self.references,key=lambda ref: ref.author_last_name)
        return sorted_references

    def print_referencenses_in_alphabetical_order_by_author_surname(self):
        self.print_references(self.sort_refs_to_alphabetical_order_by_author_surname())

    def sort_refs_to_reverse_alphabetical_order_by_author_surname(self):
        self.references = self.filehandler.read_book_refs_from_file()
        sorted_references = sorted(self.references,key=lambda ref: ref.author_last_name, reverse=True)
        return sorted_references

    def print_referencenses_in_reverse_alphabetical_order_by_author_surname(self):
        self.print_references(self.sort_refs_to_reverse_alphabetical_order_by_author_surname())