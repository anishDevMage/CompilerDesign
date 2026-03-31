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

    # CONST
    @_('CONST')
    def expr(self, p):
        val = True if p.CONST.upper() == 'T' else False
        return {
            "value": val,
            "prefix": p.CONST.upper()
        }

    # AND
    @_('expr AND expr')
    def expr(self, p):
        return {
            "value": p.expr0["value"] and p.expr1["value"],
            "prefix": f"∧ {p.expr0['prefix']} {p.expr1['prefix']}"
        }

    # OR
    @_('expr OR expr')
    def expr(self, p):
        return {
            "value": p.expr0["value"] or p.expr1["value"],
            "prefix": f"∨ {p.expr0['prefix']} {p.expr1['prefix']}"
        }

    # NOT
    @_('NOT expr')
    def expr(self, p):
        return {
            "value": not p.expr["value"],
            "prefix": f"¬ {p.expr['prefix']}"
        }

    # IMPLIES
    @_('expr IMPLIES expr')
    def expr(self, p):
        return {
            "value": (not p.expr0["value"]) or p.expr1["value"],
            "prefix": f"→ {p.expr0['prefix']} {p.expr1['prefix']}"
        }

    # Parentheses
    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    # Error handling
    def error(self, p):
        if p:
            raise SyntaxError(f'Syntax error at token {p.value}')
        else:
            raise SyntaxError("Error at EOF")

if __name__ == '__main__':
    parser = CalcParser()