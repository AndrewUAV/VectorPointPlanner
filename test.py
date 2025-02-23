import cv2
import base64
import flet as ft
import threading
import time
from io import BytesIO
from PIL import Image
from styles.Container import ContainerCreator

class VideoCapture:
    def __init__(self, video_device):
        self.video_device = video_device
        self.cap = cv2.VideoCapture(self.video_device)

    def capture_video(self, img_controls):
        if not self.cap.isOpened():
            print("Error with open camera")
            return

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame)

            buffered = BytesIO()
            pil_image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

            for img in img_controls:
                img.src_base64 = img_str
                img.update()

            time.sleep(0.03)
        self.cap.release()


class VideoStreamer:
    def __init__(self):
        # створюємо один компонент відеозахоплення,
        # який буде передавати один і той же потік у всі контейнери
        self.video_capture = VideoCapture(0)

    def create_containers_2x3(self):
        # створимо 6 компонентів для відображення відео
        imgs = [ft.Image(width=350, height=300, fit=ft.ImageFit.CONTAIN) for _ in range(6)]

        # створюємо контейнери з додаванням компоненту ft.Image
        container1 = ContainerCreator(width=350, height=300, border_radius=20, padding=20, content=imgs[0])
        container2 = ContainerCreator(width=350, height=300, border_radius=20, padding=20, content=imgs[1])
        container3 = ContainerCreator(width=350, height=300, border_radius=20, padding=20, content=imgs[2])
        container4 = ContainerCreator(width=350, height=300, border_radius=20, padding=20, content=imgs[3])
        container5 = ContainerCreator(width=350, height=300, border_radius=20, padding=20, content=imgs[4])
        container6 = ContainerCreator(width=350, height=300, border_radius=20, padding=20, content=imgs[5])

        # Розташування контейнерів у сітці 2x3
        grid = ft.Column(
            controls=[
                ft.Row(controls=[container1, container2, container3]),
                ft.Row(controls=[container4, container5, container6]),
            ]
        )
        return grid, imgs

    def start_stream(self, imgs):
        # Запускаємо відеопотік в окремому потоці
        threading.Thread(target=self.video_capture.capture_video, args=(imgs,), daemon=True).start()


if __name__ == "__main__":
    def main(page: ft.Page):
        vs = VideoStreamer()
        grid, imgs = vs.create_containers_2x3()
        page.add(grid)
        vs.start_stream(imgs)

    ft.app(main)
