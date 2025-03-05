import flet as ft
import flet.map as map


class Map:
    def __init__(self, start_lat=0, start_lon=0, start_zoom=5,
                 max_zoom=15, min_zoom=2, expend=True):
        self.expend = expend
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.start_zoom = start_zoom
        self.max_zoom = max_zoom
        self.min_zoom = min_zoom
        self.map_url = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"

    def setup_map(self):
        return map.Map(
            expand=self.expend,
            initial_center=map.MapLatitudeLongitude(self.start_lat, self.start_lon),
            initial_zoom=self.start_zoom,
            max_zoom=self.max_zoom,
            min_zoom=self.min_zoom,
            layers=[
                map.TileLayer(
                    url_template=self.map_url
                )
            ],
        )


if __name__ == "__main__":

    def main(page: ft.Page):
        page.add(Map().setup_map())

    ft.app(main)