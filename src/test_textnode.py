import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node_one = TextNode("This is a test node", TextType.BOLD)
        node_two = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node_one, node_two)

    def test_not_eq_different_text(self):
        node_one = TextNode("This is a test node", TextType.BOLD)
        node_two = TextNode("This is a different test node", TextType.BOLD)
        self.assertNotEqual(node_one, node_two)

    def test_not_eq_different_text_type(self):
        node_one = TextNode("This is a test node", TextType.BOLD)
        node_two = TextNode("This is a test node", TextType.ITALIC)
        self.assertNotEqual(node_one, node_two)

    def test_not_eq_different_url(self):
        node_one = TextNode("This is a test node", TextType.LINKS, "http://example.com")
        node_two = TextNode("This is a test node", TextType.LINKS, "http://different.com")
        self.assertNotEqual(node_one, node_two)

    def test_default_url(self):
        node = TextNode("This is a test node", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_defined_url(self):
        node = TextNode("This is a test node", TextType.LINKS, "http://example.com")
        self.assertEqual(node.url, "http://example.com")

if __name__ == "__main__":
    unittest.main()
