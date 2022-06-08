import pygame


def vic_guard(p, p2):
    if p.pris:
        if p2[0].place == 19 and p2[1].place == 19 and p2[2].place == 19 and p2[3].place == 19:
            p.place = 19


def door_open(win, p, p2):
    if not p.pris and not p.hacker:
        if p2[6].escape:
            font = pygame.font.SysFont("comicsans", 100)
            text = font.render(str(p2[6].escape_time) + "/1000", 1, (255, 255, 255))
            win.blit(text, (980, 125))
    if not p.hacker:
        if p2[6].place == 19:
            p.place = 19


def alarm_vic(p, p2):
    if not p.pris and not p.hacker:
        if p.alarm or p2[0].alarm or p2[1].alarm or p2[2].alarm:
            if p2[3].place == 19 and p2[4].place == 19 and p2[5].place == 19:
                if p.sheriff and not p.place == 19:
                    p.y = 100
                p.place = 19
