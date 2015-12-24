from pytc.testcase import TestCase, run_tests

class MyFirstTestCase(TestCase):
    enabled = True
    description = "This is a basic test case"

    def test_1(self):
        pass
    test_1.enabled = True
    test_1.description = "Nothing to be done in test_1()"

run_tests(TestCase.__subclasses__(), debug_level=1)