# ------------------------------------------------------------
# lex.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------
import ply.lex as lex

reservedWords = {
    'if'        : 'IF',
    'else'      : 'ELSE',
    'elseif'    : 'ELSEIF',
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
    'Int'       : 'INT',
    'Float'     : 'FLOAT',
    'Bool'      : 'BOOL',
    ##'find'      : 'FIND',
    ##'append'    : 'APPEND',
    'size'      : 'SIZE',
    #'empty'     : 'EMPTY',
    #'sort'      : 'SORT',
    #'pow'       : 'POW',
    #'ceil'      : 'CEIL',
    #'floor'     : 'FLOOR',
    'private'   : 'PRIVATE',
}

# List of token names.   This is always required
tokens = [
    'ID',
    'CTE_F',   # constante Float
    'CTE_I',   # constante Int
    'CTE_B',   # constante Bool
    'CTE_S',   # constante String
    'COL',     # :
    'DOT',     # .
    'COMMA',   # ,
    'SEMICOL', # ;
    'ARROW',   # ->
    'PLUS',    # +
    'MINUS',   # -
    'MUL',     # *
    'DIV',     # /
    'AND',     # &&
    'OR',      # ||
    'NOT',     # !
    'IS',      # =
    'GT',      # >
    'LT',      # <
    'EQUAL',   # ==
    'NEQ',     # !=
    'GEQ',     # >=
    'LEQ',     # <=
    'LC',      # [
    'RC',      # ]
    'LB',      # {
    'RB',      # }
    'LP',      # (
    'RP',      # )
    #'SCOM',    # Simple comment //
    #'MCOM'     # Multi line Comment /* */
]

tokens = tokens + list(reservedWords.values())

# A string containing ignored characters (spaces and tabs) and comments
t_ignore  = ' \t' # spaces and tabs
t_ignore_comment  = '\/\/.*' # 

# Regular expression rules for simple tokens
t_COMMA         = ','
t_COL           = ':'
t_SEMICOL       = ';'
t_DOT           = '\.'
t_ARROW         = '->'

t_MINUS         = r'-'
t_MUL           = r'\*'
t_DIV           = r'/'
t_PLUS          = r'\+'

t_IS            = '='
t_EQUAL         = '=='
t_GEQ           = '>='
t_LEQ           = '<='
t_LT            = '<'
t_GT            = '>'
t_NEQ           = '!='
t_NOT           = '!'
t_OR            = r'\|\|'
t_AND           = r'\&\&'

t_LC            = r'\['
t_RC            = r'\]'

t_LB            = r'\{'
t_RB            = r'\}'

t_LP            = r'\('
t_RP            = r'\)'


# A regular expression rule with some action code
def t_CTE_F(t):
    r'[0-9]+\.[0-9]+'
    return t

def t_CTE_I(t):
    r'[0-9]+'
    return t

def t_CTE_S(t):
    r'\"[ !#-}]*\"'
    t.value = t.value[1:]
    t.value = t.value[:-1]
    return t

def t_CTE_B(t):
    r'true|false'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservedWords.get(t.value,'ID')    # Check for reserved words
    #if t.value in reservedWords:
    #    t.type = t.value
    #t.value = (t.value, symbol_lookup(t.value)) # Look up symbol table information and return a tuple
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Build the lexer
lexer = lex.lex()

"""
data = '''
true
falase
false
truefalse
'''
 
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
"""