import pygame

import requests
from io import BytesIO


pygame.init()


window_size = WIDTH, HEIGHT = 1000, 1000
window = pygame.display.set_mode(window_size)


def get_map_img():
    api_server = "http://static-maps.yandex.ru/1.x/"

    lon = "37.530887"
    lat = "55.703118"
    delta = "0.002"

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    response = requests.get(api_server, params=params)

    io = BytesIO(response.content)
    io.seek(0)
    img = pygame.image.load(io)
    img = pygame.transform.scale(img, window_size)
    return img


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    map_img = get_map_img()
    window.blit(map_img, (0, 0))

    pygame.display.flip()

pygame.quit()
