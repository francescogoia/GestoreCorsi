import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._pd = None


    def get_corsi_periodo(self, e):
        if self._pd is None:
            self._view.create_alert("Selezionare un periodo didattico")
            return None
        corsi = self._model.get_corsi_periodo(self._pd)
        self._view.list_result.controls.clear()
        for corso in corsi:
            self._view.list_result.controls.append(ft.Text(corso))
        self._view.update_page()


    def get_studenti_periodo(self, e):
        if self._pd is None:
            self._view.create_alert("Selezionare un periodo didattico")
            return None
        numero_studenti = self._model.get_numero_studenti_periodo(self._pd)
        self._view.list_result.controls.clear()
        self._view.list_result.controls.append(ft.Text(f"Gli studenti iscrtitti ai corsi del periodo didattico {self._pd} sono {numero_studenti}"))
        self._view.update_page()

    def get_studenti_corso(self, e):
        pass
    def get_dettagli_corso(self, e):
        pass
    def leggi_tendina(self, e):
        self._pd = self._view.dd_periodo.value
        ## e.control.value == self._view.dd_periodo.value
        print(self._pd)