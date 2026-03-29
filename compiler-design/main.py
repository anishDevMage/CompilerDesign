from calclex import CalcLexer
from calcparser import CalcParser
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QGridLayout

class LogicCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Logic Calculator")

        layout = QVBoxLayout()

        self.input_box = QLineEdit()
        self.input_box.setReadOnly(True)
        self.input_box.setPlaceholderText("Enter expression (e.g., T ∧ F)")

        self.result_label = QLabel("Result:")

        grid = QGridLayout()

        buttons = [
            ('T', 0, 0), ('F', 0, 1),
            ('¬', 0, 2), ('→', 0, 3),
            ('∧', 1, 0), ('∨', 1, 1),
            ('(', 1, 2), (')', 1, 3),
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda _, t=text: self.add_symbol(t))
            grid.addWidget(btn, row, col)

        self.button = QPushButton("Evaluate")
        self.button.clicked.connect(self.evaluate)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_input)

        layout.addWidget(self.input_box)
        layout.addLayout(grid)
        layout.addWidget(self.button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    # ADDING SYMBOLS
    def add_symbol(self, symbol):
        current = self.input_box.text()
        self.input_box.setText(current + symbol)

    # CLEARING INPUT
    def clear_input(self):
        self.input_box.clear()

    # EVAL EVENT
    def evaluate(self):
        text = self.input_box.text()
        try:
            result = evaluate_expression(text)
            self.result_label.setText(f"Result: {result}")
        except Exception as e:
            self.result_label.setText(f"Error: {e}")



# EVALUATE EXPRESSION IN THE INPUT BOX
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
    app = QApplication([])
    window = LogicCalculator()
    window.show()
    app.exec()
