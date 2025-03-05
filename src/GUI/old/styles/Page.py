import flet as ft


class PageCreator:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.controls.clear()
        self.build()

    def build(self):
        pass

