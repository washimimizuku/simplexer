class Lexer:
    def __init__(self, tokens):
        self.tokens = tokens

    def tokenize(self, code):
        return []


class LexerError(Exception):
    pass
