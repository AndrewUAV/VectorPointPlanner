import flet as ft
from Map import Map
from styles.Container import ContainerCreator
from styles.Button import ElevatedButtonCreator


class VectorPointPlanner:
    def __init__(self, page: ft.Page):
        self.title = "Vector Point Planner"
        self.theme = "dark"
        self.page = page

    def config_page(self):
        self.page.title = self.title
        self.page.theme_mode = self.theme
        self.page.update()

    def create_main_buttons(self):
        self.page.add(ft.Row(controls=[
                                        ElevatedButtonCreator(text="Data"),
                                        ElevatedButtonCreator(text="Mission Planning"),
                                        ElevatedButtonCreator(text="Settings")
                                      ]
                            )
                     )

    def create_main_containers(self):
        self.page.add(ft.Row(controls=[
                                        ContainerCreator(width=760, height=700, border_radius=10,
                                                         padding=20),
                                        ContainerCreator(width=760, height=700, border_radius=10,
                                                         padding=20, content=Map().setup_map())
                                      ]
                            )
                      )


    def setup(self):
        self.config_page()
        self.create_main_buttons()
        self.create_main_containers()


def main(page: ft.Page):
    vvp = VectorPointPlanner(page)
    vvp.setup()


if __name__ == "__main__":
    ft.app(target=main)
    #ft.app(main, view=ft.AppView.WEB_BROWSER)
