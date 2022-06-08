def hide(p):
    if p.pris:
        if p.place == 4:
            if 1640 < p.x < 1880 and -40 < p.y < 140:
                p.hide = True
            else:
                p.hide = False
        elif p.place == 9:
            if -40 < p.x < 180 and -40 < p.y < 140:
                p.hide = True
            else:
                p.hide = False
        elif p.place == 13:
            if -40 < p.x < 180 and -40 < p.y < 140:
                p.hide = True
            else:
                p.hide = False
