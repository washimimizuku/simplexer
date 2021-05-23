import enum


class TokenType(enum.Enum):
    IDENTIFIER = "IDENTIFIER"
    KEYWORD = "KEYWORD"
    SEPARATOR = "SEPARATOR"
    OPERATOR = "OPERATOR"
    LITERAL = "LITERAL"
    COMMENT = "COMMENT"


class Token:
    def __init__(self, token_type: TokenType, literal: str) -> None:
        if not isinstance(token_type, TokenType):
            raise TokenError

        if not literal:
            raise TokenError

        self.token_type = token_type
        self.literal = literal

    def __str__(self):
        return f'{self.token_type.name}="{self.literal}"'


class TokenError(Exception):
    pass
