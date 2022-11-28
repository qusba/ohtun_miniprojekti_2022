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