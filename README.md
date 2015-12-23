#pytc
<i>pytc</i> (stands for Python Test Case) is a tiny Python code testing tool designed to keep your Python test cases organized and informative.

#What's in the Box?
You basically get two main classes (`TestCase` and `ColorfulOutputLogger`). `TestCase` is the class you'll need to extend in every test case class you write, and `ColorfulOutputLogger` is a debugging mechanism used to log all outputs in a proper format.

#Installation
`git clone https://github.com/alkass/pytc`

`cd pytc`

`python setup.py install`

#Usage
Following is a very basic example:

```python
from pytc.testcase import TestCase, run_tests

class BasicTestCase(TestCase):
    enabled = True
    description = "This is a basic test case"

    def setup(self):
        pass
    setup.enabled = True
    setup.description = "Nothing to be done in setup()"

    def test_1(self):
        pass
    test_1.enabled = True
    test_1.description = "Nothing to be done in test_1()"

run_tests(TestCase.__subclasses__())
```


#Author
[Fadi Hanna Al-Kass](http://github.com/alkass)
