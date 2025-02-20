import flet as ft


class ElevatedButtonCreator(ft.ElevatedButton):
    def __init__(self, text, width=None, height=None):
        super().__init__()
        self.bgcolor = ft.Colors.ORANGE
        self.color = ft.Colors.BLACK
        self.text = text
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height


if __name__ == "__main__":

    def main(page: ft.Page):
        page.add(ElevatedButtonCreator(text="OK"))

    ft.app(main)
