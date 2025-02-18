import flet as ft


class Button:
    def __init__(self, text=None, text_color = None, width=None, height=None, color=None, on_click=None):
        self.text = text if text is not None else 'text'
        self.text_color = text_color if text_color is not None else 'black'
        self.width = width if width is not None else 100
        self.height = height if height is not None else 30
        self.color = color if color is not None else 'orange'
        self.on_click = on_click if on_click is not None else 'default'

    def create_button(self):
        return ft.ElevatedButton(
            text=self.text,
            color=self.text_color,
            width=self.width,
            height=self.height,
            bgcolor=self.color,
            on_click=self.on_button_click
        )

    def on_button_click(self, e):
        func = {'default': self.default_click,
                'data_click': self.data_click,
                'mission_planning_click': self.mission_planning_click,
                'settings_click': self.settings_click}


        func_name = self.on_click
        if func_name in func:
            func[func_name](e)
        else:
            print("No function assigned")


    def settings_click(self, e):
        print("Setting click")


    def mission_planning_click(self, e):
        print("Mission planning")


    def data_click(self, e):
        print("Data click")


    def default_click(self, e):
        print("Button is pressed")


if __name__ == "__main__":

    def main(page: ft.Page):
        button = Button()
        page.add(button.create_button())
    ft.app(target=main)