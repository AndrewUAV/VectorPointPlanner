import flet as ft

def main(page: ft.Page):
    # URL для вбудовування Google Maps
    map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.0114663285315!2d-122.4194156846818!3d37.77492977975965!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8085808cb79f8c7b%3A0x7ec3ef8c0ef82a4b!2sSan%20Francisco%2C%20CA!5e0!3m2!1sen!2sus!4v1616164210908!5m2!1sen!2sus"

    # Створення WebView з Google Maps
    webview = ft.WebView(src=map_url, width=600, height=450)

    # Додаємо WebView на сторінку
    page.add(webview)

ft.app(target=main)
