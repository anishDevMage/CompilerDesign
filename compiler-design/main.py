from calclex import CalcLexer
from calcparser import CalcParser
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

def evaluate_expression(text):
    lexer = CalcLexer()
    parser = CalcParser()
    
    for tok in lexer.tokenize(text):
        print('type=%r, value=%r' % (tok.type, tok.value))

    parsed = parser.parse(lexer.tokenize(text))

    return parsed


def main():
    print("Hello from compiler-design!")

    # lexer = CalcLexer()
    # parser = CalcParser()
    
    # AND = r'∧'
    # OR = r'∨'
    # NOT = r'¬'
    # IMPLIES = r'→'

    # data = 'T ∧ F ∨ T ∧ F'
    # data = 'T → F ∨ T'
    # data = '(T ∨ F) ∧ F'
    
    data = 'T ∨ (F ∧ F)'
    result = evaluate_expression(data)
    

    #IMPLEMENTING PARSER
    print(result)


if __name__ == "__main__":
    main()
