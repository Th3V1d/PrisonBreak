import pygame
import random
pygame.font.init()


class Guard(object):
    def __init__(self, x, y, width, height, color, sheriff=False, engineer=False, changer=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.color = color
        # update rectangle
        self.rectangle = (self.x, self.y, self.width, self.height)
        # data for the rooms
        self.place = 0
        # data for identity
        self.hacker = False
        self.pris = False
        # restart
        self.restart = False
        # data for cam system
        self.cam = False
        self.cam_place = 0
        # data for arresting system
        self.caught1 = False
        self.caught2 = False
        self.caught3 = False
        # data for water sabotaging
        self.fix = 0
        self.fix_time = 0
        self.ongoing_sabotage = False
        self.end_sab = False
        # data for engineer
        self.engineer = engineer
        self.e_sab_timer = 0
        self.e_timer = 0
        self.e_sabotage = False
        self.e_cooldown = False
        # data for sheriff
        self.sheriff = sheriff
        self.slow1 = False
        self.slow2 = False
        self.slow3 = False
        # data for changer
        self.changer = changer
        self.change_timer = 0
        self.change_cooldown = 0
        self.change = False
        self.original_place = None
        # data for the alarm
        self.alarm_cooldown = 0
        self.alarm_timer = 0
        self.alarm = False
        # dumb data for hiding prisoners
        self.hide = False
        # dumb data for pris debuff
        self.glasses = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rectangle)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.vel
        elif keys[pygame.K_s] and self.y < (1080 - self.height):
            self.y += self.vel
        elif keys[pygame.K_a] and self.x > 0:
            self.x -= self.vel
        elif keys[pygame.K_d] and self.x < (1920 - self.width):
            self.x += self.vel

        self.update()

    def e_sab(self, keys, win):
        if keys[pygame.K_e] and not self.e_cooldown:
            self.e_sabotage = True
        if self.e_sabotage:
            font = pygame.font.SysFont("comicsans", 100)
            text = font.render(str(self.e_sab_timer) + "/2000", 1, (255, 255, 255))
            win.blit(text, (1550, 125))
            if self.e_sab_timer < 2000:
                self.e_sab_timer += 1
            else:
                self.e_sab_timer = 0
                self.e_cooldown = True
                self.e_sabotage = False

        if self.e_cooldown:
            if self.e_timer < 3000:
                self.e_timer += 1
            else:
                self.e_timer = 0
                self.e_cooldown = False

    def pris_guard(self, keys, win):
        if self.changer:
            if self.change_cooldown < 3000:
                self.change_cooldown += 1
            else:
                if keys[pygame.K_e]:
                    self.original_place = (self.x, self.y, self.place)
                    self.change = True
            if self.change:
                if self.change_timer < 2000:
                    try:
                        pygame.draw.rect(win, (255, 255, 255), (self.original_place[0], self.original_place[1], 100, 100))
                    except UnboundLocalError:
                        pass
                    self.color = (0, 255, 0)
                    self.change_timer += 1
                else:
                    self.color = (255, 0, 0)
                    self.change_timer = 0
                    self.change_cooldown = 0
                    self.change = False

    def update(self):
        self.rectangle = (self.x, self.y, self.width, self.height)


class Prisoner(object):
    pris_img = pygame.image.load("images/pb_prisoner.png")

    def __init__(self, x, y, width, height, color, place, num, handcuffed=False, glasses=False, claustrophobic=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.color = color
        self.rectangle = (self.x, self.y, self.width, self.height)
        self.place = place
        self.num = num
        self.hacker = False
        self.pris = True
        # cams
        self.cam = False
        self.cam_place = 0
        self.camera_vision = None
        # sabotage
        self.sabotage = 0
        # screwdriver
        self.screwdriver = False
        self.screw_timer = 0
        # codes
        self.stor_code = random.randint(1, 100000)
        self.cloth_code = random.randint(1, 100000)
        self.cloth_bool_code = False
        # chests
        self.hide = False
        # handcuffed debuff
        self.handcuffed = handcuffed
        self.moving_timer = 0
        self.moving = False
        # glasses debuff
        self.glasses = glasses
        # claustrophobic debuff
        self.claustrophobic = claustrophobic
        # dumb data for starting
        self.start = True
        # tasks
        self.dinner = False
        self.lunch = False
        self.exercise = False
        self.free_time = False
        self.sleep = False
        self.return_cell = False
        self.breakfast = False

    def draw(self, win):
        win.blit(self.pris_img, self.rectangle)

    def move(self):
        keys = pygame.key.get_pressed()
        # moving for the claustrophobic
        if self.claustrophobic:
            self.vel = 8
        if not self.handcuffed:
            if keys[pygame.K_w] and self.y > 0:
                self.y -= self.vel
            elif keys[pygame.K_s] and self.y < (1080 - self.height):
                self.y += self.vel
            elif keys[pygame.K_a] and self.x > 0:
                self.x -= self.vel
            elif keys[pygame.K_d] and self.x < (1920 - self.width):
                self.x += self.vel
        else:
            self.cuffed_move()

        self.update()

    def cuffed_move(self):
        def crouching():
            if keys[pygame.K_LSHIFT]:
                self.moving = False
                self.moving_timer = False
                self.vel = 4
            else:
                self.vel = 7


        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.y > 0:
            crouching()
            self.y -= self.vel
        elif keys[pygame.K_s] and self.y < (1080 - self.height):
            crouching()
            self.y += self.vel
        elif keys[pygame.K_a] and self.x > 0:
            crouching()
            self.x -= self.vel
        elif keys[pygame.K_d] and self.x < (1920 - self.width):
            crouching()
            self.x += self.vel

        if (keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_w] or keys[pygame.K_d]) == 1:
            if self.moving_timer < 30:
                self.moving_timer += 1
                self.moving = False
            else:
                self.moving = True
                self.moving_timer = 0

    def update(self):
        self.rectangle = (self.x, self.y, self.width, self.height)


class Hacker(object):
    def __init__(self):
        self.x = 500
        self.y = 500
        self.width = 0
        self.height = 0
        self.hacker = True
        self.pris = False
        self.place = 17
        self.cam_door = True
        self.storage_door = True
        self.mid_door = True
        self.jail_door = False
        self.cam = False
        self.cam_place = 0
        self.escape = False
        self.escape_time = 0
        self.cam_num = 0
        self.stor_num = 0
        self.mid_num = 0
        self.cell_num = 0
        self.hacks = 0
        self.camera_vision = True
        self.camera_vision_num = 0
        self.locations = False
        self.show_loc = 0
        self.stor_lock = False
        self.disable_alarm = False
        self.glasses = False
        self.start = False
        # time
        self.time = 100000

    def move(self):
        pass

    def draw(self, win):
        pass

    def update(self):
        pass
