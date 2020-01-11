This file contains development notes for myself.

How to make a new release
=========================

* raise version number in *setup.py*.
* Build the wheel and source distribution:
  ```
  python setup.py bdist_wheel sdist
  ```
* Upload to PyPI:
  ```
  twine upload -s dist/*
  ```
