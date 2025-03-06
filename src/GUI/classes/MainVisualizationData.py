import asyncio
import flet as ft

from new_styles.Map import Map
from new_styles.Container import ContainerCreator

from ObjectInSpace import ObjectInSpace
from MainControlsBar import MainControlsBar


class MainVisualizationData:
    def __init__(self, page):
        self.page = page
        self.add_map = Map().setup_map()
        self.map_container = ContainerCreator(content=self.add_map)
        self.osd_container = ContainerCreator(content=self.add_obj_in_space())
        self.controls_container = ContainerCreator(content=ft.Row(controls=[MainControlsBar().get_main_controls_bar()]),
                                                   expand=True)

    def add_obj_in_space(self):
        obj_in_space = ObjectInSpace(0.08)
        img = ft.Image(width=obj_in_space.width, height=obj_in_space.height, src_base64=obj_in_space.get_frame())
        asyncio.create_task(obj_in_space.update_loop(self.page, img))
        return img

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

    async def main(page: ft.Page):
        page.add(MainVisualizationData(page).setup_data_visualization())

    ft.app(main)

