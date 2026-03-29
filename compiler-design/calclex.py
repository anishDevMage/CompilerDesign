#calclex.py

from sly import Lexer

class CalcLexer(Lexer):
    tokens = { CONST, LPAREN, RPAREN, AND, OR, NOT, IMPLIES}

    ignore = ' \t'

    #ignoring speical comments
    ignore_comments = r'\#.*'

    # ID      = r'[A-Z]'
    IMPLIES = r'→'
    CONST = r'[TFtf]'
    LPAREN  = r'\('
    RPAREN  = r'\)'
    AND = r'∧'
    OR = r'∨'
    NOT = r'¬'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1


if __name__ == '__main__':
    lexer = CalcLexer()
    