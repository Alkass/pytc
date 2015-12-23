from sys import stdout, exit
import inspect
from logger import ColorfulOutputLogger


logger = ColorfulOutputLogger()


class TestCase(object):

	success = logger.success
	info = logger.info
	warning = logger.warning
	fail = logger.fail

	description = None
	enabled = True

	def setup(self):
		pass
	setup.enabled = True
	setup.description = None

	def run(self):
		if self.enabled:
			if self.description:
				logger.info("%s: %s" % (type(self).__name__, self.description), 0)
			else:
				logger.warning("%s %s" % (type(self).__name__, "has no class description."), 0)
			setup_method_attribs = dir(self.setup)
			if "enabled" not in setup_method_attribs or self.setup.enabled is True:
				if "description" in setup_method_attribs and self.setup.description is not None:
					logger.info(self.setup.description, 0)
				else:
					logger.warning("setup method has no description.", 0)
				self.setup()
			else:
				logger.warning("setup method is disabled. Enable this method by setting the 'enabled' flag to True.", 0)
			all_methods = inspect.getmembers(self, inspect.ismethod)
			for method_name, method_instance in all_methods:
				if method_name.lower().startswith("test"):
					test_method_attribs = dir(method_instance)
					if "enabled" not in test_method_attribs or method_instance.enabled is True:
						if "description" in test_method_attribs and method_instance.description is not None:
							logger.info(method_instance.description, 0)
						else:
							logger.warning("%s method has no description." % method_name, 0)
					else:
						self.warning("%s is disabled. Enable this method by setting the 'enabled' flag to True." % method_name, 0)
					method_instance()


def run_tests(classes, debug_level = 0, output_redirector = stdout):
	logger.debug_level=debug_level
	logger.output_redirector = output_redirector
	for _class in classes:
		_class().run()
	logger.out_stats()
