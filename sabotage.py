import pygame


def sabotage_water(win, p, keys):
    pos = pygame.mouse.get_pos()
    p.fix = 0
    if 1650 < p.x < 1920:
        if 850 < p.y < 1080:
            pygame.draw.rect(win, (0, 0, 0), (280, 540, 100, 100))
            pygame.draw.rect(win, (255, 255, 0), (560, 540, 100, 100))
            pygame.draw.rect(win, (0, 78, 9), (840, 540, 100, 100))
            pygame.draw.rect(win, (123, 89, 9), (1120, 540, 100, 100))
            if 280 < pos[0] < 380:
                if 540 < pos[1] < 640:
                    if keys[pygame.K_SPACE]:
                        if p.pris:
                            p.sabotage = 1
                        if not p.pris and not p.hacker:
                            p.fix = 1
            if 560 < pos[0] < 660:
                if 540 < pos[1] < 640:
                    if keys[pygame.K_SPACE]:
                        if p.pris:
                            p.sabotage = 2
                        if not p.pris and not p.hacker:
                            p.fix = 2
            if 840 < pos[0] < 940:
                if 540 < pos[1] < 640:
                    if keys[pygame.K_SPACE]:
                        if p.pris:
                            p.sabotage = 3
                        if not p.pris and not p.hacker:
                            p.fix = 3
            if 1120 < pos[0] < 1220:
                if 540 < pos[1] < 640:
                    if keys[pygame.K_SPACE]:
                        if p.pris:
                            p.sabotage = 4
                        if not p.pris and not p.hacker:
                            p.fix = 4


def sab_fixing(win, p, p2, keys):
    font = pygame.font.SysFont("comicsans", 100)
    if p.pris:
        if p2[0].end_sab or p2[1].end_sab or p2[2].end_sab or p2[3].end_sab:
            p.sabotage = 0

    if not p.pris and not p.hacker:
        p.end_sab = False
        if p2[3].sabotage == 1 or p2[4].sabotage == 1 or p2[5].sabotage == 1:
            p.ongoing_sabotage = True
            if p.place == 0:
                pygame.draw.rect(win, (255, 0, 0), (700, 800, 700, 200))
        if p2[3].sabotage == 2 or p2[4].sabotage == 2 or p2[5].sabotage == 2:
            p.ongoing_sabotage = True
            if p.place == 4:
                pygame.draw.rect(win, (255, 0, 0), (700, 800, 700, 200))
        if p2[3].sabotage == 3 or p2[4].sabotage == 3 or p2[5].sabotage == 3:
            p.ongoing_sabotage = True
            if p.place == 10:
                pygame.draw.rect(win, (255, 0, 0), (700, 800, 700, 200))
        if p2[3].sabotage == 4 or p2[4].sabotage == 4 or p2[5].sabotage == 4:
            p.ongoing_sabotage = True
            if p.place == 14:
                pygame.draw.rect(win, (255, 0, 0), (700, 800, 700, 200))

        if p.ongoing_sabotage:
            text = font.render(str(p.fix_time) + "/3500", 1, (255, 0, 0))
            win.blit(text, (1550, 900))
            if p.place == 12:
                if p.fix != 0:
                    if p2[3].sabotage == p.fix or p2[4].sabotage == p.fix or p2[5].sabotage == p.fix:
                        print("Gud work")
                        p.fix_time = 0
                        p.end_sab = True
                        p.ongoing_sabotage = False
                    else:
                        p.place = 19
                        p.fix = 0
                        p.end_sab = True
                        p.ongoing_sabotage = False
                else:
                    sabotage_water(win, p, keys)
            if p.fix_time < 3000:
                p.fix_time += 1
            else:
                p.fix_time = 0
                p.place = 19
                p.fix = 0
                p.end_sab = True
                p.ongoing_sabotage = False
        # print(p.fix_time)
