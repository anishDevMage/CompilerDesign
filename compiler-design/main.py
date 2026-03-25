from calclex import CalcLexer

def main():
    print("Hello from compiler-design!")

    lexer = CalcLexer()

    data = 'x = 3 + 42 * (s - t)'
    
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))


if __name__ == "__main__":
    main()
