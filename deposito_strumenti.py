from strumento import Strumento
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}
        self.prestiti = {}

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            file = open(file_path, "r", encoding="utf-8")
            for riga in file:
                dati = riga.strip().split(",")
                codice = dati[0]
                tipo = dati[1]
                marca = dati[2]
                anno_acquisto = dati[3]
                valore = dati[4]
                if codice not in self.strumenti:
                    strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
                    self.strumenti[codice] = strumento
            file.close()
        except FileNotFoundError:
            print(f"Il file non è stato trovato")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        codice = "S" + str(len(self.strumenti) + 1)
        nuovo_strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.strumenti[codice] = nuovo_strumento
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        from operator import attrgetter
        lista_strumenti = list(self.strumenti.values())
        lista_strumenti.sort(key=attrgetter("marca"))
        return lista_strumenti

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        codice = "P" + (str(len(self.prestiti) + 1))
        if  id_strumento not in self.strumenti:
            raise Exception("Lo strumento non esiste")
        for prestito in self.prestiti.values():
            if prestito.id_strumento == id_strumento:
                raise Exception("Lo strumento è già in prestito")
        nuovo_prestito = Prestito(codice, data, id_strumento, cognome_allievo)
        self.prestiti[codice] = nuovo_prestito
        return nuovo_prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestiti:
            raise Exception("Il codice non corrisponde ad alcun prestito esistente")
        self.prestiti.pop(id_prestito)
