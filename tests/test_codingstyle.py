import unittest
import subprocess
import glob


class TestCodingstyle(unittest.TestCase):
    @staticmethod
    def test_codingstyle():
        pyfiles = ["snallygaster", "setup.py"] + glob.glob("tests/*.py")
        subprocess.run(["pycodestyle", "--ignore=W503", "--max-line-length=100"]
                       + pyfiles, check=True)
        subprocess.run(["pyflakes"] + pyfiles, check=True)
        subprocess.run(["pylint", "--disable=missing-docstring,invalid-name,bad-continuation"]
                       + pyfiles, check=True)
        subprocess.run(["flake8", "--select=DUO"] + pyfiles, check=True)


if __name__ == '__main__':
    unittest.main()
