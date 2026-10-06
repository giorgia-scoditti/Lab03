from strumento import Strumento

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}

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
        # DA SISTEMARE!
        codice = "S" + str(len(self.strumenti) + 1)
        nuovo_strumento = (tipo, marca, anno_acquisto, valore)
        self.strumenti[codice] = nuovo_strumento
        return codice

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # DA SISTEMARE!
        from operator import attrgetter
        lista_strumenti = list(self.strumenti)
        lista_strumenti.sort(key=attrgetter("marca"))
        return lista_strumenti

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
