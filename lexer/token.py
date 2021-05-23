import enum


class TokenType(enum.Enum):
    IDENTIFIER = "IDENTIFIER"
    KEYWORD = "KEYWORD"
    SEPARATOR = "SEPARATOR"
    OPERATOR = "OPERATOR"
    LITERAL = "LITERAL"
    COMMENT = "COMMENT"


class Token:
    def __init__(self, token_type: TokenType, name: str, value: str) -> None:
        if not isinstance(token_type, TokenType):
            raise TokenError

        if not name:
            raise TokenError

        if not value:
            raise TokenError

        self.token_type = token_type
        self.name = name
        self.value = value

    def __str__(self):
        return f'{self.name}:{self.token_type.name}="{self.value}"'


class TokenError(Exception):
    pass
