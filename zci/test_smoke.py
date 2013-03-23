from unittest import TestCase


class SmokeTests(TestCase):

    def test_dummy(self):
        # There are no other tests yet but let's make sure that testing works 
        self.assertEqual(2 + 2, 4)
