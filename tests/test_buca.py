# -*- coding: UTF-8 -*-

import unittest
import buca as b

class TestWordReplacer(unittest.TestCase):
    def test_ratio0(self):
        text = "hello I'm some piece of text"
        self.assertEqual(text, b.WordReplacer(ratio=0).run(text))
        self.assertEqual(text, b.WordReplacer(ratio=1, max_count=0).run(text))
        self.assertEqual("_____ I'm ____ _____ __ ____",
                b.WordReplacer(ratio=1).run(text))
        self.assertEqual("(1) _____ I'm (2) ____ (3) _____ (4) __ (5) ____",
                b.WordReplacer(ratio=1, numbers=True).run(text))
        self.assertEqual("_____ I'm _____ _____ _____ _____",
                b.WordReplacer(ratio=1, fixed_size=True).run(text))
