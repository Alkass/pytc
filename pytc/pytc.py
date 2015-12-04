import inspect
import logging
import coloredlogs

logger = logging.getLogger(".")
coloredlogs.install(level='DEBUG')

class TestCase(object):
	description = None
	enabled = True

	info = logger.info
	warn = logger.warn
	error = logger.error

	def setup(self):
		pass

def error(error_message):
	logger.error(error_message)

def error_exit(error_message, exit_code = 1):
	from sys import exit
	error(error_message)
	exit(exit_code)

def run(DEBUG = False):
	for _class in TestCase.__subclasses__():
		c = _class()
		if _class.enabled:
			if _class.description:
				logger.info("%s: %s" % (_class.__name__, _class.description))
			elif DEBUG:
				logger.warn("class %s has no description message" % _class.__name__)
			_class_setup_fields = dir(_class.setup)
			if "enabled" not in _class_setup_fields or _class.setup.enabled is True:
				if "description" in _class_setup_fields:
					logger.info("%s.setup: %s" % (_class.__name__, _class.setup.description))
				elif DEBUG:
					logger.warn("class %s's setup field has no description message")
				c.setup()
			elif DEBUG:
				logger.warn("class %s's setup method is disabled" % _class.__name__)
			all_methods = inspect.getmembers(c, predicate=inspect.ismethod)
			for method_name, method_instance in all_methods:
				if method_name.lower().startswith("test"):
					_class_test_method_fields = dir(method_instance)
					if "enabled" not in _class_test_method_fields or method_instance.enabled is True:
						if "description" in _class_test_method_fields:
							logger.info("%s.%s: %s" % (_class.__name__, method_name, method_instance.description))
						elif DEBUG:
							logger.warn("class %s's %s method has no description message")
						method_instance()
					elif DEBUG:
						logger.warn("class %s's %s method is disabled" % (_class.__name__, method_name))
		elif DEBUG:
			logger.warn("class %s is disabled" % _class.__name__)
