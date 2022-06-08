import pygame


def camera(p, keys, p2):
    if p.place == 21 or p.hacker:
        if (800 < p.x < 1300) or p.hacker:
            if (280 < p.y < 380) or p.hacker:
                if p2[6].camera_vision or p.hacker:
                    if keys[pygame.K_1]:
                        p.cam_place = 1
                        p.cam = True
                    if keys[pygame.K_2]:
                        p.cam_place = 6
                        p.cam = True
                    if keys[pygame.K_3]:
                        p.cam_place = 7
                        p.cam = True
                    if keys[pygame.K_4]:
                        p.cam_place = 11
                        p.cam = True
                    if keys[pygame.K_ESCAPE]:
                        p.cam_place = 0
                        p.cam = False
