#pytc
<i>pytc</i> (stands for Python Test Case) a tiny Python code testing tool designed to keep your Python test cases organized and informative.

#Is pytc the Right Tool for my Project?
Large projects require well-defined sets of test cases, and as your project requirements change, you'll often find yourself re-implementing (or making major/minor modifications to) existing code. Some existing features break when they are modified or when new features are added. <i>pytc</i> allows you to re-run all your test cases with a single command line.

#Documentation
The whole idea behind <i>pytc</i> is simple; extend the `TestCase` abstract class, implement the `setup()` method (optional), write as many test methods as you need, and <i>pytc</i> will take care of the rest. The "rest" includes running all your classes in the order they are listed in the source code file.

>Note: All methods starting with the word 'test' in their names are considered individual test cases and will be automatically invoked by <i>pytc</i>.

Perhaps the bare minimum test case class looks like the following:

```python
class MyFirstTestCase(TestCase):
  pass
```
The class above will be invoked successfully, but nothing will happen as a result of its execution. Lets define some useful methods:

```python
class MyFirstTestCase(TestCase):
  def setup(self):
    pass
  def test_1(self):
    pass
  def test_2(self):
    pass
  def test_n(self):
    pass
```

The class above will be invoked successfully, but still nothing will happen as a result of its execution since all methods are declared but left unimplemented. Let's now write a simple test case class:

```python
class MyFirstTestCase(TestCase):
  var1, var2 = 0, 0
  def setup(self):
    self.var1 = 10
    self.var2 = 12
  def test_1(self):
    print "var1 == var1 ??", (self.var1 == self.var2)
  def test_2(self):
    print "var1 > var2 ??", (self.var1 > self.var2)
  def test_n(self):
    print "var1 < var2 ??", (self.var1 < self.var2)
```

The output of the above test case will look like the following:

```
var1 == var1 ?? False
var1 > var1 ?? False
var1 < var1 ?? True
```

##The `enabled` boolean flag
You may, at some point, want to temporarily disable a class, that is, wanting an implemented test case class to be overlooked when running the test cases. To do this, you need to set the `enabled` class member value to `False`.

Example:

```python
class MyFirstTestCase(TestCase):
  enabled = False
  var1, var2 = 0, 0
  def setup(self):
    self.var1 = 10
    self.var2 = 12
  def test_1(self):
    print "var1 == var1 ??", (self.var1 == self.var2)
  def test_2(self):
    print "var1 > var2 ??", (self.var1 > self.var2)
  def test_n(self):
    print "var1 < var2 ??", (self.var1 < self.var2)
```
Methods can be enabled and disabled as well.

Example:

```python
class MyFirstTestCase(TestCase):
  var1, var2 = 0, 0
  def setup(self):
    self.var1 = 10
    self.var2 = 12
  setup.enabled = True
  def test_1(self):
    print "var1 == var1 ??", (self.var1 == self.var2)
  test_1.enabled = False
  def test_2(self):
    print "var1 > var2 ??", (self.var1 > self.var2)
  test_2.enabled = False
  def test_n(self):
    print "var1 < var2 ??", (self.var1 < self.var2)
  test_3.enabled = True
```

##The `description` string literal
A test case that doesn't use the `print` function is a useless test case. You may (and you will) need to print out some information at the execution of some or every test case. To do so, simply assign a meaningful description to your classes and methods as follows:

```python
class MyFirstTestCase(TestCase):
  description = "This class assigns two different values to two variables and runs some comparison checks on them"
  var1, var2 = 0, 0
  def setup(self):
    self.var1 = 10
    self.var2 = 12
  setup.enabled = True
  def test_1(self):
    print "var1 == var1 ??", (self.var1 == self.var2)
  test_1.enabled = False
  test_1.description = "is var1 equal to var2?"
  def test_2(self):
    print "var1 > var2 ??", (self.var1 > self.var2)
  test_2.enabled = False
  test_2.description = "is var1 greater than var2?"
  def test_n(self):
    print "var1 < var2 ??", (self.var1 < self.var2)
  test_3.enabled = True
  test_3.description = "is var1 smaller than var2?"
```

#Author
[Fadi Hanna Al-Kass](http://github.com/alkass)
