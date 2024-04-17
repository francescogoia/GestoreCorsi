from database.corso_dao import CorsoDao
class Model:
    def __init__(self):
        self.corsi = CorsoDao.get_all_corsi()

    def get_corsi_periodo(self, pd):
        return CorsoDao.get_corsi_periodo(pd)


    def get_studenti_periodo(self, pd):
        """
        ## soluzione con join da sql
        matricole = CorsoDao.get_studenti_periodo(pd)
        return len(matricole)       """
        ## soluzione con mappa relazioni
        matricole = set()
        for corso in self.corsi:
            if corso.pd == int(pd):
                matricole_corso = corso.get_studenti()
                if matricole_corso is None:
                    corso.Studenti = CorsoDao.get_studenti_singolo_corso(corso.codins)
                    matricole_corso = corso.Studenti
                # unione degli iscritti
                matricole = matricole.union(matricole_corso)
        return len(matricole)