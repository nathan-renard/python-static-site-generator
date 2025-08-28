import unittest
from markdown_blocks import markdown_to_blocks


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_no_leading_trailing_newlines(self):
        md = """This is **bolded** paragraph
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        from markdown_blocks import block_to_block_type, BlockType

        self.assertEqual(
            block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH
        )

    def test_heading(self):
        from markdown_blocks import block_to_block_type, BlockType

        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_code(self):
        from markdown_blocks import block_to_block_type, BlockType

        self.assertEqual(
            block_to_block_type("```\ncode\n```"), BlockType.CODE
        )

    def test_quote(self):
        from markdown_blocks import block_to_block_type, BlockType

        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        from markdown_blocks import block_to_block_type, BlockType

        self.assertEqual(
            block_to_block_type("- Item 1\n- Item 2"), BlockType.ULIST
        )
        self.assertEqual(
            block_to_block_type("* Item 1\n* Item 2"), BlockType.ULIST
        )
        self.assertEqual(
            block_to_block_type("+ Item 1\n+ Item 2"), BlockType.ULIST
        )

    def test_ordered_list(self):
        from markdown_blocks import block_to_block_type, BlockType

        self.assertEqual(
            block_to_block_type("1. Item 1\n2. Item 2"), BlockType.OLIST
        )

if __name__ == "__main__":
    unittest.main()
