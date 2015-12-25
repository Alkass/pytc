from pytc.testcase import TestCase, run_tests

class MyFirstTestCase(TestCase):
    enabled = True
    description = "Your class description goes here"

    def setup(self):
        # our test cases preperation goes here
        pass
    setup.enabled = True
    setup.description = "Your setup method description goes here"

    def test_1(self):
        #Your test #1 goes here
        pass
    test_1.enabled = True
    test_1.description = "Your test description"

    def test_2(self):
        #Your test #2 goes here
        pass
    test_2.enabled = True
    test_2.description = "Your test description"

    def test_3(self):
        #Your test #3 goes here
        pass
    test_3.enabled = True
    test_3.description = "Your test description"


run_tests(TestCase.__subclasses__(), debug_level=1)