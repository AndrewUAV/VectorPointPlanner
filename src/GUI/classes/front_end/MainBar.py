import flet as ft
import serial.tools.list_ports

from new_styles.Title import TitleCreator
from new_styles.Button import ButtonCreator
from new_styles.DropDown import DropDownCreator

from StreamerPage import Streamer
from SettingsPage import Settings
from MissionPlanningPage import MissionPlanning
from MainVisualizationData import MainVisualizationData


class MainBar:
    def __init__(self, page):
        self.page = page
        self.height = 60
        self.data_button = ButtonCreator(text="Data", on_click=self.show_data_page)
        self.mission_planing_button = ButtonCreator(text="Mission Planning", on_click=self.show_mission_planing_page)
        self.setting_button = ButtonCreator(text="Settings", on_click=self.show_settings_page)
        self.video_streamer_button = ButtonCreator(text="Video Streamer", on_click=self.show_video_streamer_page)
        self.connect_button = ButtonCreator(text="Connect")

        self.baudrate_list = [4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
        self.ports_list = ["UDP", "TCP"] + [port.device for port in serial.tools.list_ports.comports()]

        self.baudrate_dropdown = DropDownCreator(list_content=[ft.dropdown.Option(i) for i in self.baudrate_list],
                                                 label="Baud rate")
        self.ports_dropdown = DropDownCreator(list_content=[ft.dropdown.Option(i) for i in self.ports_list],
                                              label="Ports")

    def create_main_bar(self):
        main_bar = ft.Column(controls=[

            ft.Row(controls=[TitleCreator().setup()],

                   height=self.height-40),
            ft.Row(
                controls=[
                    self.data_button,
                    self.mission_planing_button,
                    self.setting_button,
                    self.video_streamer_button,

                    self.ports_dropdown,
                    self.baudrate_dropdown,

                    self.connect_button
                ],

                alignment=ft.MainAxisAlignment.CENTER,
                height=self.height
            )
        ])

        return main_bar

    async def show_page(self, page_name):
        self.page.controls.clear()
        self.page.add(self.create_main_bar())

        if page_name == "data":
            self.page.add(MainVisualizationData(self.page).setup_data_visualization())
        elif page_name == "mission":
            self.page.add(MissionPlanning(self.page).setup())
        elif page_name == "settings":
            self.page.add(Settings(self.page).setup())
        elif page_name == "video":
            self.page.add(Streamer(self.page).setup())
        self.page.update()

    async def show_data_page(self, e):
        await self.show_page("data")

    async def show_mission_planing_page(self, e):
        await self.show_page("mission")

    async def show_settings_page(self, e):
        await self.show_page("settings")

    async def show_video_streamer_page(self, e):
        await self.show_page("video")


if __name__ == "__main__":
    async def main(page: ft.Page):
        main_bar = MainBar(page)
        page.add(main_bar.create_main_bar())
        await main_bar.show_page("data")

    ft.app(main)
