
def p_program(p):
    'program   : program_a program_c program_d main'

def p_program_a(p):
    '''
    program_a  : proram_b program_a
    | empty
    '''
def p_program_b(p):
    '''
    program_b  : let
    | class
    | emtpy
    '''
def p_program_c(p):
    '''
    program_c  : var program_c
    | emtpy
    '''
def p_program_d(p):
    '''
    program_d  : function program_d
    | emtpy
    '''
# No definition for cte variables.
# TODO: Please update cte variables
def p_type(p):
    '''
    type    : LC CTE_I RC LC CTE_I RC atomic
    | LC CTE_I RC atomic
    | atomic
    | ID
    '''

def p_atomic(p):
    '''
    atomic  : INT
    | FLOAT
    | BOOL
    '''

def p_var(p):
    'var    : VAR ID COL type var_a SEMICOL'
def p_var_a(p):
    '''
    var_a   : IS var_b
    | empty
    '''
# Possible name change to cte_vars
def p_var_b(p):
    '''
    var_b   : CTE_I
    | CTE_F
    | CTE_B
    '''

def p_let(p):
    'let    : LET ID COL type IS var_b SEMICOL'

def p_function(p):
    'function   : FUNCTION id LP params RP function_a function_block'
def p_function_a(p):
    '''
    function_a   : RARROW type
    | empty
    '''

def p_params(p):
    'params   : ID COL type params_a'
def p_params_a(p):
    '''
    params_a   : COMMA params
    | empty
    '''

def p_block(p):
    'block  : LB block_a RB'
# recursive statutes
def p_block_a(p):
    '''
    block_a : statute block_a
    | empty
    '''

def p_function_block(p):
    'function_block   : LB function_block_a block_a RB'

def p_function_block_a(p):
    '''
    function_block_a   : function_block_b function_block_a
    | empty
    '''
# Possible change of name to neutral declaration
def p_function_block_b(p):
    '''
    p_function_block_b : var
    | let
    | empty
    '''

def p_main(p):
    'main   : FUNCTION MAIN LP RP function_block'

# class_a = optional ->  : id
# class_b = optional ->  recursive(optional(private) var|let )
# class_c = optional ->  recursive(init)
# class_d = optional ->  recursive(optional(private)function)
# class_e = optional -> private
# class_f = mandatory -> var|let
def p_class(p):
    'class     : CLASS ID class_a LB class_b init class_c class_d RB'

def p_class_a(p):
    '''
    class_a   : COL ID
    | empty
    '''

def p_class_b(p):
    '''
    class_b : class_e class_f class_b
    | empty
    '''
# TODO: No PRIVATE in Lexer!!!
def p_class_e(p):
    '''
    class_e : PRIVATE
    | empty
    '''

def p_class_f(p):
    '''
    class_f : var
    | let
    '''
# first mandatory init already stablished
def p_class_c(p):
    '''
    class_c : init class_c
    | empty
    '''
# class_d = optional ->  recursive(optional(private)function)
def p_class_d(p):
    '''
    class_d : class_e function p_class_d
    | empty
    '''





def p_empty(p):
    'empty :'
