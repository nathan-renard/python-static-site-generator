from enum import Enum

class TextType(Enum):
    TEXT = 'text'
    BOLD = '**bold**'
    ITALIC = '_italic_'
    CODE = '`code`'
    LINKS = '[anchor text](url)'
    IMAGES = '![alt text](url)'

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )


    def __repr__(self):
        return f'TextNode(text={self.text}, text_type={self.text_type}, url={self.url})'