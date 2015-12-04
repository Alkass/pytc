from pytc import TestCase, run as run_tests

class M(TestCase):
	pass

class K(TestCase):
	x, y = None, None
	def setup(self):
		self.x = 30
		self.y = 30

	def test_1(self):
		print self.x + self.y
		assert(self.x == self.y)

run_tests()
