# -*- coding: utf-8 -*-

import os
import tempfile
import unittest
from unittest.mock import MagicMock
import cProfile

from pygame.tests.test_utils import png
import pygame.image, pygame.pkgdata
import pygame

class EssTest(unittest.TestCase):

    def test_surface_get_at(self):
        cyan_pixel = (0, 255, 255, 255)
        purple_pixel = (255, 0, 255, 255)
        yellow_pixel = (255, 255, 0, 255)
        green_pixel = (0, 255, 0, 255)
        pixel_array = [cyan_pixel + purple_pixel, yellow_pixel + green_pixel]

        surf = pygame.Surface((2, 2))

        surf.set_at((0, 0), cyan_pixel)
        surf.set_at((1, 0), purple_pixel)
        surf.set_at((0, 1), yellow_pixel)
        surf.set_at((1, 1), green_pixel)

        f_descriptor, f_path = tempfile.mkstemp(suffix=".bmp")

        with os.fdopen(f_descriptor, "wb") as f:
            w = png.Writer(2, 2, alpha=True)
            w.write(f, pixel_array)

        self.assertEqual(surf.get_at((0, 0)),
                         pygame.image.load(f_path).get_at((0, 0)))

        os.remove(f_path)

    def test_surface_set_at(self):
        cyan_pixel = (0, 255, 255, 255)

        surf = pygame.Surface((2, 2))

        surf.set_at((0, 0), cyan_pixel)
        self.assertEqual(surf.get_at((0, 0)),
                     cyan_pixel)


    def test_get_abs_parent_same(self):
        surf = pygame.Surface((2, 2))
        self.assertEqual(
                         surf,surf.get_abs_parent())

    def test_get_abs_parent_child(self):
        parent_surf = pygame.Surface((2, 2))
        child_surf = parent_surf.subsurface((1,1,1,1))

        self.assertEqual(
                         parent_surf,child_surf.get_abs_parent())

    def test_surface_fill(self):
        surf = pygame.Surface((2, 2))
        fill_color = (255,255,255,255)
        surf.fill(fill_color)
        self.assertEqual(surf.get_at((0,0)), fill_color)
        self.assertEqual(surf.get_at((0, 1)), fill_color)
        self.assertEqual(surf.get_at((1, 0)), fill_color)
        self.assertEqual(surf.get_at((1, 1)), fill_color)

    def test_surface_aplha(self):
        surf = pygame.Surface((2, 2))
        fill_color = (255, 255, 255, 255)
        surf.fill(fill_color)
        surf.set_alpha(150)
        self.assertEqual(150, surf.get_alpha())

    def test_surface_size(self):
        surf = pygame.Surface((2, 2))
        self.assertEqual((2,2), surf.get_size())
        self.assertEqual(2, surf.get_height())
        self.assertEqual(2, surf.get_width())


    def test_init_display(self):
        display = pygame.display.init()
        self.assertTrue(pygame.display.get_init())

    def test_display_set_caption(self):
        pygame.display.init()
        pygame.display.set_caption("Faketitle")
        self.assertEqual("Faketitle", "Faketitle", pygame.display.get_caption())

    def test_rect_copy(self):
        surf = pygame.Surface((2,2))
        color = (200,50,50,255)
        rect = pygame.draw.rect(surf, color, (1,1,1,1))
        self.assertEqual(rect, pygame.Rect.copy(rect))

    def test_mock_surf(self):
        surf = pygame.Surface((2, 2))
        mock_surf = MagicMock()
        fill_color = (255, 255, 255, 255)
        mock_surf.fill(fill_color)
        mock_surf.set_at((0, 0))
        self.assertTrue(mock_surf.set_at.called)

if __name__ == "__main__":
        unittest.main()
