

class App:
    def __init__(self, io, filehandler, referencehandler, referencevalidator):
        self.io = io
        self.bib_file_path = "references.bib"
        #When the program starts filehandler gets references
        # from storage files and these are passed to refHandler
        self.fileHandler = filehandler
        self.referenceHandler = referencehandler
        self.referenceValidator = referencevalidator

    def run(self):
        while True:
            self.io.write("Syötä 1 lisätäksesi viite")
            self.io.write("Syötä 2 listataksesi kaikki viitteet")
            self.io.write("Syötä 3 luodaksesi bibtext tiedosto")
            self.io.write("Syötä 4 poistaaksesi viite avaimen perusteella")
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
                    if key.strip() == "":
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue
                    if self.referenceValidator.does_this_key_already_exist(str(key),
                                            self.fileHandler.get_references()) == True:
                        self.io.write("\nTällä avaimella löytyy jo viite\n")
                        continue
                    author = self.io.read("Kirjailija: ")
                    if author.strip() == "":
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue
                    title = self.io.read("Nimi: ")
                    if title.strip() == "":
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue
                    year = self.io.read("Julkaisuvuosi: ")
                    if key.strip() == "":
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue
                    if year.isdigit() == False:
                        self.io.write("\nJulkaisuvuoden tulee olla positiivinen kokonaisluku\n")
                        continue
                    publisher = self.io.read("Julkaisija: ")
                    if publisher.strip() == "":
                        self.io.write("\nSyöte ei saa olla tyhjä\n")
                        continue

                    #Inputs go as parameters to the object generation methods
                    self.referenceHandler.generate_book_reference_object([str(key), author, title,
                                                                        int(year), publisher])
                    self.io.write("\nViite lisätty \n")

                except Exception as error:
                    self.io.write("\nJotain meni vikaan \n")
            elif command == "2":
                try:
                    self.io.write("")
                    self.referenceHandler.print_references()
                    self.io.write("")
                except Exception as error:
                    self.io.write("\nJotain meni vikaan \n")
            elif command == "3":
                try:
                    return_bit = self.fileHandler.write_bibtext_file(self.bib_file_path)
                    if return_bit == 0:
                        self.io.write("Ei viitteitä \n")
                    else:
                        self.io.write("references.bib tiedosto luotu \n")
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