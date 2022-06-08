def moving(p, p2, sound):
    if not p.pris and not p.hacker:
        if p2[3].moving and p2[3].place == p.place:
            sound.play()
