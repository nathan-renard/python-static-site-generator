import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith("> "):
        return BlockType.QUOTE
    if re.match(r"^(\*|-|\+) ", block) or re.match(r"^\d+\. ", block):
        if re.match(r"^(\*|-|\+) ", block):
            return BlockType.ULIST
        else:
            return BlockType.OLIST
    return BlockType.PARAGRAPH
    