import flet as ft


class DropdownCreator(ft.Dropdown):
    def __init__(self, width, height, list_content):
        super().__init__()
        self.width = width
        self.height = height
        self.options = list_content
        self.bgcolor = ft.Colors.ORANGE_300
        self.color = ft.Colors.BLACK87



if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(DropdownCreator(width=200, height=50,
                                                        list_content=[ft.dropdown.Option(1)]))


    ft.app(target=main)