from console_io import ConsoleIO
from app import App

def main():
    console_io = ConsoleIO()
    app = App(console_io)
    app.run()

if __name__ == "__main__":
    main()