import flet as ft


class ElevatedButtonCreator(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.Colors.ORANGE
        self.color = ft.Colors.BLACK
        self.text = text


if __name__ == "__main__":

    def main(page: ft.Page):
        page.add(ElevatedButtonCreator(text="OK"))

    ft.app(main)
