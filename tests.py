from pytc.testcase import TestCase, run_tests as run_tests

class AA(TestCase):
    pass

run_tests(TestCase.__subclasses__())