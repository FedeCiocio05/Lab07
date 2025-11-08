import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        self._view._ddMuseo.options.clear()
        self._view._ddEpoca.options.clear()

        #popola musei
        self._view._ddMuseo.options.append(ft.dropdown.Option("Nessun filtro"))
        lista_musei = self._model.get_musei()
        for museo in lista_musei:
            self._view._ddMuseo.options.append(ft.dropdown.Option(museo.nome))

        #popola epoche
        self._view._ddEpoca.options.append(ft.dropdown.Option("Nessun filtro"))
        lista_epoche = self._model.get_epoche()
        for epoca in lista_epoche:
            self._view._ddEpoca.options.append(ft.dropdown.Option(epoca))

        self.museo_selezionato = None
        self.epoca_selezionata = None

        self._view.update()
    # TODO

    # CALLBACKS DROPDOWN
    def on_museo_change(self, e: ft.ControlEvent):
        value = e.control.value if e else None
        self.museo_selezionato = value if value and value != "Nessun filtro" else None

    def on_epoca_change(self, e: ft.ControlEvent):
        value = e.control.value if e else None
        self.epoca_selezionata = value if value and value != "Nessun filtro" else None
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    def on_mostra_artefatti(self, e):
        self._view._lst_results.controls.clear()

        try:
            artefatti = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)

            if artefatti is None:
                self._view.show_alert("Impossibile recuperare gli artefatti dal database.")
                return
            elif not artefatti:
                self._view.show_alert("Nessun artefatto trovato per i filtri selezionati.")
                return
            else:
                for artefatto in artefatti:
                    self._view._lst_results.controls.append(ft.Text(str(artefatto)))

        except Exception as e:
            self._view.show_alert(f'Errore: {e}')

        self._view.update()
    # TODO
