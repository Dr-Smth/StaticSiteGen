from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"

class TextNode():
    def __init__(self, text, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_textnode):
        return (
            self.text == other_textnode.text and
            self.text_type == other_textnode.text_type and
            self.url == other_textnode.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"