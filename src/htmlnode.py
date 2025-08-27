from textnode import TextNode, TextType

class HTMLNode:
    def __init__(
            self,
            tag: str = None,
            value: str = None,
            props: dict = None,
            children: list["HTMLNode"] = None,
            ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"<{self.tag}{self.props_to_html()}>" + (self.value or '') + ''.join(str(child) for child in self.children or []) + f"</{self.tag}>"

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        if not self.props or len(self.props) == 0:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value or ''}</{self.tag}>"
    
def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("text_node must be an instance of TextNode")
    ttype = text_node.text_type
    if ttype == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif ttype == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif ttype == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif ttype == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif ttype == TextType.LINKS:
        if not text_node.url:
            raise ValueError("TextNode of type LINK must have a url")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif ttype == TextType.IMAGES:
        if not text_node.url:
            raise ValueError("TextNode of type IMAGE must have a url")
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported text_type: {ttype}")
        
        
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag must be defined for ParentNode")
        if self.children is None:
            raise ValueError("Children must be provided for ParentNode")
        if not self.children:
            raise ValueError("Children list must not be empty for ParentNode")
        
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"