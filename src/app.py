from file_handler import FileHandler
from reference_handler import ReferenceHandler


class App:
    def __init__(self, io):
        self.io = io

        #When the program starts filehandler gets references
        # from storage files and these are passed to refHandler
        books_file_path = "src/storage/book_references.csv"
        self.fileHandler = FileHandler(books_file_path)
        self.referenceHandler = ReferenceHandler(io,self.fileHandler)

    def run(self):
        while True:
            self.io.write("Syötä 1 lisätäksesi viite")
            self.io.write("Syötä 2 listataksesi kaikki viitteet")
            self.io.write("Paina enter lopettaaksesi")
            self.io.write("")
            command = self.io.read("Syötä komento: ")

            if not command:
                break

            if command == "1":
                #The input prompts for different ref classes need
                #to be interactive because different refs
                #have different fields
                try:
                    key = self.io.read("Avain: ")
                    author = self.io.read("Kirjailija: ")
                    title = self.io.read("Nimi: ")
                    year = self.io.read("Julkaisuvuosi: ")
                    publisher = self.io.read("Julkaisija: ")

                    #Inputs go as parameters to the object generation methods
                    self.referenceHandler.generate_book_reference_object([key, author, title,
                                                                        int(year), publisher])
                    self.io.write("")

                except Exception as error:
                    self.io.write(error)
                    self.io.write("\nJotain meni vikaan \n")
            elif command == "2":
                try:
                    self.io.write("")
                    self.referenceHandler.print_references()
                    self.io.write("")
                except Exception as error:
                    self.io.write("\nJotain meni vikaan \n")