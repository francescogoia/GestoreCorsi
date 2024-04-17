from dataclasses import dataclass

@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int

    studenti: set = None

    def __eq__(self, other):
        return self.codins == other.codins
    def __hash__(self):
        return hash(self.codins)

    def __str__(self):
        return f"{self.nome} ({self.codins})"

    def get_studenti(self):
        if self.studenti in None:
            self.studenti = CorsoDao.get_studenti_singolo_corso(self.codins)
        else:
            return self.studenti