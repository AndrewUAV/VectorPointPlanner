import cv2
import base64
import flet as ft
import threading
import time
import asyncio

from io import BytesIO
from PIL import Image
from styles.Container import ContainerCreator
from ObjectInSpace import ObjectInSpace

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

            time.sleep(0.06)
        self.cap.release()


class VideoStreamer:
    def __init__(self,page, map=None, obj_in_space=None):
        self.page = page
        if map is not None:
            self.map = map
        if obj_in_space is not None:
            self.obj_in_space = obj_in_space

        self.video_capture = VideoCapture(0)

    def add_obj_in_space(self):
        obj_in_space = ObjectInSpace(0.08)
        img = ft.Image(width=obj_in_space.width, height=obj_in_space.height,
                            src_base64=obj_in_space.get_frame())
        asyncio.create_task(obj_in_space.update_loop(self.page, img))
        return img

    def create_containers_2x3(self):
        imgs = [ft.Image(width=350, height=300, fit=ft.ImageFit.CONTAIN) for _ in range(2)]

        container1 = ContainerCreator(width=750, height=350, border_radius=1, padding=1, content=imgs[0])
        container2 = ContainerCreator(width=750, height=350, border_radius=1, padding=1, content=self.add_obj_in_space())
        container3 = ContainerCreator(width=750, height=350, border_radius=1, padding=1, content=imgs[1])
        container4 = ContainerCreator(width=750, height=350, border_radius=1, padding=1, content=self.map.setup_map())

        grid = ft.Column(
            controls=[
                ft.Row(controls=[container1, container2]),
                ft.Row(controls=[container3, container4]),
            ]
        )
        return grid, imgs

    def start_stream(self, imgs):

        threading.Thread(target=self.video_capture.capture_video, args=(imgs,), daemon=True).start()


if __name__ == "__main__":
    from Map import Map
    async def main(page: ft.Page):
        page.theme_mode = 'dark'
        map = Map()
        vs = VideoStreamer(map=map, page=page)
        grid, imgs = vs.create_containers_2x3()
        page.add(grid)
        vs.start_stream(imgs)

    ft.app(main)
