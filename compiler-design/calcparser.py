from sly import Parser
from calclex import CalcLexer

class CalcParser(Parser):
    tokens = CalcLexer.tokens

    #GRAMMAR
    # E -> E → E
    # E -> E ∨ E
    # E -> E ∧ E
    # E -> ¬ E
    # E -> ( E )
    # E -> T
    # E -> F

    precedence = (
        ('right', IMPLIES),
        ('left', OR),
        ('left', AND),
        ('right', NOT),
    )

    @_('CONST')
    def expr(self, p):
        if p.CONST == 'T': 
            return True 
        else: 
            return False
        
    @_('expr AND expr')
    def expr(self, p):
        return p.expr0 and p.expr1
    
    @_('expr OR expr')
    def expr(self, p):
        return p.expr0 or p.expr1

    @_('NOT expr')
    def expr(self, p):
        return not p.expr
    
    @_('expr IMPLIES expr')
    def expr(self, p):
        return (not p.expr0) or p.expr1
    
    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr
    
    def error(self, p):
        if p:
            raise SyntaxError(f'Syntax error at token {p.value}')
        else:
            raise SyntaxError("Error at EOF")

if __name__ == '__main__':
    parser = CalcParser()