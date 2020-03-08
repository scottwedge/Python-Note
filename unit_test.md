Content

- [unit testing fundamental](#unit-testing-fundamental)
  - [Unit Test Vocabulary](#unit-test-vocabulary)
  - [Summary](#summary)
- [Unit Testing Why and When](#unit-testing-why-and-when)
  - [understand what to build](#understand-what-to-build)
  - [document the unites](#document-the-unites)
  - [design the units](#design-the-units)
  - [regression protection](#regression-protection)
- [Unit Testing with pytest](#unit-testing-with-pytest)
- [Testable Documentation with doctest](#testable-documentation-with-doctest)
- [Using Test Doubles](#using-test-doubles)
  - [Stub module](#stub-module)
  - [Fake module](#fake-module)
  - [Dummies](#dummies)
  - [Mocks an Spies module](#mocks-an-spies-module)
  - [Monkey Patching](#monkey-patching)
  - [Summary](#summary-1)
- [Parameterized Tests & Test Coverage](#parameterized-tests--test-coverage)


# unit testing fundamental

it is a small Piece of code:
* a method or funciton
* a module or class
* a small group of related classes

automated unit test is designed by a human and run without intervention, reports either 'pass' or 'fail'.

```python
import unittest


class PhoneBook:

    def __init(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number
        pass

    def lookup(self, name):
        return self.numbers[name]
    
    def is_consistent(self):
        return True 

class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
    '''automatically run before unittest'''
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
    '''automatically run after unittest, release resources from memory like files'''
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.asertEqual("12345", number)
    
    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    @unittest.skip("WIP") # will sikp next module
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
```

if you want to run the unittest using:(in the same folder)

```bash
python -m unittest
```

Using pycharm and it can add the unittest in IDE.(try this :D).

## Unit Test Vocabulary
* Test suite
* Test case
* Test Fixture
* Unit Under Test(Test Runner)

![unit_test_suite](./images/Unit_test_suite.png)

![unit_test_vocabulary](./images/unittest_vab.png)

the good structure of unitest is :(for each scenario)
* arrange
* act
* assert

Check the **online document** [Unittest](https://docs.python.org/3/library/unittest.html)

|Method | CHecks that| New in|
|---|---|---|
|assertAlmostEqual(a, b)|round(a-b, 7) == 0| |
|assertNotAlmostEqual(a, b)|round(a-b, 7) != 0||
|assertGreater(a, b)|a > b|3.1|
|assertGreaterEqual(a, b)|a >= b|3.1|
|assertLess(a, b)|a < b|3.1|
|assertLessEqual(a, b)|a <= b|3.1|
|assertRegex(s, r)|r.search(s)|3.1|
|assertNotRegex(s, r)|not r.search(s)|3.2|
|assertCountEqual(a, b)|a and b have the same elements in the same number, regardless of their order.|3.2|

## Summary

vocabulary:
* test case
* teset runner
* test Suite
* test Fixture
  * test case Design:
    * Test name
    * arrange-Act-assert
  
# Unit Testing Why and When

what is Unit testing for?

## understand what to build

* business Analysis
* tester
* Designer
* architect
* end-user
* etc

## document the unites

* specify behaviour of the unit under test
* how the original developer indended the unit to be used.
* excutable: keeps in sync with the unit under test

## design the units

![design_unites](.\images\design_the _unites.png)
follow the logic stream (for a better design!)

## regression protection

ensure previously developed and tested software still performs after a change

uh...there is a lots of philosophy idea behind the regression protection

# Unit Testing with pytest

* Defining test cases with pytest
* interpreting test failures
* Test Fixtures
* Organizing test code



original unit testing like this:(not pythonic)

![test_case_class](.\images\tast_case_class.png)



that bring us the **pytest:** a popular alternative to unittest

[pytest link](https://docs.pytest.org/en/latest/)

the pytest could also added in the pycharm test Runner

the pytest fixtures will call the porperty of pytest.fixture:

```python
@pytest.fixture
def resource():
    return Resource()
```

add those code at the front of the test then call it on every test case:D



**useful Pytest Plugins**

* pytest-html: can creat HTML report for you

  ```powershell
  pip install pytest-html
  ```

  

# Testable Documentation with doctest

what is the doctest?

handling output that changes

using **doctest** for regression testing

![doctest](C:\Users\Jerry\Documents\GitHub\Python-Note\images\doctest.png)

the **doctest** can help  to keep the sample update to date.

1. understand what to build
2. **Document the units**
3. Design the units
4. **Regression protection**

how to use it?

just add the example in the docstring:

```python
def Test():
    '''
    this module will print Hello
    >>> test()
    "Hello"
    '''
    print("Hello")
```

then using the doctest to run it:

```python
python -m doctest --doctest-modules test.py
```

![doctest2](C:\Users\Jerry\Documents\GitHub\Python-Note\images\doctest2.png)



How to match varying output?

using:

```python
#doctest:+ELLIPSIS
```

![doctest3](C:\Users\Jerry\Documents\GitHub\Python-Note\images\doctest3.png)

Check this out!!

[doctest official link](https://docs.python.org/3/library/doctest.html)

# Using Test Doubles

## Stub module

the Stub framework in the unitest, it looks good from the outside, while it contains nothing except what you put there.

## Fake module

the Fake modle looks good from out side but it has an implementation with logic and behaviour.   

## Dummies

it doesn't matter what it looks like, and it usually None

## Mocks an Spies module

the stub will not fail the test but the Mock or Spy can fail the test if it's not called correctly(it will make assertion).

Three kinds of assertion: **return_value, State change, Method call**

The **mock** expect certain method calls, otherwise raise an error

![test doubles](images/doubles%20test.png)

## Monkey Patching

```python

from unittest.mock import patch

## two way to achaive the monkey patch

## first method using with
def test_alarm_with_high_pressure_value():
    with patch('alarm.Sensor') as test_sensor_class:
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 22
        test_sensor_class.return_value = test_sensor_instance

        alarm = Alarm()
        alarm.check()

        assert alarm.is_alarm_on

## second method using decorator
@patch('alarm.Sensor')
def test_alarm_with_high_pressure_value(test_sensor_class):
    with patch('alarm.Sensor') as test_sensor_class:
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 22
        test_sensor_class.return_value = test_sensor_instance

        alarm = Alarm()
        alarm.check()
```

The monkey used when it's hard to insert a testing module or replce a module with testing.

please reach to the reference:

[unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

## Summary
1. What is a test double?
2. Why use a Test Doulbe?
3. Inject Test Doubles using Monkeypatching
# Parameterized Tests & Test Coverage