import unittest

from lexer.token import Token, TokenType, TokenError


class TestToken(unittest.TestCase):

    def test_identifier_token_creation(self):
        token = Token(TokenType.IDENTIFIER, 'variable')
        self.assertEqual(str(token), 'IDENTIFIER="variable"')

    def test_keyword_token_creation(self):
        token = Token(TokenType.KEYWORD, 'function')
        self.assertEqual(str(token), 'KEYWORD="function"')

    def test_separator_token_creation(self):
        token = Token(TokenType.SEPARATOR, '(')
        self.assertEqual(str(token), 'SEPARATOR="("')

    def test_operator_token_creation(self):
        token = Token(TokenType.OPERATOR, '+')
        self.assertEqual(str(token), 'OPERATOR="+"')

    def test_string_literal_token_creation(self):
        token = Token(TokenType.LITERAL, 'some text')
        self.assertEqual(str(token), 'LITERAL="some text"')

    def test_numeric_literal_token_creation(self):
        token = Token(TokenType.LITERAL, 123)
        self.assertEqual(str(token), 'LITERAL="123"')

    def test_token_creation_with_invalid_token_type(self):
        with self.assertRaises(TokenError):
            Token(123, None)

    def test_token_creation_with_empty_token_type(self):
        with self.assertRaises(TokenError):
            Token(None, 'something')

    def test_token_creation_with_empty_literal(self):
        with self.assertRaises(TokenError):
            Token(TokenType.LITERAL, None)
