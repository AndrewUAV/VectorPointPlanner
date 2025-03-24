import flet as ft

class Streamer:
    def __init__(self, page: ft.Page):
        self.page = page

    def setup(self):
        return ft.Text("Video Streamer Page")