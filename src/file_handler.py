from refclasses.bookref import Bookref

class FileHandler:
    def __init__(self):
        self.references = []

    def read_book_refs_from_file(self):
        #Format of the storage file:
        #author;title;year;publisher
        books_file = open("src/storage/book_references.csv", "r")
        lines = books_file.readlines()
        for line in lines:
            book_object = Bookref(line.split(";")[0],line.split(";")[1],
                                int(line.split(";")[2]),line.split(";")[3])
            self.references.append(book_object)
        return self.references

    def write_book_refs_to_file(self, references):
        self.references = references
        books_file = open("storage/book_references.csv", "w")
        for reference in self.references:
            str_to_write = str(reference.author+";"+reference.title+";"+
                                str(reference.year)+";"+reference.publisher)
            books_file.write(str_to_write)
        books_file.close()
