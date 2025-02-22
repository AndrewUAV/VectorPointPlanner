import io
import math
import time
import pygame
import base64
import asyncio
import flet as ft


class ObjectInSpace:
    def __init__(self, scale=1, width=400, height=300, angle_x=0, angle_y=0, angle_z=0):
        self.py_init = pygame.init()
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height))
        self.BLACK = (0, 0, 0) # (0, 0, 0) (255, 255, 255)
        self.BLUE = (100, 70, 255)
        self.EDGE_COLOR = (255, 255, 255)
        self.angle_x, self.angle_y, self.angle_z = angle_x, angle_y, angle_z
        self.scale = scale
        self.color_menu_data = (255, 165, 0)

        self.vertices = [[x * self.scale, y * self.scale, z * self.scale] for x, y, z in [
                         [-5, -2, 0.5], [0, 8, 0.5], [5, -2, 0.5], [0, 0, 0.5],
                         [-4, -1, -0.5], [0, 6, -0.5], [4, -1, -0.5], [0, 1, -0.5]]]

        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0),
                      (4, 5), (5, 6), (6, 7), (7, 4),
                      (0, 4), (1, 5), (2, 6), (3, 7)]

        self.faces = [(0, 1, 3), (1, 2, 3),  # Верх
                      (4, 5, 7), (5, 6, 7),  # Низ
                      (0, 1, 5), (0, 4, 5),  # Передня грань
                      (2, 3, 7), (2, 6, 7),  # Задня грань
                      (0, 3, 4), (3, 4, 7),  # Ліва грань
                      (1, 2, 5), (2, 5, 6)  # Права грань
                    ]

    def rotate_3d(self, point, angle_x, angle_y, angle_z):
        x, y, z = point

        cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
        y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x

        cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
        x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y

        cos_z, sin_z = math.cos(angle_z), math.sin(angle_z)
        x, y = x * cos_z - y * sin_z, x * sin_z + y * cos_z

        return x, y, z

    def project_3d_to_2d(self, point, fov=400, distance=5):
        x, y, z = point
        z += distance
        factor = fov / (fov + z)
        x, y = x * factor, y * factor
        return int(self.width / 2 + x * self.width / 4), int(self.height / 2 - y * self.height / 4)


    def add_menu_data(self, roll=0, pitch=0, yaw=0, sats=0, hdop=0, air_speed=0,
                      ground_speed=0, all_bat_vol=0, bat_cel_vol=0, current=0):
        font = pygame.font.Font(None, 24)

        text_surface = font.render(f"Yaw: {yaw:.2f}°", True, self.color_menu_data)
        self.surface.blit(text_surface, (self.height // 2, 10))

        text_surface = font.render(f"Roll: {roll:.2f}°", True, self.color_menu_data)
        self.surface.blit(text_surface, (10, 40))  # Відображення у верхньому лівому куті

        text_surface = font.render(f"Pitch: {pitch:.2f}°", True, self.color_menu_data)
        self.surface.blit(text_surface, (10, 70))

        text_surface = font.render(f"Sats: {sats:.2f}", True, self.color_menu_data)
        self.surface.blit(text_surface, (10, 120))

        text_surface = font.render(f"Hdop: {hdop:.2f}", True, self.color_menu_data)
        self.surface.blit(text_surface, (10, 150))

        text_surface = font.render(f"Air Speed: {air_speed:.2f}", True, self.color_menu_data)
        self.surface.blit(text_surface, (10, 200))

        text_surface = font.render(f"Ground Speed: {ground_speed:.2f}", True, self.color_menu_data)
        self.surface.blit(text_surface, (10, 230))

    def get_frame(self):
        self.surface.fill(self.BLACK)
        self.angle_x += 0.02
        self.angle_y += 0.01
        self.angle_z += 0.005
        transformed_vertices = [self.rotate_3d(v, self.angle_x, self.angle_y, self.angle_z) for v in self.vertices]
        projected_points = [self.project_3d_to_2d(v) for v in transformed_vertices]
        for face in self.faces:
            pygame.draw.polygon(self.surface, self.BLUE, [projected_points[i] for i in face])
        for edge in self.edges:
            pygame.draw.line(self.surface, self.EDGE_COLOR, projected_points[edge[0]], projected_points[edge[1]], 2)

        self.add_menu_data(roll=self.angle_x, pitch=self.angle_y, yaw=self.angle_z) # add menu data

        buffer = io.BytesIO()
        pygame.image.save(self.surface, buffer, "PNG")
        buffer.seek(0)
        return base64.b64encode(buffer.read()).decode("utf-8")

    async def update_loop(self, page: ft.Page, img: ft.Image, interval=0.01):
        while True:
            img.src_base64 = self.get_frame()
            page.update()
            await asyncio.sleep(interval)

if __name__ == "__main__":
    async def main(page: ft.Page):
        ob = ObjectInSpace(scale=0.2)
        img = ft.Image(width=ob.width, height=ob.height, src_base64=ob.get_frame())
        page.add(img)
        asyncio.create_task(ob.update_loop(page, img))


    ft.app(target=main)


