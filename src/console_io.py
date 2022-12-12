class ConsoleIO:
    def __init__(self):
        self.written = []

    def write(self, value):
        self.written.append(value)
        print(value)

    def read(self, prompt):
        return input(prompt)

    def get_log(self):
        return self.written
    
    def instructions(self):
        # added a method to print instructions, makes the code more readable
        self.write("Syötä 1 lisätäksesi viite")
        self.write("Syötä 2 listataksesi viitteet")
        self.write("Syötä 3 luodaksesi bibtext tiedosto")
        self.write("Syötä 4 poistaaksesi viite avaimen perusteella")
        self.write("Paina enter lopettaaksesi")
        self.write("")

    def reference_instructions(self):
        # instructions for listing references
        self.write("Syötä 1 listataksesi viitteet lisäysjärjestyksessä vanhin ensin")
        self.write("Syötä 2 listataksesi viitteet lisäysjärjestyksessä uusin ensin")
        self.write("Syötä 3 listataksesi viitteet aakkosjärjestykseen kirjoittajan sukunimen mukaan")
        self.write("Syötä 4 listataksesi viitteet käänteiseen aakkosjärjestykseen kirjoittajan sukunimen mukaan")
        self.write("Paina enter palataksesi edelliseen valikkoon")