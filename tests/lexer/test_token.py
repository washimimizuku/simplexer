import unittest

from lexer.token import Token, TokenType, TokenError


class TestToken(unittest.TestCase):

    def test_identifier_token_creation(self):
        token_inputs = (TokenType.IDENTIFIER, 'ID', '[a-zA-Z_][a-zA-Z0-9_]*')
        token = Token(*token_inputs)
        self._test_token_creation(token, token_inputs)

    def test_keyword_token_creation(self):
        token_inputs = (TokenType.KEYWORD, 'FUNCTION', 'function')
        token = Token(*token_inputs)
        self._test_token_creation(token, token_inputs)

    def test_separator_token_creation(self):
        token_inputs = (TokenType.SEPARATOR, 'LPAREN', '(')
        token = Token(*token_inputs)
        self._test_token_creation(token, token_inputs)

    def test_operator_token_creation(self):
        token_inputs = (TokenType.OPERATOR, 'PLUS', '+')
        token = Token(*token_inputs)
        self._test_token_creation(token, token_inputs)

    def test_string_literal_token_creation(self):
        token_inputs = (TokenType.LITERAL, 'STRING', '[a-zA-Z_][a-zA-Z0-9_]*')
        token = Token(*token_inputs)
        self._test_token_creation(token, token_inputs)

    def test_numeric_literal_token_creation(self):
        token_inputs = (TokenType.LITERAL, 'NUMBER', '\d+')
        token = Token(*token_inputs)
        self._test_token_creation(token, token_inputs)

    def test_token_creation_with_invalid_token_type(self):
        with self.assertRaises(TokenError):
            Token(123, 'ID', 'something')

    def test_token_creation_with_empty_token_type(self):
        with self.assertRaises(TokenError):
            Token(None, 'ID', 'something')

    def test_token_creation_with_empty_name(self):
        with self.assertRaises(TokenError):
            Token(TokenType.LITERAL, None, 'something')

    def test_token_creation_with_empty_value(self):
        with self.assertRaises(TokenError):
            Token(TokenType.LITERAL, 'ID', None)

    def _test_token_creation(self, token, token_inputs):
        (token_type, name, value) = token_inputs
        self.assertEqual(token.token_type, token_type)
        self.assertEqual(token.name, name)
        self.assertEqual(token.value, value)
        self.assertEqual(str(token), f'{name}:{token_type.name}="{value}"')
