import flet as ft

class Settings:
    def __init__(self, page: ft.Page):
        self.page = page

    def setup(self):
        return ft.Text("Settings Page")