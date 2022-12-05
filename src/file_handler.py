from refclasses.bookref import Bookref


class FileHandler:
    # FileHandler takes the paths to the storage files as parameters
    def __init__(self, books_file_path):
        self.references = []
        self.books_file_path = books_file_path

    def get_references(self):
        return self.references

    def set_references(self, references):
        self.references = references

    def read_book_refs_from_file(self):
        self.references = []
        # Format of the storage file:
        # key;author;title;year;publisher
        books_file = open(self.books_file_path, "r")
        lines = books_file.readlines()

        if len(lines) > 0:
            for line in lines:
                book_object = Bookref(str(line.split(";")[0]), line.split(";")[1],
                                      line.split(";")[2], int(
                                          line.split(";")[3]),
                                      line.split(";")[4].strip())
                self.references.append(book_object)
        books_file.close()
        return self.references

    def write_book_refs_to_file(self, references):
        self.references = references
        books_file = open(self.books_file_path, "w")
        for reference in self.references:
            str_to_write = str(reference.key+";"+reference.author+";"+reference.title+";" +
                               str(reference.year)+";"+reference.publisher+"\n")
            books_file.write(str_to_write)
        books_file.close()

    def write_ref_object_into_bibtext_file(self, ref_object, file_to_write):
        ref_object_fields = list(ref_object.__dict__.keys())

        str_to_write = str("@"+ref_object.type+"{"+ref_object.key+",\n")
        for key in ref_object_fields[2:]:
            str_to_write = str_to_write + \
                ("    "+key+" = {"+str(ref_object.__dict__[key])+"},\n")
        str_to_write = str_to_write+"}\n\n"

        file_to_write.write(str_to_write)

    def write_bibtext_file(self, path_to_bibtext_file):
        if len(self.references) == 0:
            return 0
        else:
            file = open(path_to_bibtext_file, "w")
            for ref in self.references:
                self.write_ref_object_into_bibtext_file(ref, file)
            file.close()
            return 1

    def remove_reference_from_file(self, ref_key):
        # this method removes the wanted reference from the list and then rewrites the csv file without it
        ref_list = self.read_book_refs_from_file()
        rem_success = False
        for ref in ref_list:
            if ref.get_key() == ref_key:
                ref_list.remove(ref)
                rem_success = True
                self.clear_for_rewrite()
                self.write_book_refs_to_file(ref_list)
                return rem_success
        return rem_success

    def clear_for_rewrite(self):
        # opening a csv file like this removes the content of the file
        books_file = open(self.books_file_path, "w+")
        books_file.close()
        # print("done")
