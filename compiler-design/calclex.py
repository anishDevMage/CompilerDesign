#calclex.py

from sly import Lexer

class CalcLexer(Lexer):
    tokens = { NUMBER, ID, LPAREN, RPAREN, IF, ELSE, WHILE, PRINT,
               PLUS, MINUS, TIMES, DIVIDE, ASSIGN,
               EQ, LT, LE, GT, GE, NE }
    
    
    literals = { '(', ')', '{', '}', ';' }

    ignore = ' \t'

    #ignoring speical comments
    ignore_comments = r'\#.*'
    ignore_newline = r'\n+'

    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    EQ      = r'=='
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'
    LE      = r'<='
    LT      = r'<'
    GE      = r'>='
    GT      = r'>'
    NE      = r'!='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t
    
    # Identifiers and Keywords  
    # ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    # ID['if'] = IF
    # ID['else'] = ELSE
    # ID['while'] = WHILE
    # ID['print'] = PRINT

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1


if __name__ == '__main__':
    lexer = CalcLexer()
    