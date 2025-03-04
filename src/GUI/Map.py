import flet as ft
import flet.map as map


class Map:
    def __init__(self, start_lat=None, start_lon=None, start_zoom=None,
                 max_zoom=None, min_zoom=None, width=None, height=None):
        self.expend = True
        self.start_lat = 0 if start_lat is None else start_lat
        self.start_lon = 0 if start_lon is None else start_lon
        self.start_zoom = 5 if start_zoom is None else start_zoom
        self.max_zoom = 15 if max_zoom is None else max_zoom
        self.min_zoom = 2 if min_zoom is None else min_zoom
        self.map_url = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
        self.width = 800 if width is None else width
        self.height = 600 if height is None else height

    def setup_map(self):
        return map.Map(
            expand=self.expend,
            initial_center=map.MapLatitudeLongitude(self.start_lat, self.start_lon),
            initial_zoom=self.start_zoom,
            max_zoom=self.max_zoom,
            min_zoom=self.min_zoom,
            width=self.width,
            height=self.height,
            layers=[
                map.TileLayer(
                    url_template=self.map_url
                )
            ],
        )

    def create_map(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.setup_map()
                ]
            ),
            alignment=ft.Alignment(1, 0),
        )

