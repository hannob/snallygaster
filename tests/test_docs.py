import re
import unittest


class TestCodingstyle(unittest.TestCase):
    # checking if there is documentation for all snallygaster tests
    # in the TEST.md documentation
    def test_docs(self):
        f = open("snallygaster", encoding="utf-8")
        funcs = re.findall("def test_([a-z_]*)", f.read())
        f.close()
        fd = open("TESTS.md", encoding="utf-8")
        docs = []
        ol = ""
        for line in fd.readlines():
            if line.startswith("---"):
                docs.append(ol.rstrip())
            ol = line
        fd.close()
        self.assertEqual(funcs, docs)


if __name__ == "__main__":
    unittest.main()
