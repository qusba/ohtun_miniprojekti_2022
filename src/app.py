import os

class App:
    def __init__(self, io, filehandler, referencehandler, referencevalidator):
        self.io = io
        self.cwd = os.getcwd()
        self.bib_file_path = "references.bib"
        #When the program starts filehandler gets references
        # from storage files and these are passed to refHandler
        self.fileHandler = filehandler
        self.referenceHandler = referencehandler
        self.referenceValidator = referencevalidator

    def list_references(self):
        while True:
            self.io.reference_instructions() # prints instructions on how to list references
            command = self.io.read("Syötä komento: ")
            
            if command == "1":
                try:
                    self.io.write("")
                    self.referenceHandler.print_references(self.fileHandler.read_book_refs_from_file())
                    self.io.write("")
                except Exception as error:
                    print(error)
                    self.io.write("\nJotain meni vikaan \n")
            if command == "2":
                try:
                    self.io.write("")
                    self.referenceHandler.print_references(self.referenceHandler.reverse_the_reference_list())
                    self.io.write("")
                except Exception as error:
                    print(error)
                    self.io.write("\nJotain meni vikaan \n")
            if command == "3":
                try:
                    self.io.write("")
                    self.referenceHandler.print_references(
                                    self.referenceHandler.sort_refs_to_alphabetical_order_by_author_surname())
                    self.io.write("")
                except Exception as error:
                    print(error)
                    self.io.write("\nJotain meni vikaan \n")
            if command == "4":
                try:
                    self.io.write("")
                    self.referenceHandler.print_references(
                            self.referenceHandler.sort_refs_to_reverse_alphabetical_order_by_author_surname())
                    self.io.write("")
                except Exception as error:
                    print(error)
                    self.io.write("\nJotain meni vikaan \n")
            if not command:
                self.io.write("")
                break


    def run(self):
        while True:
            self.io.instructions() # prints instructions
            command = self.io.read("Syötä komento: ")

            if not command:
                break

            if command == "1":
                #The input prompts for different ref classes need
                #to be interactive because different refs
                #have different fields
                try:
                    key = self.io.read("Avain: ")
                    
                    if self.referenceValidator.is_input_empty(key):
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue
                    if self.referenceValidator.does_this_key_already_exist(str(key),
                                            self.fileHandler.get_references()) == True:
                        self.io.write("\nTällä avaimella löytyy jo viite\n")
                        continue
                    author_first_name = self.io.read("Kirjailija etunimi: ")
                    if self.referenceValidator.is_input_empty(author_first_name):
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue
                    author_last_name = self.io.read("Kirjailija sukunimi: ")
                    if self.referenceValidator.is_input_empty(author_last_name):
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue
                    
                    title = self.io.read("Nimi: ")
                    if self.referenceValidator.is_input_empty(title):
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue
                    
                    year = self.io.read("Julkaisuvuosi: ")
                    if self.referenceValidator.is_input_empty(year):
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue
                    if not self.referenceValidator.is_input_a_number(year) or not self.referenceValidator.is_number_positive(year):
                        self.io.write("\nJulkaisuvuoden tulee olla positiivinen kokonaisluku\n")
                        continue
                    
                    publisher = self.io.read("Julkaisija: ")
                    if self.referenceValidator.is_input_empty(publisher):
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue

                    #Inputs go as parameters to the object generation methods
                    self.referenceHandler.generate_book_reference_object([str(key), author_first_name, author_last_name,
                                                                            title, int(year), publisher])
                    self.io.write("\nViite lisätty \n")

                except Exception as error:
                    print(error)
                    self.io.write("\nJotain meni vikaan \n")
            
            elif command == "2":
                try:
                    self.list_references()
                    #self.io.write("")
                    #self.referenceHandler.print_referencenses_in_alphabetical_order_by_author_surname()
                    #self.referenceHandler.print_references(self.fileHandler.read_book_refs_from_file())
                    #self.io.write("")
                except Exception as error:
                    self.io.write("\nJotain meni vikaan \n")
            
            elif command == "3":
                try:
                    return_bit = self.fileHandler.write_bibtext_file(self.bib_file_path)
                    if return_bit == 0:
                        self.io.write("Ei viitteitä \n")
                    else:
                        self.io.write("references.bib tiedosto luotu sijaintiin "+str(self.cwd)+"\n")
                except Exception as error:
                    self.io.write("\nJotain meni vikaan \n")
            
            elif command == "4":
                try:
                    key = self.io.read("Poistettavan viitteen avain: ")
                    rem_success = self.fileHandler.remove_reference_from_file(key)
                    if rem_success == False:
                        self.io.write("Ei vastaavaa viitettä \n")
                    else:
                        self.io.write("Viite poistettu \n")
                except Exception as error:
                    self.io.write("\nJotain meni vikaan \n")