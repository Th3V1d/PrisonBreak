import pygame
from network import Network
from hacker_text import InputBox
from cams import camera
from arrest import arresting
from sabotage import sabotage_water, sab_fixing
from hacker_mechanics import hacker_mech
from victory import vic_guard, door_open, alarm_vic
from screwdriver import screwdriver_vis
from alarm import trigger_alarm, action_alarm
from search_clothes import search
from chests import hide
from pris_debuffs import moving
from minimap import mini
from taskbar import taskbar

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Client")
pygame.font.init()
pygame.mixer.init()


def redrawWindow(win, player, other_player, box):
    if not player.cam and not player.hacker:
        if not player.hide:
            player.draw(win)

    if player.pris:
        if other_player[2].change:
            if player.place == other_player[2].original_place[2]:
                pygame.draw.rect(win, (255, 255, 255),
                                 (other_player[2].original_place[0], other_player[2].original_place[1], 100, 100))

    if not player.cam:
        if not player.glasses:
            if player.place == other_player[0].place:
                other_player[0].draw(win)
            if player.place == other_player[1].place:
                other_player[1].draw(win)
            if player.place == other_player[2].place:
                other_player[2].draw(win)
            if not player.pris:
                if (player.place == other_player[3].place) and (player.x - 500 < other_player[3].x < player.x + 500) \
                        and (player.y - 500 < other_player[3].y < player.y + 500) and not other_player[3].hide:
                    other_player[3].draw(win)
                if (player.place == other_player[4].place) and (player.x - 500 < other_player[4].x < player.x + 500) \
                        and (player.y - 500 < other_player[4].y < player.y + 500) and not other_player[4].hide:
                    other_player[4].draw(win)
                if (player.place == other_player[5].place) and (player.x - 500 < other_player[5].x < player.x + 500) \
                        and (player.y - 500 < other_player[5].y < player.y + 500) and not other_player[5].hide:
                    other_player[5].draw(win)
            else:
                if player.place == other_player[3].place:
                    other_player[3].draw(win)
                if player.place == other_player[4].place:
                    other_player[4].draw(win)
                if player.place == other_player[5].place:
                    other_player[5].draw(win)
        else:
            if (player.place == other_player[0].place) and (player.x - 600 < other_player[0].x < player.x + 600) \
                    and (player.y - 600 < other_player[0].y < player.y + 600):
                other_player[0].draw(win)
            if (player.place == other_player[1].place) and (player.x - 600 < other_player[1].x < player.x + 600) \
                    and (player.y - 600 < other_player[1].y < player.y + 600):
                other_player[1].draw(win)
            if (player.place == other_player[2].place) and (player.x - 600 < other_player[2].x < player.x + 600) \
                    and (player.y - 600 < other_player[2].y < player.y + 600):
                other_player[2].draw(win)
            if (player.place == other_player[3].place) and (player.x - 600 < other_player[3].x < player.x + 600) \
                    and (player.y - 600 < other_player[3].y < player.y + 600):
                other_player[3].draw(win)
            if (player.place == other_player[4].place) and (player.x - 600 < other_player[4].x < player.x + 600) \
                    and (player.y - 600 < other_player[4].y < player.y + 600):
                other_player[4].draw(win)
            if (player.place == other_player[5].place) and (player.x - 600 < other_player[5].x < player.x + 600) \
                    and (player.y - 600 < other_player[5].y < player.y + 600):
                other_player[5].draw(win)

    if player.cam:
        if player.cam_place == other_player[0].place:
            other_player[0].draw(win)
        if player.cam_place == other_player[1].place:
            other_player[1].draw(win)
        if player.cam_place == other_player[2].place:
            other_player[2].draw(win)
        if player.cam_place == other_player[3].place:
            other_player[3].draw(win)
        if player.cam_place == other_player[4].place:
            other_player[4].draw(win)
        if player.cam_place == other_player[5].place:
            other_player[5].draw(win)

    if player.place == 17 and not player.cam:
        box.draw(win)

    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    box = InputBox(0, 1000, 2000, 50)
    font = pygame.font.SysFont("comicsans", 30)
    handcuffedSound = pygame.mixer.Sound("images/download.wav")
    room1 = pygame.image.load("images/room1.png")
    minimap = pygame.image.load("images/minimap.png")
    while run:
        clock.tick(60)
        p2 = n.send(p)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            box.handle_event(event)

            #       Room mechanincs     #
        if p.place == 0:
            win.fill((0, 0, 0))
            trigger_alarm(win, p, p2, keys)
            pygame.draw.rect(win, (0, 255, 0), (10, 10, 150, 10))
            if p.pris:
                text = font.render(str(p.stor_code), 1, (255, 0, 0))
                win.blit(text, (1800, 60))
            if p.y > 1080 - p.height - 2:
                p.y = 3
                p.place = 1
        if p.place == 1 or p.cam_place == 1:
            win.fill((0, 0, 255))
            if p.y < 1:
                p.y = (1080 - p.height) - 2
                p.place = 0
            elif p.x > 1920 - p.width - 2:
                p.x = 3
                p.place = 2
            if not p.hacker:
                if p2[6].escape:
                    if p.pris:
                        if p.x < 1:
                            p.place = 19
        if p.place == 2:
            win.fill((0, 123, 166))
            pygame.draw.rect(win, (122, 122, 122), (1700, 100, 200, 200))
            pygame.draw.rect(win, (0, 0, 0), (960, 0, 50, 10))
            if p.pris:
                if p.screwdriver:
                    if not p.claustrophobic:
                        if 1600 < p.x < 1900:
                            if 0 < p.y < 300:
                                p.place = 6
                                p.x, p.y = 500, 150
            if p.x < 1:
                p.x = 1920 - p.width - 2
                p.place = 1
            elif p.y > 1080 - p.height - 2:
                p.y = 3
                p.place = 3
        if p.place == 3:
            win.fill((0, 123, 123))
            if p.y < 1:
                p.y = 1080 - p.height - 2
                p.place = 2
            elif p.y > 1080 - p.height - 2:
                p.y = 3
                p.place = 5
            elif p.x > 1920 - p.width - 2:
                if p2[6].cam_door:
                    p.x = 3
                    p.place = 4
        if p.place == 4:
            win.fill((255, 255, 0))
            pygame.draw.rect(win, (191, 111, 2), (1740, 40, 140, 100))
            if p.x < 1:
                if p2[6].cam_door:
                    p.x = 1920 - p.width - 2
                    p.place = 3
        if p.place == 5:
            win.fill((0, 255, 255))
            if p.y < 1:
                p.y = 1080 - p.height - 2
                p.place = 3
            elif p.x < 1:
                if p2[6].storage_door and (p2[6].stor_lock or (not p.pris and not p.hacker)):
                    p.x = 1920 - p.width - 2
                    p.place = 6
            elif p.x > 1920 - p.width - 2:
                p.x = 3
                p.place = 7
        if p.place == 6 or p.cam_place == 6:
            win.fill((255, 0, 255))
            pygame.draw.rect(win, (122, 122, 122), (500, 300, 200, 200))
            pygame.draw.rect(win, (191, 111, 2), (40, 40, 140, 100))
            pygame.draw.rect(win, (0, 0, 0), (960, 0, 50, 10))
            if p.glasses:
                p.glasses = False
            if p.pris:
                p.screwdriver = True
                if p.screwdriver:
                    if not p.claustrophobic:
                        if 400 < p.x < 700:
                            if 200 < p.y < 500:
                                p.place = 11
                                p.x, p.y = 1700, 400
            if p.x > 1920 - p.width - 2:
                if p2[6].storage_door:
                    p.x = 3
                    p.place = 5
        if p.place == 7 or p.cam_place == 7:
            win.fill((255, 255, 255))
            if p.x < 1:
                p.x = 1920 - p.width - 2
                p.place = 5
            elif p.y > 1080 - p.height - 2:
                if p2[6].mid_door:
                    p.y = 3
                    p.place = 8
        if p.place == 8:
            win.fill((124, 9, 17))
            if p.y < 1:
                if p2[6].mid_door:
                    p.y = 1080 - p.height - 2
                    p.place = 7
            elif p.x < 1:
                p.x = 1920 - p.width - 2
                p.place = 9
            elif p.y > 1080 - p.height - 2:
                p.y = 3
                p.place = 11
            elif p.x > 1920 - p.width - 2:
                p.x = 3
                p.place = 18
        if p.place == 9:
            win.fill((0, 89, 200))
            pygame.draw.rect(win, (12, 12, 12), (1700, 100, 200, 200))
            pygame.draw.rect(win, (191, 111, 2), (40, 40, 140, 100))
            if p.pris:
                if p.screwdriver:
                    if not p.claustrophobic:
                        if 1600 < p.x < 1900:
                            if 0 < p.y < 300:
                                p.place = 6
                                p.x, p.y = 500, 600
            if p.x > 1920 - p.width - 2:
                p.x = 3
                p.place = 8
            elif p.x < 1:
                p.x = 1920 - p.width - 2
                p.place = 10
        if p.place == 10:
            win.fill((0, 78, 9))
            pygame.draw.rect(win, (0, 0, 0), (960, 0, 50, 10))
            if p.x > 1920 - p.width - 2:
                p.x = 3
                p.place = 9
        if p.place == 11 or p.cam_place == 11:
            win.fill((200, 200, 200))
            pygame.draw.rect(win, (122, 122, 122), (1700, 100, 200, 200))
            if p.pris:
                if p.screwdriver:
                    if not p.claustrophobic:
                        if 1600 < p.x < 1900:
                            if 0 < p.y < 300:
                                p.place = 9
                                p.x, p.y = 1700, 350
            if p.y < 1:
                p.y = 1080 - p.height - 2
                p.place = 8
            elif p.y > 1080 - p.height - 2:
                p.y = 3
                p.place = 12
        if p.place == 12:
            win.fill((0, 7, 255))
            pygame.draw.rect(win, (0, 0, 0), (1800, 980, 100, 150))
            if p.y < 1:
                p.y = 1080 - p.height - 2
                p.place = 11
            elif p.x < 1:
                p.x = 1920 - p.width - 2
                p.place = 13
            elif p.x > 1920 - p.width - 2:
                p.x = 3
                p.place = 24
            sabotage_water(win, p, keys)
        if p.place == 13:
            win.fill((78, 27, 128))
            pygame.draw.rect(win, (191, 111, 2), (40, 40, 140, 100))
            if p.x > 1920 - p.width - 2:
                p.x = 3
                p.place = 12
            elif p.y > 1080 - p.height - 2:
                if p2[6].jail_door or not p.pris:
                    p.y = 3
                    p.place = 16
            elif p.x < 1:
                p.x = 1920 - p.width - 2
                p.place = 14
            elif p.y < 1:
                p.y = 1080 - p.height - 2
                p.place = 25
        if p.place == 14:
            win.blit(room1, (0, 0))
            pygame.draw.rect(win, (0, 0, 0), (960, 0, 50, 10))
            if p.y > 1080 - p.height - 2:
                if p2[6].jail_door or not p.pris:
                    p.y = 3
                    p.place = 15
            elif p.x > 1920 - p.width - 2:
                p.x = 3
                p.place = 13
            elif p.x < 1:
                p.x = 1920 - p.width - 2
                p.place = 23

        # pris1 cell start #
        if p.place == 15:
            win.fill((29, 0, 193))
            pygame.draw.rect(win, (255, 0, 0), (1700, 800, 100, 150))
            pygame.draw.rect(win, (255, 255, 255), (1700, 950, 100, 50))
            if p.y < 1:
                if p2[6].jail_door or not p.pris:
                    p.y = 1080 - p.height - 2
                    p.place = 14
        # pris1 cell end #

        # pris2 cell start #
        if p.place == 16:
            win.fill((12, 89, 90))
            pygame.draw.rect(win, (255, 0, 0), (1700, 800, 100, 150))
            pygame.draw.rect(win, (255, 255, 255), (1700, 950, 100, 50))
            if p.y < 1:
                if p2[6].jail_door or not p.pris:
                    p.y = 1080 - p.height - 2
                    p.place = 13
        # pris2 cell end #

        # 17 is for hackerman
        if p.place == 25:
            win.fill((43, 0, 0))
            if p.pris:
                if (106000 < p2[6].time < 108000) or (119000 < p2[6].time < 121000):
                    p.breakfast, p.lunch, p.dinner = True, True, True
                else:
                    p.breakfast, p.lunch, p.dinner = False, False, False
            if p.y > 1080 - p.height - 2:
                p.y = 3
                p.place = 13
        if p.place == 18:
            win.fill((69, 169, 96))
            if p.x < 1:
                p.x = 1920 - p.width - 2
                p.place = 8
            elif p.x > 1920 - p.width - 2:
                p.x = 3
                p.place = 20
        if p.place == 20:
            win.fill((34, 67, 200))
            if p.x < 1:
                p.x = 1920 - p.width - 2
                p.place = 18
            elif p.y < 1:
                p.y = 1080 - p.height - 2
                p.place = 21
            elif p.y > 1080 - p.height - 2:
                p.y = 3
                p.place = 22
        if p.place == 21 and not p.cam:
            win.fill((23, 56, 182))
            pygame.draw.rect(win, (30, 27, 239), (800, 160, 500, 120))
            if p.y > 1080 - p.height - 2:
                p.y = 3
                p.place = 20
        if p.place == 22:
            win.fill((3, 7, 11))
            if p.y < 1:
                p.y = 1080 - p.height - 2
                p.place = 20

        # pris3 cell start #
        if p.place == 23:
            win.fill((4, 20, 42))
            pygame.draw.rect(win, (255, 0, 0), (1700, 800, 100, 150))
            pygame.draw.rect(win, (255, 255, 255), (1700, 950, 100, 50))
            if p.x > 1920 - p.width - 2:
                p.x = 1
                p.place = 14
        # pris3 cell end #

        if p.place == 24:
            win.fill((123, 44, 5))
            if p.pris:
                if 110000 < p2[6].time < 112000:
                    p.exercise = True
                else:
                    p.exercise = False
            if p.x < 1:
                p.x = 1920 - p.width - 2
                p.place = 12

        # 19 is the lobby screen
        if p.place == 19:
            win.fill((0, 0, 0))
            if not p.pris and not p.hacker:
                if p.sheriff:
                    pygame.draw.rect(win, (255, 255, 255), (600, 599, 122, 122))
                    if p2[0].place == 19 and p2[1].place == 19 and p2[2].place == 19 and p2[3].place == 19 and \
                            p2[4].place == 19 and p2[5].place == 19 and p2[6].place == 19:
                        if p.y > 800:
                            p.restart = True
                            p.place, p.cam, p.cam_place, p.caught1, p.caught2, p.caught3, p.alarm, p.alarm_cooldown, p.alarm_timer = 0, False, 0, False, False, False, False, 0, 0
                else:
                    if p2[0].place == 0:
                        p.place, p.cam, p.cam_place, p.caught1, p.caught2, p.caught3 = 0, False, 0, False, False, False
            elif p.pris:
                if p2[0].place == 0 and p2[0].restart:
                    if p.num == 1:
                        p.place = 10
                    elif p.num == 2:
                        p.place = 15
                    elif p.num == 3:
                        p.place = 16
                    p.sabotage, p.screwdriver = 0, False
            if p.hacker:
                if p2[0].place == 0:
                    p.place = 17

        if not p.hacker:
            mini(win, minimap, p)
        if p2[6].start:
            camera(p, keys, p2)
            hacker_mech(win, p, box, p2)
            arresting(p, p2, keys)
            sab_fixing(win, p, p2, keys)
            vic_guard(p, p2)
            door_open(win, p, p2)
            screwdriver_vis(win, p, p2)
            action_alarm(win, p, p2)
            search(win, p, p2, keys)
            hide(p)
            moving(p, p2, handcuffedSound)
            alarm_vic(p, p2)
            taskbar(win, keys, p, p2)
        if not p.pris and not p.hacker:
            p.pris_guard(keys, win)
            if p.engineer:
                p.e_sab(keys, win)
        if not p.cam:
            p.move()
        print(p.y)
        redrawWindow(win, p, p2, box)

main()
