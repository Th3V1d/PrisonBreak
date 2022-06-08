import pygame


def minimap_rendering(win, p, x, y):
    if not p.pris:
        pygame.draw.rect(win, (255, 0, 0), (x, y, 10, 10))
    else:
        pygame.draw.rect(win, (0, 255, 0), (x, y, 10, 10))


def mini(win, minimap, p):
    win.blit(minimap, (0, 0))
    if p.place == 0:
        minimap_rendering(win, p, 75, 20)
    if p.place == 1:
        minimap_rendering(win, p, 75, 55)
    if p.place == 2:
        minimap_rendering(win, p, 110, 55)
    if p.place == 3:
        minimap_rendering(win, p, 110, 90)
    if p.place == 4:
        minimap_rendering(win, p, 145, 90)
    if p.place == 5:
        minimap_rendering(win, p, 110, 125)
    if p.place == 6:
        minimap_rendering(win, p, 75, 125)
    if p.place == 7:
        minimap_rendering(win, p, 145, 125)
    if p.place == 8:
        minimap_rendering(win, p, 145, 160)
    if p.place == 9:
        minimap_rendering(win, p, 110, 160)
    if p.place == 10:
        minimap_rendering(win, p, 75, 160)
    if p.place == 11:
        minimap_rendering(win, p, 145, 195)
    if p.place == 12:
        minimap_rendering(win, p, 145, 230)
    if p.place == 13:
        minimap_rendering(win, p, 110, 230)
    if p.place == 14:
        minimap_rendering(win, p, 75, 230)
    if p.place == 15:
        minimap_rendering(win, p, 75, 265)
    if p.place == 16:
        minimap_rendering(win, p, 110, 265)
    if p.place == 18:
        minimap_rendering(win, p, 180, 160)
    if p.place == 20:
        minimap_rendering(win, p, 215, 160)
    if p.place == 21:
        minimap_rendering(win, p, 215, 125)
    if p.place == 22:
        minimap_rendering(win, p, 215, 195)
    if p.place == 23:
        minimap_rendering(win, p, 40, 230)
    if p.place == 24:
        minimap_rendering(win, p, 180, 230)
    if p.place == 25:
        minimap_rendering(win, p, 110, 195)
