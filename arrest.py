import pygame


def arresting(p, p2, keys):
    if not p.pris:
        p.caught1 = False
        p.caught2 = False
        p.caught3 = False
        if p.place == p2[3].place and not p2[3].hide:
            if p.x - 250 < p2[3].x < p.x + 250:
                if p.y - 250 < p2[3].y < p.y + 250:
                    if keys[pygame.K_SPACE]:
                        p.caught1 = True
                        if p.sheriff and not p.slow1 and not p.slow2 and not p.slow3:
                            p.slow1 = True
        if p.place == p2[4].place and not p2[4].hide:
            if p.x - 250 < p2[4].x < p.x + 250:
                if p.y - 250 < p2[4].y < p.y + 250:
                    if keys[pygame.K_SPACE]:
                        p.caught2 = True
                        if p.sheriff and not p.slow1 and not p.slow2 and not p.slow3:
                            p.slow2 = True
        if p.place == p2[5].place and not p2[5].hide:
            if p.x - 250 < p2[5].x < p.x + 250:
                if p.y - 250 < p2[5].y < p.y + 250:
                    if keys[pygame.K_SPACE]:
                        p.caught3 = True
                        if p.sheriff and not p.slow1 and not p.slow2 and not p.slow3:
                            p.slow3 = True

    if p.pris:
        if p.num == 1:
            if p2[0].caught1 or p2[1].caught1 or p2[2].caught1 or p2[3].caught1:
                p.place = 10
                if (p2[0].alarm or p2[1].alarm or p2[2].alarm or p2[3].alarm) and not p2[3].place == 10:
                    p.place = 19
        if p.num == 2:
            if p2[0].caught2 or p2[1].caught2 or p2[2].caught2 or p2[3].caught2:
                p.place = 15
                if (p2[0].alarm or p2[1].alarm or p2[2].alarm or p2[3].alarm) and not p2[4].place == 15:
                    p.place = 19
        if p.num == 3:
            if p2[0].caught3 or p2[1].caught3 or p2[2].caught3 or p2[3].caught3:
                p.place = 16
                if (p2[0].alarm or p2[1].alarm or p2[2].alarm or p2[3].alarm) and not p2[5].place == 16:
                    p.place = 19
        if p2[0].slow1 and p.num == 1:
            p.vel = 6
        if p2[0].slow2 and p.num == 2:
            p.vel = 6
        if p2[0].slow3 and p.num == 3:
            p.vel = 6
