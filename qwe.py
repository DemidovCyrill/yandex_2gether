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
    img = pygame.transform.scale(img, list(map(lambda x: x // 2, window_size)))
    return img

p1 = p2 = 4
k = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.K_UP:
            p2 = 10
        if event.type == pygame.K_DOWN:
            p2 = 2
        if event.type == pygame.K_LEFT:
            p1 = 10
        if event.type == pygame.K_RIGHT:
            p1 = 2
        if event.type == pygame.K_PAGEUP:
            k += 1
            img = pygame.transform.scale(img, list(map(lambda x: x // (2 * k), window_size)))
        if event.type == pygame.K_PAGEUP:
            k -= 1
            img = pygame.transform.scale(img, list(map(lambda x: x // (2 * k), window_size)))

    map_img = get_map_img()
    window.blit(map_img, (window_size[0] // p1, window_size[1] // p2))

    pygame.display.flip()

pygame.quit()