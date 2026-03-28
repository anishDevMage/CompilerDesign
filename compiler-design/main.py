from calclex import CalcLexer
from calcparser import CalcParser

def main():
    print("Hello from compiler-design!")

    lexer = CalcLexer()
    parser = CalcParser()

    # data = '''x = 3 + 
    #             42 #this is a comment
    #                 * (s - t)'''
    
    data = '5 - 2'
    
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))

    #IMPLEMENTING PARSER
    result = parser.parse(lexer.tokenize(data))
    print(result)


if __name__ == "__main__":
    main()
