DEBUG = False

def cambiar_modo():
    '''brief: cambia el modo(hitbox)'''
    global DEBUG
    DEBUG = not DEBUG

def get_modo():
    '''brief: si cambio el modo le digo que hacer(en mi caso mostrar hitbox)'''
    return DEBUG