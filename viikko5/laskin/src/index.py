from tkinter import Tk
from kayttoliittyma import Kayttoliittyma
from sovelluslogiikka import Sovelluslogiikka


def main():
    sovelluslogiikka = Sovelluslogiikka()

    window = Tk()
    window.title("Laskin")

    kayttoliittyma = Kayttoliittyma(sovelluslogiikka, window)
    kayttoliittyma.kaynnista()

    window.mainloop()


if __name__ == "__main__":
    main()
