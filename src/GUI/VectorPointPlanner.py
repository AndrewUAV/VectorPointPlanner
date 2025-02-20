import flet as ft
import serial.tools.list_ports

from Map import Map
from VectorPointPalnnerTitle import VectorPointPlannerTitle

from styles.Dropdown import DropdownCreator
from styles.Container import ContainerCreator
from styles.Button import ElevatedButtonCreator


class VectorPointPlanner:
    def __init__(self, page: ft.Page):
        self.title = "Vector Point Planner"
        self.theme = "dark"
        self.page = page

        self.list_baudrate = [4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
        self.baudrate_dropdown = DropdownCreator(width=200, height=50, list_content=[ft.dropdown.Option(i) for i in self.list_baudrate])

        self.list_ports = ["UDP", "TCP"] + [port.device for port in serial.tools.list_ports.comports()]
        self.ports_dropdown = DropdownCreator(width=200, height=50, list_content=[ft.dropdown.Option(i) for i in self.list_ports])

    def config_page(self):
        self.page.title = self.title
        self.page.theme_mode = self.theme
        self.page.update()

    def create_main_buttons(self):
        self.page.add(ft.Row(controls=[
            ft.Row(controls=[
                ElevatedButtonCreator(text="Data", width=130, height=50),
                ElevatedButtonCreator(text="Mission Planning", width=130, height=50),
                ElevatedButtonCreator(text="Settings", width=130, height=50)]),

            ft.Row(controls=[ContainerCreator(width=530, height=70, border_radius=1, padding=1,
                                              content=VectorPointPlannerTitle().setup()),
                             self.ports_dropdown,
                             self.baudrate_dropdown,
                             ElevatedButtonCreator(text="Connect", width=130, height=50)],
                   alignment=ft.MainAxisAlignment.END)
        ]))

    def create_main_containers(self):
        self.page.add(ft.Row(controls=[
                                        ContainerCreator(width=750, height=700, border_radius=10,
                                                         padding=1),
                                        ContainerCreator(width=750, height=700, border_radius=10,
                                                         padding=1, content=Map().setup_map())
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
