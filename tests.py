from pytc.pytc import TestCase, run as run_tests

class A(TestCase):
	description = "This is a test case example"
	x, y = None, None
	def setup(self):
		self.x = 30
		self.y = 30
	setup.description = "invoking the setup method"

	def test_if_equal(self):
		self.info("Yes" if self.x == self.y else "No")
	test_if_equal.description = "Are x and y equal?"

	def test_if_x_is_greater(self):
		self.info("Yes" if self.x > self.y else "No")
	test_if_x_is_greater.description = "Is x greater than y?"

	def test_if_y_is_greater(self):
		self.info("Yes" if self.y > self.x else "No")
	test_if_y_is_greater.description = "Is y greater than x?"

"""
	The following method call tells pytc to run all TestCase
	children in the order they are implemented in this source
	file.
"""
run_tests(DEBUG=True)
