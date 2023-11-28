import glob
import subprocess
import unittest


class TestCodingstyle(unittest.TestCase):
    @staticmethod
    def test_codingstyle():
        pyfiles = ["snallygaster", "setup.py"] + glob.glob("tests/*.py")
        subprocess.run(["pycodestyle", "--ignore=W503", "--max-line-length=100"]
                       + pyfiles, check=True)
        subprocess.run(["pyflakes"] + pyfiles, check=True)
        subprocess.run(["pylint", "--disable=missing-docstring,invalid-name,"
                                  "consider-using-with,too-many-lines"]
                       + pyfiles, check=True)
        subprocess.run(["flake8", "--select=DUO"] + pyfiles, check=True)
        subprocess.run(["pyupgrade", "--py311-plus"] + pyfiles, check=True)


if __name__ == "__main__":
    unittest.main()
