import flet as ft


class DropDownCreator(ft.Dropdown):
    def __init__(self, list_content, label):
        super().__init__()
        self.options = list_content
        self.bgcolor = ft.Colors.ORANGE_300
        self.color = ft.Colors.BLACK87
        self.expand = True
        self.label = label

