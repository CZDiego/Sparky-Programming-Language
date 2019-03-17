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
    'if'        : 'IF',
    'else'      : 'ELSE',
    'while'     : 'WHILE',
    'input'     : 'INPUT',
    'print'     : 'PRINT',
    'var'       : 'VAR',
    'let'       : 'LET',
    'function'  : 'FUNCTION',
    'class'     : 'CLASS',
    'return'    : 'RETURN',
    'init'      : 'INIT',
    'main'      : 'MAIN',
    'int'       : 'INT',
    'float'     : 'FLOAT',
    'bool'      : 'BOOL',
    'true'      : 'TRUE',
    'false'     : 'FALSE',
    'find'      : 'FIND',
    'append'    : 'APPEND',
    'size'      : 'SIZE',
    'emtpy'     : 'EMPTY',
    'sort'      : 'SORT',
    'pow'       : 'POW',
    'ceil'      : 'CEIL',
    'floor'     : 'FLOOR',
    }

    #'cte.float' : 'CTE_F',
    #'cte.int'   : 'CTE_I',
    #'cte.string': 'CTE_S',
    # List of token names.
    tokens =[
    'ID',
    'COL',
    'DOT',
    'COMMA',
    'SEMICOL',
    # TO is ' -> '
    'TO',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'AND',
    'OR',
    'NOT',
    # IS is ' = '
    'IS',
    #Greater tan
    'GT',
    #Less tan
    'LT',
    # EQ is ' == '
    'EQUAL',
    # Not Equal to
    'NEQ',
    # Greater or Equal To  ' >= '
    'GEQ',
    # Less or Equal To  ' >= '
    'LEQ',
    #Left/Right Corchet [ ]
    'LC',
    'RC',
    #Left/Right brackets
    'LB',
    'RB',
    #Left/Right Parentesis
    'LP',
    'RP',
    #Simple comment //
    'SCOM',
    #Multi line Comment /* */
    'MCOM'
    ] + list(reserved.values())

    t_ignore        = ' \t\r\n\f\v'
    t_MCOM          = r'/\*(.|\n)*?\*/'
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
    #Check if correct*


    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, t.type)
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

 # Build the lexer and try it out
#m = Lexer()
#m.build()           # Build the lexer
#m.test("/* AOIDJNA980394U10IJRNASFD AOISDFBNASDJ */")
