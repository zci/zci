from __future__ import absolute_import, unicode_literals, print_function

"""
:mod:`zci.tests` -- Helpers for internal testing
================================================
"""

import inspect
import os

import zci
from zci.compat import unittest


def _get_zci_dir():
    """
    Return the root directory of the zci package.
    """
    return os.path.dirname(inspect.getabsfile(zci))


def load_unit_tests():
    """
    Load all unit tests and return a TestSuite object

    Discover all unit tests. By simple convention those are kept in python
    modules that start with the word 'test_' .
    """
    return unittest.defaultTestLoader.discover(_get_zci_dir())


def test_suite():
    """
    Test suite function used by setuptools test loader.

    Uses unittest test discovery system to get a list of test cases defined
    inside zci. See setup.py setup(test_suite=...) for a matching entry
    """
    return load_unit_tests()
