# PEP8 and PYLINT

- [PEP8 and PYLINT](#pep8-and-pylint)
  - [what is PEP](#what-is-pep)
  - [what is the PEP8](#what-is-the-pep8)
  - [PEP8 coding stype](#pep8-coding-stype)
  - [three tool for pep8 style](#three-tool-for-pep8-style)

## what is PEP

Python Enhancement Proposal (PEP) 

here is the link to [PEP](https://www.python.org/dev/peps/)

![PEP](./images/PEP.png)

## what is the PEP8

mainly describe the style of the Python code

## PEP8 coding stype

it's about stype, not about program correctness (formatting, whitespace/punctuation, naming)
![PEP8](./images/PEP8.png)

prefer this site: [PEP.org](https://pep8.org/)

pycharm have the build-in function to correct the format style.

Module should be on separate lines,  the imports modules should be in **three groups** separated by **blank lines**:

* Standard library
* Third-part libraries
* Local application/library

Naming rule:

* Modules: short, lowercase names
* Classes: CapitalizerdNaming
* Functions: lowercase_with_underscores
* Constants: ALL_CAPS
* Non-pubilc names start with underscore

Documentation:

* Docstrings for all p**ublic modules, functions, classes** and methods

## three tool for pep8 style

* **pylint**: check the name and style
* **pycodestyle**: focus on style
* **Black**: auto correct

``the pylint can check variable name and more than pycharm can do``

all that three tool can be install through pip.
