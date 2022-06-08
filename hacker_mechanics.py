import pygame


def hacker_mech(win, p, box, p2):
    if p.place == 17 and not p.cam:
        p.start = True
        font = pygame.font.SysFont("comicsans", 100)
        win.fill((0, 0, 0))
        if p.hacks < 1:
            if not p2[1].e_sabotage:
                if box.text == "doors.close(cams)":
                    p.cam_door = False
                    p.hacks = 1
                if box.text == "doors.close(storage)":
                    p.storage_door = False
                    p.hacks = 1
                if box.text == "doors.close(mid)":
                    p.mid_door = False
                    p.hacks = 1
                if box.text == "cams.off()":
                    p.camera_vision = False
                    p.camera_vision_num = 1
                    p.hacks = 1
                if box.text == "open_cells == True":
                    p.jail_door = True
                    p.hacks = 1
                if box.text == "guard.loc(show)":
                    p.locations = True
                    p.hacks = 1
                if box.text == str(p2[4].stor_code) + str(p2[5].stor_code) + str(p2[6].stor_code):
                    p.stor_lock = True
                if box.text == str(p2[4].cloth_code) or box.text == str(p2[5].cloth_code)\
                        or box.text == str(p2[6].cloth_code):
                    p.disable_alarm = True
            else:
                print("Sabotage")
        elif 1 <= p.hacks < 2500:
            p.hacks += 1
            text = font.render(str(p.hacks) + "/2500", 1, (255, 255, 255))
            win.blit(text, (1550, 125))
        else:
            p.hacks = 0
        box.update()
        if not p.escape:
            if box.text == "jail.escape()":
                p.escape = True

        if not p.cam_door:
            if p.cam_num < 1000:
                p.cam_num += 1
            else:
                p.cam_door = True
                p.cam_num = 0

        if not p.storage_door:
            if p.stor_num < 1000:
                p.stor_num += 1
            else:
                p.storage_door = True
                p.stor_num = 0

        if not p.mid_door:
            if p.mid_num < 1000:
                p.mid_num += 1
            else:
                p.mid_door = True
                p.mid_num = 0

        if p.jail_door:
            if p.cell_num < 1000:
                p.cell_num += 1
            else:
                p.jail_door = False
                p.jail_cell = 0

        if 1 <= p.camera_vision_num < 1000:
            p.camera_vision_num += 1
        else:
            p.camera_vision = True
            p.camera_vision_num = 0

        if p.escape:
            if p.escape_time < 1000:
                p.escape_time += 1
            else:
                p.place = 19
                p.escape = False

        if p.locations:
            text = font.render(("|" + str(p2[0].place) + "|") + (str(p2[1].place) + "|") +
                               (str(p2[2].place) + "|") + (str(p2[3].place) + "|"), 1, (255, 255, 255))
            win.blit(text, (500, 540))
            if p.show_loc < 500:
                p.show_loc += 1
            else:
                p.show_loc = 0
                p.locations = False

        # time rendering
        if p.start:
            if p.time < 124000:
                if not p2[4].sleep or not p2[5].sleep or not p2[6].sleep:
                    p.time += 1
                else:
                    p.time += 10
                print(str(p.time)[1:3], str(p.time)[3:5])
            else:
                p.time = 100000
