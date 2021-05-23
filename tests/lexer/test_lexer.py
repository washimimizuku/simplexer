import unittest

from lexer.lexer import Lexer
from lexer.token import Token, TokenType


class TestLexer(unittest.TestCase):

    def test_empty_code(self):
        lexer = Lexer({})
        tokens = lexer.tokenize('')

        self.assertEqual(tokens, [])

    def test_monkey_lang_lexer(self):
        lexer = Lexer({
            # Identifiers
            Token(TokenType.IDENTIFIER, 'ID', '[a-zA-Z_][a-zA-Z0-9_]*'),
            # Keywords
            Token(TokenType.KEYWORD, 'FUNCTION', 'fn'),
            Token(TokenType.KEYWORD, 'LET', 'let'),
            Token(TokenType.KEYWORD, 'IF', 'if'),
            Token(TokenType.KEYWORD, 'ELSE', 'else'),
            Token(TokenType.KEYWORD, 'WHILE', 'while'),
            # Separators
            Token(TokenType.SEPARATOR, 'COMMA', ','),
            Token(TokenType.SEPARATOR, 'SEMICOLON', ';'),
            Token(TokenType.SEPARATOR, 'COLON', ':'),
            Token(TokenType.SEPARATOR, 'LPAREN', '('),
            Token(TokenType.SEPARATOR, 'RPAREN', ')'),
            Token(TokenType.SEPARATOR, 'LBRACE', '{'),
            Token(TokenType.SEPARATOR, 'RBRACE', '}'),
            Token(TokenType.SEPARATOR, 'LBRACKET', '['),
            Token(TokenType.SEPARATOR, 'RBRACKET', ']'),
            # Operators
            Token(TokenType.OPERATOR, 'ASSIGN', '='),
            Token(TokenType.OPERATOR, 'PLUS', '+'),
            Token(TokenType.OPERATOR, 'MINUS', '-'),
            Token(TokenType.OPERATOR, 'BANG', '!'),
            Token(TokenType.OPERATOR, 'ASTERISK', '*'),
            Token(TokenType.OPERATOR, 'SLASH', '/'),
            Token(TokenType.OPERATOR, 'LT', '<'),
            Token(TokenType.OPERATOR, 'GT', '>'),
            Token(TokenType.OPERATOR, 'EQ', '=='),
            Token(TokenType.OPERATOR, 'NOT_EQ', '!='),
            # Literals
            Token(TokenType.LITERAL, 'INT', '\d'),
            Token(TokenType.LITERAL, 'BOOLEAN', 'true|false'),
            Token(TokenType.LITERAL, 'STRING', '[a-zA-Z_][a-zA-Z0-9_]*'),
            # Comments
            Token(TokenType.COMMENT, 'COMMENT', '\/\*.*\*\/'),
        })

        tokens = lexer.tokenize('''
            let five = 5;
            let ten = 10;
            let add = fn(x, y) {
                x + y;
            };
            let result = add(five, ten);
        ''')

        expected_values = (
            (TokenType.KEYWORD, "LET", "let"),
            (TokenType.IDENTIFIER, "ID", "five"),
            (TokenType.OPERATOR, 'ASSIGN', '='),
            (TokenType.LITERAL, 'INT', "5"),
            (TokenType.SEPARATOR, 'SEMICOLON', ";"),
            (TokenType.KEYWORD, "LET", "let"),
            (TokenType.IDENTIFIER, "ID", "ten"),
            (TokenType.OPERATOR, 'ASSIGN', '='),
            (TokenType.LITERAL, 'INT', "10"),
            (TokenType.SEPARATOR, 'SEMICOLON', ";"),
            (TokenType.KEYWORD, "LET", "let"),
            (TokenType.IDENTIFIER, "ID", "add"),
            (TokenType.OPERATOR, 'ASSIGN', '='),
            (TokenType.KEYWORD, 'FUNCTION', "fn"),
            (TokenType.SEPARATOR, 'LPAREN', "("),
            (TokenType.IDENTIFIER, "ID", "x"),
            (TokenType.SEPARATOR, 'COMMA', ","),
            (TokenType.IDENTIFIER, "ID", "y"),
            (TokenType.SEPARATOR, 'RPAREN', ")"),
            (TokenType.SEPARATOR, 'LBRACE', "{"),
            (TokenType.IDENTIFIER, "ID", "x"),
            (TokenType.OPERATOR, 'PLUS', "+"),
            (TokenType.IDENTIFIER, "ID", "y"),
            (TokenType.SEPARATOR, 'SEMICOLON', ";"),
            (TokenType.SEPARATOR, 'RBRACE', "}"),
            (TokenType.SEPARATOR, 'SEMICOLON', ";"),
            (TokenType.KEYWORD, "LET", "let"),
            (TokenType.IDENTIFIER, "ID", "result"),
            (TokenType.OPERATOR, 'ASSIGN', '='),
            (TokenType.IDENTIFIER, "ID", "add"),
            (TokenType.SEPARATOR, 'LPAREN', "("),
            (TokenType.IDENTIFIER, "ID", "five"),
            (TokenType.SEPARATOR, 'COMMA', ","),
            (TokenType.IDENTIFIER, "ID", "ten"),
            (TokenType.SEPARATOR, 'RPAREN', ")"),
            (TokenType.SEPARATOR, 'SEMICOLON', ";"),
        )

        self.assertEqual(len(tokens), 36)

        for index, (token_type, name, value) in enumerate(tokens):
            self.assertEqual(token_type,
                             expected_values[index].token_type,
                             f"Expected token type is wrong. Got {token_type}, but expected {expected_values[index].token_type}")
            self.assertEqual(name,
                             expected_values[index].name,
                             f"Expected name is wrong. Got {name}, but expected {expected_values[index].name}")
            self.assertEqual(value,
                             expected_values[index].value,
                             f"Expected value is wrong. Got {value}, but expected {expected_values[index].value}")
