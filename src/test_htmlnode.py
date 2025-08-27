import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from htmlnode import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):

    def test_full_html_representation(self):
        node = HTMLNode(
            tag="div",
            value="Hello, World!",
            props={"class": "greeting"},
            children=[HTMLNode(tag="span", value="This is a child node")]
        )
        expected_html = '<div class="greeting">Hello, World!<span>This is a child node</span></div>'
        self.assertEqual(str(node), expected_html)

    def test_html_without_value(self):
        node = HTMLNode(
            tag="p",
            props={"id": "paragraph"}
        )
        expected_html = '<p id="paragraph"></p>'
        self.assertEqual(str(node), expected_html)

    def test_html_with_no_props(self):
        node = HTMLNode(
            tag="section",
            value="This section has no props."
        )
        expected_html = '<section>This section has no props.</section>'
        self.assertEqual(str(node), expected_html)

    def test_html_with_no_children(self):
        node = HTMLNode(
            tag="header",
            value="Header without children"
        )
        expected_html = '<header>Header without children</header>'
        self.assertEqual(str(node), expected_html)

    def test_html_with_empty_props(self):
        node = HTMLNode(
            tag="footer",
            value="Footer with empty props",
            props={}
        )
        expected_html = '<footer>Footer with empty props</footer>'
        self.assertEqual(str(node), expected_html)

class TestLeafNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_bold(self):
        from textnode import TextNode, TextType
        from htmlnode import text_node_to_html_node
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_text_node_to_html_node_italic(self):
        from textnode import TextNode, TextType
        from htmlnode import text_node_to_html_node
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_text_node_to_html_node_code(self):
        from textnode import TextNode, TextType
        from htmlnode import text_node_to_html_node
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")

    def test_text_node_to_html_node_link(self):
        from textnode import TextNode, TextType
        from htmlnode import text_node_to_html_node
        node = TextNode("Link text", TextType.LINKS, "http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        self.assertEqual(html_node.props["href"], "http://example.com")

    def test_text_node_to_html_node_image(self):
        from textnode import TextNode, TextType
        from htmlnode import text_node_to_html_node
        node = TextNode("Alt text", TextType.IMAGES, "http://img.com/img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "http://img.com/img.png")
        self.assertEqual(html_node.props["alt"], "Alt text")

    def test_text_node_to_html_node_invalid_type(self):
        from textnode import TextNode, TextType
        from htmlnode import text_node_to_html_node
        class FakeType:
            pass
        node = TextNode("Invalid", FakeType())
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_leaf_to_html_p(self):
        node = LeafNode(
            "p",
            "Hello, world!"
            )
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode(
            "span",
            "This is a span",
            props={"class": "highlight"}
        )
        self.assertEqual(node.to_html(), '<span class="highlight">This is a span</span>')

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_without_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, []).to_html()

    def test_to_html_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_to_html_with_empty_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>'
        )