import flet as ft


class TabsCreator(ft.Tabs):
    def __init__(self, tabs, animation_duration=200, expend=True, selected_index=1):
        super().__init__()
        self.animation_duration = animation_duration
        self.expand = expend
        self.tabs = tabs
        self.selected_index = selected_index

        self.label_color = ft.Colors.ORANGE
        self.divider_color = ft.Colors.RED_300
        self.overlay_color = ft.Colors.ORANGE
        self.indicator_color = ft.Colors.RED
        self.unselected_label_color = ft.Colors.ORANGE_600
        self.expend = expend


if __name__ == "__main__":

    def main(page: ft.Page):
        page.add(ft.Container(content=TabsCreator(tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center,
                    bgcolor=ft.Colors.BLACK
                )),
            ft.Tab(
                text="Tab 2",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                )),
        ])))

    ft.app(main)
