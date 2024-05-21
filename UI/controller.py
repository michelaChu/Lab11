import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        anni = [2015,2016,2017,2018]
        for a in anni:
            self._view._ddyear.options.append(ft.dropdown.Option(a))

        colori = self._model._allColors
        for c in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(c))

        self._view.update_page()


    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        self._model.creaGrafo(self._view._ddcolor.value, self._view._ddyear.value)
        self._view.txtOut.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodes()}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {self._model.getNumEdges()}"))
        for arco in self._model.getTop3():
            self._view.txtOut.controls.append(ft.Text(f"Arco da a , peso"))
        self._view.update_page()

    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
