from file_handler import FileHandler
from reference_handler import ReferenceHandler


class App:
    def __init__(self, io):
        self.io = io

        #When the program starts filehandler gets references
        # from storage files and these are passed to refHandler
        self.fileHandler = FileHandler()
        self.references = self.fileHandler.read_book_refs_form_file()
        self.referenceHandler = ReferenceHandler(io, self.references)

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
                    self.io.write("Tähän syöttettäis viitteen tiedot")
                    self.io.write("")
                    #Inputs go as parameters to the object generation methods
                    #self.referenceHandler.generate_book_reference_object()
                    
                except Exception as error:
                    self.io.write("Jotain meni vikaan")
            elif command == "2":
                try:
                    self.referenceHandler.print_references()
                    #self.io.write("Pitäs printata kaikki")
                    self.io.write("")
                except Exception as error:
                    self.io.write("Jotain meni vikaan")