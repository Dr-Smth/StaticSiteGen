#HTML node classes

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
    

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        if value is None:
            raise ValueError("LeafNode instances must have a 'value'.")
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        #if tag does not exist return "value" as raw text string:
        if self.tag == None:
            return f"{self.value}"      

        #if props exists set "prop_string" to a string representation of "props" using .props_to_html method:
        if self.props != None:
            prop_string = self.props_to_html()
        else: prop_string = ""

        #create the opening and closing tags
        start_tag = f"<{self.tag}{prop_string}>"
        end_tag = f"</{self.tag}>"
        
        #combine the opening tag, value, and closing tag
        return start_tag + self.value + end_tag
    

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        if children is None:
            raise ValueError("ParentNode instances must have 'children'.")
        if tag is None:
            raise ValueError("ParentNode instances must have a 'tag'.")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.children == []:
            raise ValueError("ParentNode instances must have 'children'.")

        #generate the string representation of the node's attributes
        prop_string = self.props_to_html() if self.props else ""
        
        #create the opening and closing tags
        start_tag = f"<{self.tag}{prop_string}>"
        end_tag = f"</{self.tag}>"
        
        #recursively generate HTML for all child nodes
        children_html = ''.join(child.to_html() for child in self.children)
        
        #combine the opening tag, children HTML, and closing tag
        return f"{start_tag}{children_html}{end_tag}"