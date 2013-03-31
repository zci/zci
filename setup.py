import sys

try:
    from setuptools import setup
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

if sys.version_info[0] == 3:
    tests_require = ["unittest2py3k"]
else:
    tests_require = ["unittest2"]

setup(
    setup_requires=['d2to1'],
    d2to1=True,
    # This is unsupported by d2to1
    test_suite="zci.tests.test_suite",
    tests_require=tests_require,
    use_2to3=True,
    zip_safe=True,
)
