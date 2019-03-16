# ------------------------------------------------------------
# lexer.py
#
# Luis Salomon Flores Ugalde
# A00817435
# ------------------------------------------------------------
import ply.lex as lex

class Lexer(object):
    # Reserved words
    reserved = {
    'program'   : 'PROG',
    'var'       : 'VAR',
    'if'        : 'IF',
    'else'      : 'ELSE',
    'print'     : 'PRINT',
    'int'       : 'INT',
    'float'     : 'FLOAT',
    'cte.float' : 'CTE_F',
    'cte.int'   : 'CTE_I',
    'cte.string': 'CTE_S',

    }

    # List of token names.
    tokens =[
    'ID',
    'COMMA',
    'NUMBER',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'EQUAL',
    #Left/Right Parentesis
    'LP',
    'RP',
    #Left/Right brackets
    'LB',
    'RB',
    'COL',
    'SEMICOL',
    # Not Equal to
    'NEQ',
    #Less tan
    'LT',
    #Greater tan
    'GT'
    ] + list(reserved.values())

    t_ignore        = ' \t\r\n\f\v'
    t_COMMA         = ','
    t_COL           = ':'
    t_SEMICOL       = ';'
    t_MINUS         = r'-'
    t_MUL           = r'\*'
    t_DIV           = r'/'
    t_PLUS          = r'\+'
    t_EQUAL         = '='

    t_LP            = r'\('
    t_RP            = r'\)'
    t_LB            = r'\{'
    t_RB            = r'\}'

    t_NEQ           = '<>'
    t_LT            = '<'
    t_GT            = '>'


    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, t.type)
        return t

    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

# # Build the lexer and try it out
#m = Lexer()
#m.build()           # Build the lexer
#m.test("program Foo; { if (value > value) { } else { };}"#)     # Test it##
