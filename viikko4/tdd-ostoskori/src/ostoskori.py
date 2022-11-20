from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self.ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if len(self.ostokset) > 0:
            sum = 0
            for ostos in self.ostokset:
                sum += ostos.lukumaara()
            return sum
        return 0
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2

    def hinta(self):
        if len(self.ostokset) > 0:
            sum = 0
            for ostos in self.ostokset:
                sum += ostos.hinta()
            return sum
        return 0
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        lisattavaOstos = Ostos(lisattava)
        found = False
        for ostos in self.ostokset:
            if ostos.tuotteen_nimi() == lisattavaOstos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(1)
                found = True
        if not found:
            self.ostokset.append(lisattavaOstos)

    def poista_tuote(self, poistettava: Tuote):
        poistettavaOstos = Ostos(poistettava)
        for ostos in self.ostokset:
            if ostos.tuotteen_nimi() == poistettavaOstos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(-1)

        ostoksetFiltered = list(
            filter(lambda x: (x.lukumaara() != 0), self.ostokset))

        self.ostokset = ostoksetFiltered
        # poistaa tuotteen

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
