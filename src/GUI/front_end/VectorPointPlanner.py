import flet as ft
from MainBar import MainBar


class VectorPointPlanner:
    def __init__(self, page):
        self.page = page
        self.main_bar = MainBar(self.page)

    def setup_vpp(self):
        return ft.Column(controls=[
            self.main_bar.create_main_bar()
        ],
            expand=True)

    async def show_page(self, page_name):
        await self.main_bar.show_page(page_name)

    async def show_data_page(self, e):
        await self.show_page("data")

    async def show_mission_planing_page(self, e):
        await self.show_page("mission")

    async def show_settings_page(self, e):
        await self.show_page("settings")

    async def show_video_streamer_page(self, e):
        await self.show_page("video")


if __name__ == "__main__":
    async def main(page: ft.Page):
        vector_point_planner = VectorPointPlanner(page)
        page.add(vector_point_planner.setup_vpp())
        await vector_point_planner.show_page("data")

    #ft.app(main)
    ft.app(main, view=ft.AppView.WEB_BROWSER)
