This file contains development notes for myself.

How to make a new release
=========================

* raise version number in *pyproject.toml*.
* Tag it:
  ```
  git tag -a v0.0.x
  [add changelog message]
  git push origin v0.0.x
  ```
* Build the wheel and source distribution:
  ```
  python -m build
  ```
* Upload to PyPI:
  ```
  twine upload dist/*
  ```
