import lexer
import re

def main():
    with open('test.lang', 'r') as file:
        content = file.read()

    lex = lexer.Lexer(content)
    # # We now call the tokenize method
    token = lex.tokenize()


main()

