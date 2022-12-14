from refclasses.bookref import Bookref


class ReferenceHandler:
    def __init__(self, io_object, filehandler):
        self.io_object = io_object
        self.filehandler = filehandler
        self.references = self.filehandler.read_book_refs_from_file()

    def get_references(self):
        return self.references

    def set_references(self, references):
        self.references = references

    def generate_book_reference_object(self, inputs):
        self.references = self.filehandler.read_book_refs_from_file()
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
        sorted_references = sorted(
            self.references, key=lambda ref: ref.author_last_name)
        return sorted_references

    def sort_refs_to_reverse_alphabetical_order_by_author_surname(self):
        self.references = self.filehandler.read_book_refs_from_file()
        sorted_references = sorted(
            self.references, key=lambda ref: ref.author_last_name, reverse=True)
        return sorted_references

    def reverse_the_reference_list(self):
        self.references = self.filehandler.read_book_refs_from_file()
        reversed_references = reversed(self.references)
        return reversed_references
