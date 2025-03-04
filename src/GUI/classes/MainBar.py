
import flet as ft
import serial.tools.list_ports

from new_styles.Title import TitleCreator
from new_styles.Button import ButtonCreator
from new_styles.DropDown import DropDownCreator


class MainBar:
    def __init__(self):
        self.height = 60
        self.data_button = ButtonCreator(text="Data")
        self.mission_planing_button = ButtonCreator(text="Mission Planning")
        self.setting_button = ButtonCreator(text="Settings")
        self.connect_button = ButtonCreator(text="Connect")

        self.baudrate_list = [4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
        self.ports_list = ["UDP", "TCP"] + [port.device for port in serial.tools.list_ports.comports()]

        self.baudrate_dropdown = DropDownCreator([ft.dropdown.Option(i) for i in self.baudrate_list])
        self.ports_dropdown = DropDownCreator([ft.dropdown.Option(i) for i in self.ports_list])

    def create_main_bar(self):
        main_bar = ft.Column(controls=[
            ft.Row(controls=[TitleCreator().setup()],
                   height=self.height-40),
            ft.Row(
                controls=[
                    self.data_button,
                    self.mission_planing_button,
                    self.setting_button,

                    self.ports_dropdown,
                    self.baudrate_dropdown,

                    self.connect_button
                ],

                alignment=ft.MainAxisAlignment.CENTER,
                height=self.height
            )
        ])

        return main_bar


if __name__ == "__main__":

    def main(page: ft.Page):
        page.add(MainBar().create_main_bar())

    ft.app(main)