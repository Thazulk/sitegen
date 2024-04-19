from textnode import TextNode


def main():
    textnode = TextNode("Text", "bold", "https://www.boot.dev")
    print(textnode.__repr__())


main()
