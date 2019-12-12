This file contains development notes for myself.

How to make a new release
=========================

* raise version number in *setup.py*.
* Build the wheel:
  ```
  python setup.py bdist_wheel
  ```
* Upload to PyPI:
  ```
  twine upload -s dist/*
  ```
