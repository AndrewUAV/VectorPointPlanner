import flet as ft

class Page:
    def __init__(self, _title=None, _theme_mode=None):
        self._title = _title if _title is not None else "Page"
        self._theme_mode = _theme_mode if _theme_mode is not None else 'dark'


    def setup_page(self, page: ft.Page):
        page.title = self._title
        page.theme_mode = self._theme_mode
        page.update()


    def add_buttons_like_row(self, list_buttons):
        return ft.Row(controls=list_buttons)


    def add_button(self, page: ft.Page, new_button):
        page.add(new_button)



if __name__ == "__main__":

    def main(page: ft.Page):
        my_page = Page()
        my_page.setup_page(page)

        # Перевірка, чи не перевизначена тема на рівні елементів:
        page.add(ft.Text("Hello, this is the dark theme page!"))

    ft.app(target=main)
