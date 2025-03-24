import flet as ft


class ContainerCreator(ft.Container):
    def __init__(self, border_radius=2, padding=2, content=None, aligment=None,expand=True):
        super().__init__()
        self.expand = expand
        self.bgcolor = ft.colors.BLACK # BLACK WHITE
        self.border_radius = ft.border_radius.all(border_radius)
        self.padding = padding
        if content is not None:
            self.content = content
        if aligment is not None:
            self.alignment = aligment


if __name__ == "__main__":

    def main(page: ft.Page):
        page.add(ContainerCreator())

    ft.app(main)