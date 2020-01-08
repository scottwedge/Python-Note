# how to generate the most document for project

* **Sphinx**: generating HTML from source documentation.
* **reStructuredText**: markup formatting

``following the rule of PEP257 for docstrings with semantics and conventions``

**Docstrings**:

* string as first statement of a module, function, class or method.
* Becomes the __doc__ attribute.
  * always use ```three double quotes```
  * phrase ending in a period.
  * Methods: specify return value.
  * ![docstring](./images/docstrings.png)
  * ![docstring](./images/docstrings2.png)

## getting start with Sphinx

Sphinx advantage:

* Python documentation generator.
* De-facto standard.
* reStructuredText -> HTML, PDF, etc.
* Extract docstrings from code.

```python
# using pip install sphinx
>>> pip install sphinx
```
![sphinx](./images/Sphinx.png)

edit the index.rst (reStructuredText file).

* the paragraph was seperated by **blank lane**, section was determined by underline headers.
* the code section would be started two "::" and surrended by two blank lane.
* two dot is the comment "..".
* double check the manual of sphinx.

## applying type hint in a project