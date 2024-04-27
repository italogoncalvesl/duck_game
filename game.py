import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 60
SCREEN_X = 800
SCREEN_Y = 600

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption('AVP 1 - ITALO GONÇALVES')

fundo = pygame.transform.scale(
    pygame.image.load("fundo.jpg"),
    (SCREEN_X, SCREEN_Y))

pato_img = pygame.image.load("pato.png")
pato_img = pygame.transform.scale(pato_img, (80, 80))

mira_img = pygame.image.load("crosshair.png")
cursor_img_rect = mira_img.get_rect()

som_recarga = pygame.mixer.Sound("reload.mp3")
som_tiro = pygame.mixer.Sound("shotgun.mp3")

pato_posição = [
    {'image': pato_img, 'rect': pato_img.get_rect(center=(80, 455)), "velocidade": -1},
    {'image': pato_img, 'rect': pato_img.get_rect(center=(200, 450)), "velocidade": -4},
    {'image': pato_img, 'rect': pato_img.get_rect(center=(600, 480)), "velocidade": -6},
    {'image': pato_img, 'rect': pato_img.get_rect(center=(300, 500)), "velocidade": -2},
    {'image': pato_img, 'rect': pato_img.get_rect(center=(460, 450)), "velocidade": -1},
    {'image': pato_img, 'rect': pato_img.get_rect(center=(540, 500)), "velocidade": -3},
    {'image': pato_img, 'rect': pato_img.get_rect(center=(400, 470)), "velocidade": -2},
    {'image': pato_img, 'rect': pato_img.get_rect(center=(150, 500)), "velocidade": -1},
    {'image': pato_img, 'rect': pato_img.get_rect(center=(680, 450)), "velocidade": -3},
    {'image': pato_img, 'rect': pato_img.get_rect(center=(720, 530)), "velocidade": -1},
]

bala_disponivel = True

while True:
    cursor_img_rect.center = pygame.mouse.get_pos()

    DISPLAYSURF.blit(fundo, (0, 0))
    for pato in pato_posição:
        pato['rect'].move_ip(pato['velocidade'], 0)
        if pato['rect'].right < 0:
            pato['rect'].left = SCREEN_X
        DISPLAYSURF.blit(pato['image'], pato['rect'])

    DISPLAYSURF.blit(mira_img, cursor_img_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and bala_disponivel:
                mouse_pos = pygame.mouse.get_pos()
                for pato in pato_posição[:]:
                    if pato['rect'].collidepoint(mouse_pos):
                        pato_posição.remove(pato)
                som_tiro.play()
                bala_disponivel = False
            elif event.button == 3:
                som_recarga.play()
                bala_disponivel = True

    pygame.display.update()
    fpsClock.tick(FPS)

    if not pato_posição:
        pygame.quit()
        sys.exit()
