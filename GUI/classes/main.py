import flet as ft
from VectorPointPlanner import VectorPointPlanner


def main(page: ft.Page):
    vpp = VectorPointPlanner()
    vpp.get_page(page)


ft.app(target=main)