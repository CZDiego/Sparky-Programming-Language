import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    'program   : program_a program_c program_d main'

def p_program_a(p):
    '''
    program_a  : program_b program_a
    | empty
    '''

def p_program_b(p):
    '''
    program_b  : let
    | class
    '''

def p_program_c(p):
    '''
    program_c  : var program_c
    | empty
    '''

def p_program_d(p):
    '''
    program_d  : function program_d
    | empty
    '''

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

def p_main(p):
    'main   : MAIN LP RP function_block'

def p_function(p):
    'function   : FUNCTION ID LP params RP function_a function_block'

def p_function_a(p):
    '''
    function_a   : ARROW type
    | empty
    '''

def p_params(p):
    '''
    params   : ID COL type params_a
    | empty
    '''

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
    function_block_b : var
    | let
    '''

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
    class_d : class_e function class_d
    | empty
    '''
def p_init(p):
    'init   : INIT LP params RP block'

def p_statute(p):
    '''
    statute : print
    | input
    | assignment
    | condition
    | loop
    | call_function
    | return
    '''

def p_return(p):
    'return : RETURN expression SEMICOL'

def p_assignement(p):
    'assignment : ID array attribute IS expression SEMICOL'

def p_print(p):
    'print : PRINT LP print_a RP SEMICOL'

def p_print_a(p):
    '''
    print_a : expression
    | CTE_S
    | empty
    '''
def p_input(p):
    'input  : INPUT LP ID array attribute RP SEMICOL'

def p_loop(p):
    'loop   : WHILE expression block'

def p_call_function(p):
    'call_function  : ID LP call_params RP SEMICOL'

def p_call_params(p):
    '''
    call_params    : expression call_params_a
    | empty
    '''
def p_call_params_a(p):
    '''
    call_params_a  : COMMA expression call_params_a
    | empty
    '''
def p_condition(p):
    'condition  : IF expression block condition_a condition_b'

def p_condition_a(p):
    '''
    condition_a  : elseif condition_a
    | empty
    '''

def p_condition_b(p):
    '''
    condition_b : else
    | empty
    '''

def p_elseif(p):
    'elseif : ELSE IF expression block'

def p_else(p):
    'else   : ELSE block'

def p_expression(p):
    'expression : comparison expression_a'

def p_expression_a(p):
    '''
    expression_a    : AND expression
    | OR expression
    | empty
    '''

def p_comparison(p):
    'comparison    : exp comparison_a'

def p_comparison_a(p):
    '''
    comparison_a  : comparison_b exp
    | empty
    '''
def p_comparison_b(p):
    '''
    comparison_b  : GEQ
    | LEQ
    | GT
    | LT
    | EQUAL
    | NEQ
    '''

def p_exp(p):
    'exp    : term exp_a'

def p_exp_a(p):
    '''
    exp_a   : PLUS exp
    | MINUS exp
    | empty
    '''

def p_term(p):
    'term    : factor term_a'
def p_term_a(p):
    '''
    term_a   : MUL term
    | DIV term
    | empty
    '''

def p_factor(p):
    '''
    factor  : LP expression RP
    | factor_a var_cte
    '''
def p_factor_a(p):
    '''
    factor_a    : PLUS
    | MINUS
    | NOT
    | empty
    '''
def p_var_cte(p):
    '''
    var_cte : ID array attribute
    | ID LP call_params RP array attribute
    | CTE_I
    | CTE_F
    | CTE_B
    '''
def p_array(p):
    'array   : LC expression RC array_a'
def p_array_a(p):
    '''
    array_a  : LC expression RC
    | empty
    '''

def p_attribute(p):
    'attribute   : DOT ID attribute_a'
def p_attribute_a(p):
    '''
    attribute_a   : LP call_params RP
    | empty
    '''

#no need for comment since lexer ignores it


def p_empty(p):
    'empty :'

# Error rule for syntax errors
def p_error(p):
    if p != None:
        print("Syntax error in input!")
        print(p)    


# Build the parser
parser = yacc.yacc(start='program')


with open("program.txt", "r") as inputFile:
    data = inputFile.read()

result = 0;

while result != None:
    try:
        s = data
    except EOFError:
        break
    if not s: 
        continue
    result = parser.parse(s)
    if result != None:
        print(result)


