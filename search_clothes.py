import pygame


def search(win, p, p2, keys):
    if p.pris:
        font = pygame.font.SysFont("comicsans", 30)
        if p2[2].change:
            if p2[2].original_place[0] - 200 < p.x < p2[2].original_place[0] + 200:
                if p2[2].original_place[1] - 200 < p.y < p2[2].original_place[1] + 200:
                    if p2[2].original_place[2] == p.place:
                        pygame.draw.rect(win, (0, 0, 255), (900, 150, 100, 30))
                        text = font.render("Press SPACE to reveal the code", 1, (255, 0, 0))
                        win.blit(text, (900, 120))
                        if keys[pygame.K_SPACE]:
                            p.cloth_bool_code = True
                        if p.cloth_bool_code:
                            text = font.render(str(p.cloth_code), 1, (255, 255, 255))
                            win.blit(text, (1850, 30))
