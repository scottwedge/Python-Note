# pip install packages

Overview in this chapter:

* Dependencies
* packages
  * Find, download and install
  * Manage
* Virtual environments
  * Project dependencies
  * creat use, and manage
* Best practices
* Recommended tools

## pip-package management

```python
pip -v
#will show the version of the python
```

when using the Windows:

* Configuring PATH
* Run pip

![pip_install](./images/pip-install.png)

![pip-PATH](./images/pip-PATH.png)

### Managing packages with pip

* Installing packages
* Removing packages
* Listing packages
* Inspecting packages
* Getting help
* Searching Packages

* Rule #1:
  * best practice with a virtual environment (to avoid any fatal error)
  * don't use pip with sudo

```python
# check the package list
pip list
# install package
pip install packagename
# removing package
pip unistall packagename
# looking for help
pip help list
# for package detail
pip show packagename
```

check the **pypi** for more package :D

### where are packages installed?

* the sys.path variable
* installing for other python version

```python
>>> import sys
>>> sys.path
['', 'C:\\Users\\Jerry\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 'C:\\Users\\Jerry\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 'C:\\Users\\Jerry\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 'C:\\Users\\Jerry\\AppData\\Local\\Programs\\Python\\Python38-32', 'C:\\Users\\Jerry\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Users\\Jerry\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages']
>>>
```

The package only can be ran under the right python version and location. (espicially when there are multiple version in the directory)

### a better way to call pip

```python
python2 -m pip install flask
#instead of just using pip
```

**it's all depend on the system configure!!**

## Virtual environments-Projects and dependencies

## Virtualenvwrapper-making venv more convenient

## Other tools
