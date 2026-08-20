import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_type_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_neq(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://hej.hopp")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://hej.happ")
        self.assertNotEqual(node, node2)

    def test_type_neq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_italic_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://hej.hopp")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://hej.hopp")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
