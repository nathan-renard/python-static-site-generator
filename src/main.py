from textnode import TextNode, TextType

def main():
    dummy_text = TextNode('example', TextType.TEXT, 'https://example.com')
    print(f'TextNode({dummy_text.text}, {dummy_text.text_type}, {dummy_text.url})')    

main()