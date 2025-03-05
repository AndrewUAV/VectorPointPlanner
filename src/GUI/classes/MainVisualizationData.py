import flet as ft

from new_styles.Map import Map
from new_styles.Container import ContainerCreator

from MainControlsBar import MainControlsBar


class MainVisualizationData:
    def __init__(self):
        self.add_map = Map().setup_map()
        self.map_container = ContainerCreator(content=self.add_map)
        self.osd_container = ContainerCreator()
        self.controls_container = ContainerCreator(content=MainControlsBar().get_main_controls_bar(), expand=False)

    def setup_data_visualization(self):
        return ft.Row(controls=[

            ft.Column(controls=[
                self.osd_container,
                self.controls_container
            ],
                expand=True),

            ft.Column(controls=[
                self.map_container
            ],
                expand=True)
        ],
            expand=True)


if __name__ == "__main__":

    def main(page: ft.Page):
        page.add(MainVisualizationData().setup_data_visualization())

    ft.app(main)

