import typing

from lexer.token import Token


class Lexer:
    def __init__(self, tokens: typing.List[Token]) -> None:
        self.tokens = tokens
        self.code = ''
        self.position = 0
        self.read_position = 0
        self.current_char = ''

    def tokenize(self, code: str) -> typing.List[Token]:
        self.code = code
        while self.current_char != '\0':
            self._read_char()
            print(self.current_char)

        return []

    def _next_token(self) -> Token:
        self._skip_whitespace()

        token = None

        # TODO: Detect type of token
        # TODO: Create Token

        self._read_char()

        return token

    def _read_char(self) -> str:
        if self.read_position >= len(self.code):
            self.current_char = '\0'
        else:
            self.current_char = self.code[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    # TODO: Make this configurable
    def _skip_whitespace(self):
        while self.current_char in [' ', '\t', '\r', '\n']:
            self._read_char()


class LexerError(Exception):
    pass
