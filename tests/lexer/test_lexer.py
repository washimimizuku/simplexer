import unittest

from lexer.lexer import Lexer


class TestLexer(unittest.TestCase):

    def test_basic_(self):
        lexer = Lexer()
        tokens = lexer.tokenize('')

        self.assertEqual(tokens, [])
