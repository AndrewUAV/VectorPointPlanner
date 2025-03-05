import flet as ft

from new_styles.Tabs import TabsCreator


class MainControlsBar:
    def __init__(self):

        self.quick = ft.Tab(text="Quick")
        self.preflight = ft.Tab(text="PreFlight")
        self.actions = ft.Tab(text="Actions")

    def get_main_controls_bar(self):
        return ft.Container(content=TabsCreator(tabs=[self.quick, self.preflight, self.actions]))


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(MainControlsBar().get_main_controls_bar())

    ft.app(main)
