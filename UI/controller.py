import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fill_dds(self):
        for y in range(2015, 2019):
            self.view.dd_anno.options.append(ft.dropdown.Option(f"{y}"))
        for b in self.model.brands:
            self.view.dd_brand.options.append(ft.dropdown.Option(f"{b}"))

    def handle_crea_grafo(self, e):
        if self.view.dd_brand.value is None or self.view.dd_anno.value is None:
            self.view.create_alert("Selezionare un brand e un anno")
            return
        brand = self.view.dd_brand.value
        year = int(self.view.dd_anno.value)
        graph = self.model.build_graph(brand, year)
        self.view.txt_result.controls.clear()
        self.view.txt_result.controls.append(ft.Text(f"Grafo con {len(graph.nodes)} nodi e "
                                                     f"{len(graph.edges)} archi creato"))
        sorted_edges, duplicati = self.model.get_archi_pesanti()
        self.view.txt_result.controls.append(ft.Text(f"I tre archi più pesanti sono: "))
        for edge in sorted_edges:
            self.view.txt_result.controls.append(ft.Text(f"{edge[0]} -> {edge[1]}: "
                                                         f"{graph[edge[0]][edge[1]]['weight']}"))
        self.view.txt_result.controls.append(ft.Text(f"I nodi duplicati sono {duplicati}"))
        self.view.update_page()

    def handle_percorso(self, e):
        pass

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model
