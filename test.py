import pygame
import flet as ft
import io
import base64
import threading
import time
import math

pygame.init()
WIDTH, HEIGHT = 400, 300
surface = pygame.Surface((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLUE = (100, 70, 255)
EDGE_COLOR = (255, 255, 255)


class ObjectInSpace:
    def __init__(self, scale=1):
        self.scale = scale
        self.vertices = [[x / self.scale, y / self.scale, z / self.scale] for x, y, z in [
            [-5, -2, 0.5], [0, 8, 0.5], [5, -2, 0.5], [0, 0, 0.5],
            [-4, -1, -0.5], [0, 6, -0.5], [4, -1, -0.5], [0, 1, -0.5]]]
        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
        self.faces = [(0, 1, 3), (1, 2, 3), (4, 5, 7), (5, 6, 7), (0, 1, 5), (0, 4, 5),
                      (2, 3, 7), (2, 6, 7), (0, 3, 4), (3, 4, 7), (1, 2, 5), (2, 5, 6)]

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
        return int(WIDTH / 2 + x * WIDTH / 4), int(HEIGHT / 2 - y * HEIGHT / 4)


OBJ = ObjectInSpace(5)
angle_x, angle_y, angle_z = 0, 0, 0


def get_frame():
    global angle_x, angle_y, angle_z
    surface.fill(WHITE)
    angle_x += 0.02
    angle_y += 0.01
    angle_z += 0.005
    transformed_vertices = [OBJ.rotate_3d(v, angle_x, angle_y, angle_z) for v in OBJ.vertices]
    projected_points = [OBJ.project_3d_to_2d(v) for v in transformed_vertices]
    for face in OBJ.faces:
        pygame.draw.polygon(surface, BLUE, [projected_points[i] for i in face])
    for edge in OBJ.edges:
        pygame.draw.line(surface, EDGE_COLOR, projected_points[edge[0]], projected_points[edge[1]], 2)
    buffer = io.BytesIO()
    pygame.image.save(surface, buffer, "PNG")
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")


def update_loop(page: ft.Page, img: ft.Image, interval=0.05):
    while True:
        img.src_base64 = get_frame()
        page.update()
        time.sleep(interval)


def main(page: ft.Page):
    img = ft.Image(width=WIDTH, height=HEIGHT, src_base64=get_frame())
    page.add(img)
    threading.Thread(target=update_loop, args=(page, img), daemon=True).start()


ft.app(target=main)
