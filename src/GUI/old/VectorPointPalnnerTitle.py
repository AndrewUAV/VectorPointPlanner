
import flet as ft
import flet.canvas as cv


class VectorPointPlannerTitle():
    def __init__(self):
        pass

    def setup(self):
        # Return the canvas object correctly
        return cv.Canvas([
            cv.Text(
                text="VectorPointPlanner",  # Keyword argument for text
                x=50,                        # Positional argument for x-coordinate
                y=0,                        # Positional argument for y-coordinate
                text_align=ft.TextAlign.RIGHT,

                style=ft.TextStyle(
                    weight=ft.FontWeight.BOLD,
                    size=50,
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            (200, 200),
                            (300, 300),
                            colors=[ft.Colors.ORANGE, ft.Colors.RED],
                        ),
                        stroke_join=ft.StrokeJoin.ROUND,
                        stroke_cap=ft.StrokeCap.ROUND,
                    ),
                ),
            ),
        ])


if __name__ == "__main__":
    def main(page: ft.Page):
        # Add the setup method content to the page
        page.add(VectorPointPlannerTitle().setup())

    ft.app(main)
