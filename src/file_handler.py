from refclasses.bookref import Bookref

class FileHandler:
    #FileHandler takes the paths to the storage files as parameters
    def __init__(self, books_file_path):
        self.references = []
        self.books_file_path = books_file_path
    
    def get_references(self):
        #for testing
        return self.references

    def read_book_refs_from_file(self):
        #Format of the storage file:
        #key;author;title;year;publisher
        books_file = open(self.books_file_path, "r")
        lines = books_file.readlines()

        if len(lines) > 0:
            for line in lines:
                book_object = Bookref(line.split(";")[0],line.split(";")[1],
                                    line.split(";")[2],int(line.split(";")[3]),
                                    line.split(";")[4].strip())
                self.references.append(book_object)
        books_file.close()
        return self.references

    def write_book_refs_to_file(self, references):
        self.references = references
        books_file = open(self.books_file_path, "w")
        for reference in self.references:
            str_to_write = str(reference.key+";"+reference.author+";"+reference.title+";"+
                                str(reference.year)+";"+reference.publisher+"\n")
            books_file.write(str_to_write)
        books_file.close()

    def write_ref_object_into_bibtext_file(self, ref_object, file_to_write):
        ref_object_fields = list(ref_object.__dict__.keys())
        
        str_to_write =str("@"+ref_object.type+"{"+ref_object.key+",\n")
        for key in ref_object_fields[2:]:
            str_to_write = str_to_write+("    "+key+" = {"+str(ref_object.__dict__[key])+"},\n")
        str_to_write = str_to_write+"}\n\n"
        
        file_to_write.write(str_to_write)
        
    def write_bibtext_file(self, path_to_bibtext_file):
        file = open(path_to_bibtext_file, "w")
        for ref in self.references:
            self.write_ref_object_into_bibtext_file(ref, file)
        file.close()