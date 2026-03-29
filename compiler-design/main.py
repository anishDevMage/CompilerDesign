from calclex import CalcLexer
from calcparser import CalcParser
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class LogicCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Logic Calculator")

        layout = QVBoxLayout()

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter expression (e.g., T ∧ F)")

        self.result_label = QLabel("Result:")

        self.button = QPushButton("Evaluate")
        self.button.clicked.connect(self.evaluate)

        layout.addWidget(self.input_box)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def evaluate(self):
        text = self.input_box.text()
        try:
            result = evaluate_expression(text)
            self.result_label.setText(f"Result: {result}")
        except Exception as e:
            self.result_label.setText(f"Error: {e}")

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
