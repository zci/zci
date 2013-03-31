from __future__ import absolute_import, unicode_literals, print_function

"""
:mod:`zci.compat` -- Compatibility code for python2.6 and python2.7
===================================================================
"""

try:
    import unittest.loader  # pragma: no cover
except ImportError:
    import unittest2 as unittest # pragma: no cover
else:
    import unittest # pragma: no cover

__all__ = ["unittest"]