class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag #string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value #string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children #list of HTMLNode objects representing the children of this node
        self.props = props #dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    
    def to_html(self):
        #to be overriden by child classes
        raise NotImplementedError
    
    def props_to_html(self):
        #returns a string representation of the HTML attributes of the node
        if self.props == None:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return (
            f"HTMLNode(\n"
            f"\n"
            f"Tag: {self.tag}. \n"
            f"\n"
            f"Value: {self.value}. \n"
            f"\n"
            f"Children: {self.children}. \n"
            f"\n"
            f"Props: {self.props})"
        )