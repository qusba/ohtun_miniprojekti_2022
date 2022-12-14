from refclasses.bookref import Bookref


class FileHandler:
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
        # key;author_first_name;author_last_name;title;year;publisher
        with open(self.books_file_path, "r") as books_file:
            lines = books_file.readlines()

        if len(lines) > 0:
            for line in lines:
                book_object = Bookref(str(line.split(";")[0]), line.split(";")[1],
                                      line.split(";")[2], line.split(";")[3],
                                      int(line.split(";")[4]), line.split(";")[5].strip())
                if len(line.split(";")) > 6:
                    tags = []
                    for i in range(6, len(line.split(";"))):
                        tags.append(line.split(";")[i].strip())
                    book_object.set_tags(tags)
                self.references.append(book_object)
        books_file.close()
        return self.references

    def write_book_refs_to_file(self, references):
        self.references = references
        with open(self.books_file_path, "w") as books_file:
            for reference in self.references:
                str_to_write = str(reference.key+";"+reference.author_first_name+";" +
                                   reference.author_last_name+";"+reference.title+";" +
                                   str(reference.year)+";"+reference.publisher+"\n")
                if len(reference.get_tags()) > 0:
                    for tag in reference.get_tags():
                        str_to_write = str_to_write.strip()+";"+tag
                    str_to_write = str_to_write + "\n"
                books_file.write(str_to_write)
            books_file.close()

    def write_ref_object_into_bibtext_file(self, ref_object, file_to_write):
        ref_object_fields = list(ref_object.__dict__.keys())

        str_to_write = str("@"+ref_object.type+"{"+ref_object.key+",\n" +
                           "    author = {"+ref_object.author_first_name+", "+ref_object.author_last_name+"},\n")
        for key in ref_object_fields[4:-1]:
            str_to_write = str_to_write + \
                ("    "+key+" = {"+str(ref_object.__dict__[key])+"},\n")
        str_to_write = str_to_write+"}\n\n"

        file_to_write.write(str_to_write)

    def write_bibtext_file(self, path_to_bibtext_file):
        if len(self.references) == 0:
            return 0
        with open(path_to_bibtext_file, "w") as file:
            for ref in self.references:
                self.write_ref_object_into_bibtext_file(ref, file)
            file.close()
            return 1

    def remove_reference_from_file(self, ref_key):
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
        with open(self.books_file_path, "w+") as books_file:
            books_file.close()
