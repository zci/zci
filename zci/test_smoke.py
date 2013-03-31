from __future__ import absolute_import, unicode_literals, print_function

"""
:mod:`zci.test_smoke` -- Smoke tests for ZCI
============================================
"""

from zci.compat import unittest


class SmokeTests(unittest.TestCase):

    def test_dummy(self):
        # There are no other tests yet but let's make sure that testing works 
        self.assertEqual(2 + 2, 4)
