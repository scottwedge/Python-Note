# typing hint static typing in python

in order to make the code give a better hint during the construction. you can use the build-in function like:

```python

def  average(a:int, b:int, c:int) -> float:
     return (a + b + c) / 3
```
# Static Typing in Python

variable hint, Function Hint only included in the latest version (after python 3.6)

## Why

* Find bugs at compile-time
* easier maintenance
  * type hints document your code
  * improved IDE support
* Better program design
* But: no need to use it always

## applying typing hints in project

Check this out-- MyPy module
Here is the [Mypy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

```bash
pip install mypy
```
