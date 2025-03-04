import flet as ft


class ButtonCreator(ft.CupertinoFilledButton):
    def __init__(self, text="Button"):
        super().__init__()
        self.content = ft.Text(text)
        self.opacity_on_click = 0.3
        self.bgcolor = ft.Colors.ORANGE
        self.color = ft.Colors.BLACK
        self.expand = True  # дозволяє кнопкам займати доступну площу


if __name__ == "__main__":
    def main(page: ft.Page):
        # Створюємо три кнопки
        button1 = ButtonCreator(text="Button 1")
        button2 = ButtonCreator(text="Button 2")
        button3 = ButtonCreator(text="Button 3")

        # Додаємо кнопки в один рядок з вказаною висотою
        row = ft.Row(
            controls=[button1, button2, button3],
            alignment=ft.MainAxisAlignment.CENTER,
            height=10 # Задаємо висоту рядка
        )

        # Додаємо рядок з кнопками на сторінку
        page.add(row)

    ft.app(main)
