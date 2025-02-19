import flet as ft


class ContainerCreator(ft.Container):
    def __init__(self, width, height, border_radius, padding, content=None):
        super().__init__()
        self.width = width
        self.height = height
        self.bgcolor = ft.colors.WHITE
        self.border_radius = ft.border_radius.all(border_radius)
        self.padding = padding
        if content is not None:
            self.content = content


if __name__ == "__main__":

    def main(page: ft.Page):
        page.add(ContainerCreator(width=350, height=700, border_radius=20, padding=20))

    ft.app(main)
