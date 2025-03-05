import flet as ft

from VectorPointPlanner import VectorPointPlanner


def main(page: ft.Page):
    vpp = VectorPointPlanner()
    page.add(vpp.setup_vpp())


if __name__ == "__main__":

    #ft.app(main)
    ft.app(main, view=ft.AppView.WEB_BROWSER)