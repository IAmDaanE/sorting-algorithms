import pygame
import random
import time
import os
import sys

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

speed = 0.5

pygame.init()

def resource_path(file):
    return os.path.join(getattr(sys, "_MEIPASS", "."), file)

font = pygame.font.Font(resource_path("LuckiestGuy-Regular.ttf"), 60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("bubble-sort")

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
130, 131, 132, 133, 134, 135, 136, 137, 138, 139,
140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
150, 151, 152, 153, 154, 155, 156, 157, 158, 159,
160, 161, 162, 163, 164, 165, 166, 167, 168, 169,
170, 171, 172, 173, 174, 175, 176, 177, 178, 179,
180, 181, 182, 183, 184, 185, 186, 187, 188, 189,
190, 191, 192, 193, 194, 195, 196, 197, 198, 199,
200]

random.shuffle(values)

bar_width = SCREEN_WIDTH // len(values)

for i, value in enumerate(values):
    x = i * bar_width
    y = SCREEN_HEIGHT - value * 2
    height = value * 2

    pygame.draw.rect(screen, (255, 255, 255), (x, y, bar_width - 2, height))

pygame.display.update()
running2 = False
running = True
clock = pygame.time.Clock()

counter = 0
max_counter = 199
highlighted = 0
examined = 0

pygame.time.delay(1000)
start_time = time.time()
end_time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if counter == 0:
        swapped = False

    if counter < max_counter:
        if values[counter] > values[counter + 1]:
            values[counter], values[counter + 1] = values[counter + 1], values[counter]
            swapped = True
        counter += 1
    else:
        if not swapped:
            running = False
            running2 = True
            end_time = time.time()
            elapsed = end_time - start_time
            break

        counter = 0
        max_counter -= 1

    
    screen.fill((0, 0, 0))
    
    bar_width = SCREEN_WIDTH // len(values)

    for i, value in enumerate(values):
        x = i * bar_width
        y = SCREEN_HEIGHT - value * 2
        height = value * 2

        pygame.draw.rect(screen, (255, 255, 255), (x, y, bar_width - 2, height))

    pygame.display.update()

for i, value in enumerate(values):
        x = i * bar_width
        y = SCREEN_HEIGHT - value * 2
        height = value * 2

        pygame.draw.rect(screen, (0, 255, 0), (x, y, bar_width - 2, height))
        pygame.time.delay(1)
        pygame.display.update()

while running2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = False

    screen.fill((0, 0, 0))
    for i, value in enumerate(values):
        x = i * bar_width
        y = SCREEN_HEIGHT - value * 2
        height = value * 2

        pygame.draw.rect(screen, (0, 255, 0), (x, y, bar_width - 2, height))
    
    text_surface1 = font.render("Array Sorted!", True, (0, 255, 0))
    text_surface2 = font.render(str(round(elapsed,4)), True, (0, 255, 0))
    text_rect1 = text_surface1.get_rect(midtop=(screen.get_rect().centerx, 70))
    text_rect2 = text_surface2.get_rect(midtop=(screen.get_rect().centerx, 120))
    screen.blit(text_surface1, text_rect1)
    screen.blit(text_surface2, text_rect2)
    pygame.display.update()
    pygame.time.delay(500)
    screen.fill((0, 0, 0))

    for i, value in enumerate(values):

        x = i * bar_width
        y = SCREEN_HEIGHT - value * 2
        height = value * 2

        pygame.draw.rect(screen, (255, 255, 255), (x, y, bar_width - 2, height))
    pygame.display.update()
    pygame.time.delay(500)