import pygame


def screwdriver_vis(win, p, p2):
    if p.pris:
        if p.screwdriver or p2[4].screwdriver or p2[5].screwdriver:
            if p.screw_timer < 500:
                font = pygame.font.SysFont("comicsans", 100)
                text = font.render("Screwdriver obtained. The vents are open", 1, (255, 255, 255))
                win.blit(text, (100, 100))
                p.screw_timer += 1
            else:
                p.screw_timer = 501
