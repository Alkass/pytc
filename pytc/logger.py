class ColorfulOutput:

	class Colors:
		RED = "\033[0;31m"
		BLUE = ""
		GREEN = ""
		ORANGE = ""
		BLANK = "\033[0;00m"
		
	def success(self, message):
		return "%sSUCCESS: %s%s" % (self.Colors.GREEN, message, self.Colors.BLANK)

	def info(self, message):
		return "%sINFO: %s%s" % (self.Colors.BLUE, message, self.Colors.BLANK)

	def warning(self, message):
		return "%sWARNING: %s%s" % (self.Colors.ORANGE, message, self.Colors.BLANK)

	def fail(self, message):
		return "%sFAIL: %s%s" % (self.Colors.RED, message, self.Colors.BLANK)


class ColorfulOutputLogger:

	cout = None
	debug_level = 0
	padding_str, trailing_str = "", ""

	def __init__(self, cout = ColorfulOutput(), debug_level = 0):
		self.cout = cout
		self.debug_level = debug_level

	def header(self):
		from getpass import getuser as username
		return username()

	def success(self, message, debug_level):
		if self.debug_level <= self.debug_level:
			print("%s%s %s%s" % (self.padding_str, self.header(), self.cout.success(message), self.trailing_str))

	def info(self, message, debug_level):
		if self.debug_level <= self.debug_level:
			print("%s%s %s%s" % (self.padding_str, header(), self.cout.info(message), self.trailing_str))

	def warning(self, message, debug_level):
		if self.debug_level <= self.debug_level:
			print("%s %s" % (self.padding_str, header(), self.cout.warning(message), self.trailing_str))

	def fail(self, message, debug_level):
		if self.debug_level <= self.debug_level:
			print("%s%s %s%s" % (self.padding_str, header(), self.cout.fail(message), self.trailing_str))

	def terminate_logger(self):
		pass

c = ColorfulOutputLogger(debug_level = 30)


c.success("hello there", 0)
