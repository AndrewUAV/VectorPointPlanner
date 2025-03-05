import flet as ft

from MainBar import MainBar
from MainVisualizationData import MainVisualizationData


class VectorPointPlanner:
    def __init__(self):
        pass

    def setup_vpp(self):
        return ft.Column(controls=[
            MainBar().create_main_bar(),
            MainVisualizationData().setup_data_visualization(),
        ],
            expand=True)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(VectorPointPlanner().setup_vpp())

    ft.app(main)
    #ft.app(main, view=ft.AppView.WEB_BROWSER)
