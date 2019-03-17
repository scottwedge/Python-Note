# Python-Note
this is my python study note :)

## the study of the plursight note


### Beyond the basic-Package:
1. **Module, package**, here is the general picture for the connection between package and module:

    ![package](./images/package.png)

the **packages** are generally directories and the **Modules** are files (without any directories)
here is the type between urllib and urllib.request (the 1st is packages and 2nd is Modules):
```python
>>> import urllib>>> import urllib.request
>>> type (urllib)
<class 'module'>
>>> type (urllib.request)
<class 'module'>
>>> urllib.__path__
['C:\\Users\\jarffery\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\urllib']
>>> urllib.request.__path__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'urllib.request' has no attribute '__path__'
>>>
```

2. **How does Python locate modules?**

the Python would use the a Module named **sys.path** to list of directories Python searches for modules, using the sys.path to get the path of modules.
new path of module could be added in the **sys.path** using:
```python
sys.path.append('the name of the module')
import 'the name of the module'
```
3. **Basic package structure**

Here is the picture for a basic package structure:

![basicalstructure](./images/basicstructure.png)


