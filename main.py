import pygame

import requests
from io import BytesIO


pygame.init()


window_size = WIDTH, HEIGHT = 1000, 1000
window = pygame.display.set_mode(window_size)

api_server = "http://static-maps.yandex.ru/1.x/"

lon = "37.530887"
lat = "55.703118"
delta = "0.002"


def get_map_img():
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
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == 1073741906 and float(lon) < 90:
                lat = str(float(lat) + 0.5)
            elif event.key == 1073741905 and float(lon) > 0:
                lat = str(float(lat) - 0.5)
            elif event.key == 1073741904:
                lon = str(float(lon) - 0.5)
            elif event.key == 1073741903:
                lon = str(float(lon) + 0.5)
            elif event.key == 1073741899:
                delta = str(float(delta) - 0.01)
            elif event.key == 1073741902:
                delta = str(float(delta) + 0.01)

    map_img = get_map_img()
    window.blit(map_img, (0, 0))

    pygame.display.flip()

pygame.quit()