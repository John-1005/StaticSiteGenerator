import unittest
from main import extract_title



class Test_extract_title(unittest.TestCase):
    def test_basic_header(self):
        markdown = "# Heading 1, testing heading 1"
        result = extract_title(markdown)
        self.assertEqual(result, "Heading 1, testing heading 1")

    def test_no_header(self):
        markdown = "No header in this text"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_header_extra_spacing(self):
        markdown = "#    This header has extra spaces   "
        result = extract_title(markdown)
        self.assertEqual(result, "This header has extra spaces")

    def test_h2_header(self):
        markddown = "## Heading 2, should return an error"
        with self.assertRaises(Exception):
            extract_title(markdown)




if __name__ == "__main__":
    unittest.main()
