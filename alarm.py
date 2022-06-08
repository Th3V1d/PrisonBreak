import pygame


def trigger_alarm(win, p, p2, keys):
    font1 = pygame.font.SysFont("comicsans", 30)
    font2 = pygame.font.SysFont("comicsans", 100)
    print(p2[6].disable_alarm)
    pygame.draw.rect(win, (255, 255, 255), (910, 100, 100, 100))
    if not p.pris and not p.hacker:
        p.restart = False
        text = font1.render(str(p.alarm_cooldown) + "/6000", 1, (255, 255, 255))
        win.blit(text, (925, 200))
        if 710 < p.x < 1110:
            if -100 < p.y < 300:
                if not p.alarm:
                    text = font2.render("Press P to alarm", 1, (0, 255, 0))
                    win.blit(text, (820, 920))
                if keys[pygame.K_p]:
                    if p.alarm_cooldown == 0:
                        if not p2[6].disable_alarm:
                            p.alarm = True


def action_alarm(win, p, p2):
    font2 = pygame.font.SysFont("comicsans", 100)
    if not p.pris and not p.hacker:
        if p.alarm or p2[0].alarm or p2[1].alarm or p2[2].alarm:
            if p.alarm_timer < 2500:
                p.alarm_timer += 1
            else:
                p.alarm_timer = 0
                p.alarm = False
                p.alarm_cooldown = 1
        else:
            if 1 <= p.alarm_cooldown < 6000:
                p.alarm_cooldown += 1
            else:
                p.alarm_cooldown = 0
    if p.pris:
        if p2[0].alarm or p2[1].alarm or p2[2].alarm or p2[3].alarm:
            text = font2.render("THE ALARM IS TRIGGERED", 1, (255, 0, 0))
            win.blit(text, (925, 200))
