# -*- coding: utf-8 -*-

import cProfile
import pygame.image, pygame.pkgdata
import pygame
import os
import tempfile
from pygame.tests.test_utils import png

def profile_function():

    surf = pygame.Surface((2, 2))

    surf.set_at((0, 0), (0, 255, 255, 255))

    surf.fill((0, 0, 255, 255))

    surf.subsurface((1, 1, 1, 1))

    surf.get_at((0, 0))

    rect = pygame.draw.rect(surf, (0, 255, 255, 255), (1, 1, 1, 1))

    pygame.Rect.copy(rect)


    #DISPLAY
    dis = pygame.display.init()
    pygame.display.get_init()
    pygame.display.set_caption("FakeCaption")
    pygame.display.set_mode(size=(0, 0), flags=0, depth=0, display=0)
    pygame.display.get_surface()
    pygame.display.flip()
    pygame.display.update()
    pygame.display.get_driver()
    pygame.display.Info()
    pygame.display.get_wm_info()
    pygame.display.list_modes()
    pygame.display.mode_ok(size=(0,0), flags=0, depth=0, display=0)
    pygame.display.gl_set_attribute(1, 1)
    pygame.display.gl_get_attribute(1)
    pygame.display.get_active()
    pygame.display.iconify()
    pygame.display.toggle_fullscreen()


    #DRAW
    rect = pygame.draw.rect(surf, (0, 255, 255, 255), (1, 1, 1, 1))
    poly = pygame.draw.polygon(surf, (0, 255, 255, 255), ((1, 1), (0, 0)), 1)
    aaline = pygame.draw.aaline(surf, (0, 255, 255, 255), (0, 0), (1, 1))

    #EVENT
    event = pygame.event.Event
    pygame.event.pump()
    pygame.event.get()
    pygame.event.poll()
    pygame.event.peek()
    pygame.event.clear()
    pygame.event.get_grab()
    pygame.event.peek()
    pygame.event.poll()

    #IMAGE

    pygame.display.quit()






if __name__ == '__main__':
    cProfile.run("profile_function()")
