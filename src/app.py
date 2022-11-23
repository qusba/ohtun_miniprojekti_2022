class App:
    def __init__(self, io):
        self.io = io

    def run(self):
        while True:
            self.io.write("Syötä 1 lisätäksesi viite")
            self.io.write("Syötä 2 listataksesi kaikki viitteet")
            self.io.write("Paina enter lopettaaksesi")
            self.io.write("")
            command = self.io.read("Syötä komento: ")

            if not command:
                self.io.write("Ai moti loppu, ei se mitään :)")
                break

            if command == "1":
                try:
                    self.io.write("Tähän syöttettäis viitteen tiedot")
                    self.io.write("")
                except Exception as error:
                    self.io.write("Jotain meni vikaan")
            elif command == "2":
                try:
                    self.io.write("Pitäs printata kaikki")
                    self.io.write("")
                except Exception as error:
                    self.io.write("Jotain meni vikaan")