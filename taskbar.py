import pygame


def taskbar(win, keys, p, p2):
    font = pygame.font.SysFont("comicsans", 30)
    if p.pris:
        if keys[pygame.K_TAB]:
            pygame.draw.rect(win, (96, 96, 96), (0, 0, 250, 550))
            text = font.render(str(p2[6].time)[1:3] + ":00", 1, (255, 255, 255))
            win.blit(text, (100, 10))
            if 106000 < p2[6].time < 108000:
                if p.breakfast:
                    text = font.render("Lunch Time", 1, (0, 255, 0))
                    win.blit(text, (100, 110))
                else:
                    text = font.render("Lunch Time", 1, (255, 0, 0))
                    win.blit(text, (100, 110))
            elif 108000 < p2[6].time < 110000:
                text = font.render("Free Time", 1, (0, 255, 0))
                win.blit(text, (100, 110))
            elif 110000 < p2[6].time < 112000:
                if p.exercise:
                    text = font.render("Exercise time", 1, (0, 255, 0))
                    win.blit(text, (100, 110))
                else:
                    text = font.render("Exercise Time", 1, (255, 0, 0))
                    win.blit(text, (100, 110))
            elif 112000 < p2[6].time < 114000:
                if p.lunch:
                    text = font.render("Lunch Time", 1, (0, 255, 0))
                    win.blit(text, (100, 110))
                else:
                    text = font.render("Lunch Time", 1, (255, 0, 0))
                    win.blit(text, (100, 110))
            elif 114000 < p2[6].time < 117000:
                text = font.render("Free Time", 1, (0, 255, 0))
                win.blit(text, (100, 110))
            elif 117000 < p2[6].time < 119000:
                if p.exercise:
                    text = font.render("Exercise time", 1, (0, 255, 0))
                    win.blit(text, (100, 110))
                else:
                    text = font.render("Exercise Time", 1, (255, 0, 0))
                    win.blit(text, (100, 110))
            elif 119000 < p2[6].time < 121000:
                if p.dinner:
                    text = font.render("Dinner Time", 1, (0, 255, 0))
                    win.blit(text, (100, 110))
                else:
                    text = font.render("Dinner Time", 1, (255, 0, 0))
                    win.blit(text, (100, 110))
            elif 121000 < p2[6].time < 122000:
                if p.return_cell:
                    text = font.render("RETURN TO YOUR CELL", 1, (0, 255, 0))
                    win.blit(text, (100, 110))
                else:
                    text = font.render("RETURN TO YOUR CELL", 1, (255, 0, 0))
                    win.blit(text, (100, 110))
        if not (106000 < p2[6].time < 122000):
            p.breakfast, p.lunch, p.dinner, p.free_time, p.exercise, p.return_cell = False, False, False, False, False, False
            if 1600 < p.x < 1800:
                if 700 < p.y < 950:
                    p.sleep = True
        else:
            p.sleep = False
