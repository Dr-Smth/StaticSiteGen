from textnode import *
from htmlnode import *
from textnode_to_htmlnode import *

def main():
    test_textnode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test_textnode.__repr__)









if __name__ == "__main__":
    main()