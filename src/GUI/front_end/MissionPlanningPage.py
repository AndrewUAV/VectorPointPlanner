import flet as ft


class MissionPlanning:
    def __init__(self, page: ft.Page):
        self.page = page

    def setup(self):
        return ft.Text("Mission Planning Page")