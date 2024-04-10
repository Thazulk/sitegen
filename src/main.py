from textnode import TextNode

print("Hello world")


def main():
    textnode = TextNode("Text", "bold", "https://www.boot.dev")
    print(textnode.repr())


main()
