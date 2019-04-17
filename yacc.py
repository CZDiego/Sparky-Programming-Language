# ------------------------------------------------------------
# yacc.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------
import ply.yacc as yacc
from lex import tokens
from program import Program
from varTable import Var
import math

program = Program()

def p_program(p):
    'program   : prog0 program_a program_c program_d main'

def p_program_a(p):
    '''
    program_a  : program_b program_a
    | empty
    '''
def p_program_b(p):
    '''
    program_b  : let prog1
    | class prog2
    '''
def p_program_c(p):
    '''
    program_c  : var prog3 program_c
    | empty
    '''

def p_program_d(p):
    '''
    program_d  : function prog4 program_d
    | empty
    '''
#-----------------------------------------------------------------------
# Neuro points program stage
#################
def p_prog0(p):
    'prog0    :'
    program.current_quad = ("goto", None, None, None)
    program.add_quad()
    program.add_pJump()
    program.print_quads()
    # Goto is missing the operator add to pending operators List
    # increment program.BASE +1
def p_prog1(p):
    'prog1  :'
    # Tabla metes
    # new variable object!
    #

def p_prog2(p):
    'prog2  :'
    # new class object!
    # current_class_name is set at class rules
    # current_class is an object class created in class rules
    # program.classesDir.Add(current_class_name,current_class)
    # Add to class sub dictionary of program dictionary

def p_prog3(p):
    'prog3  :'
    # same as prog2
    # Add to var sub dictionary of program dictionary

def p_prog4(p):
    'prog4  :'
    # same as prog2
    # Add to function sub dictionary of program dictionary

#################
#-----------------------------------------------------------------------

def p_type(p):
    '''
    type    : type0 atomic
    '''

# typeM is a fix.
def p_typeM(p):
    '''
    typeM    : type0 LC CTE_I RC LC CTE_I RC atomic type1
    | type0 LC CTE_I RC atomic type2
    | type0 ID type4
    '''
#-----------------------------------------------------------------------
# Neuro points type stage
#################

# A type variable object for easier management!!!!
# Also a type.Directory for space
def p_type0(p):
    'type0  :'
    program.new_type()
    # current_type = new SparkyType()

def p_type1(p):
    'type1  :'
    program.current_type.spark_type = p[-1]
    program.current_type.col = p[-3]
    program.current_type.row = p[-6]
    # //total space needed

def p_type2(p):
    'type2  :'
    program.current_type.spark_type = p[-1]
    program.current_type.col = p[-3]
    program.current_type.row = -1
    # //total space needed

def p_type3(p):
    'type3  :'
    program.current_type.spark_type = p[-1]
    program.current_type.col = -1 #atomic not array
    program.current_type.row = -1 #atomic not matrix


def p_type4(p):
    'type4  :'
    if p[-1] not in program.varTable.objects:
        print('\033[91m' + "ERROR:" + '\033[0m' + " Object Class has not been declared at line " + str(p.lexer.lineno) + ".")
    program.current_type.spark_type = p[-1]

#################
#-----------------------------------------------------------------------

def p_atomic(p):
    '''
    atomic  : INT type3
    | FLOAT type3
    | BOOL type3
    '''

#-----------------------------------------------------------------------
# Neuro points atomic stage
#################


#################
#-----------------------------------------------------------------------

def p_var(p):
    '''
    var    : VAR ID var1 COL type var2 var_a SEMICOL
    |  VAR ID var1 COL typeM SEMICOL var2
    '''

#assignment in declaration
def p_var_a(p):
    '''
    var_a   : IS var_b var3
    | empty
    '''
# Possible name change to cte_vars
def p_var_b(p):
    '''
    var_b   : CTE_I var4
    | CTE_F var5
    | CTE_B var6
    '''
#-----------------------------------------------------------------------
# Neuro points var stage
#################

def p_var1(p):
    'var1    :'
    # current_var = new var()
    # current_stage -> global true, local false
    # current_var_name = p[-1]
    # if(program.current_stage){
    #   if(program.VarTable.Search(p[-1])) then error
    #  }else {
    #   if(program.class_stage){
    #    if(program.VarTable.Objects[].Search(p[-1])) then error
    #   }else{
    # if(program.functionTable.VarTable.Search(p[-1])) then error
    #   }
    #}
    #}

def p_var2(p):
    'var2    :'
    # current_var.type = current_type
    # current_var_name = p[-1]
    # add (current_var_name, current_var)
    # current_var = new var
def p_var3(p):
    'var3    :'
    #create assignment quad
def p_var4(p):
    'var4   :'
    program.current_value = p[-1]
    program.current_type.spark_type = "Int"
    # current_assignation_right = "Int"
    #  memory manager?
    # if(!ConstantDir.Search(p[-1])){
    #      var location = program.Memory.INT_CONST_MEMORY_LOC
    #      program.Memory.Increase("Int")
    #       if(!program.Memory.CheckInt()){error stackoverflow}
    #        // this if would be something like ->
    #           if( program.Memory.INT_CONST_MEMORY_LOC > program.Memory.MAX_INT_MEMORY)
    #
    # }
    #
    # Add constant memory direction to stack
    #
def p_var5(p):
    'var5   :'
    program.current_value = p[-1]
    program.current_type.spark_type = "Float"
    #current_assignation_right = "Float"
    # if(!ConstantDir.Search(p[-1])){
    #      var location = program.Memory.INT_CONST_MEMORY_LOC
    #      program.Memory.Increase("Int")
    #       if(!program.Memory.CheckInt()){error stackoverflow}
    #        // this if would be something like ->
    #           if( program.Memory.INT_CONST_MEMORY_LOC > program.Memory.MAX_INT_MEMORY)
    # }
    #
def p_var6(p):
    'var6   :'
    program.current_value = p[-1]
    program.current_type.spark_type = "Bool"
    #current_assignation_right = "Bool"
    #  Same as 5 and 4 but could be
    #  initialized in memory from start

#################
#-----------------------------------------------------------------------

def p_let(p):
    'let    : LET ID let1 COL type let2 IS var_b SEMICOL let3'
#-----------------------------------------------------------------------
# Neuro points let stage
#################
def p_let1(p):
    'let1   :'
    program.current_var = Var()
    program.current_var.constant = True
    # current_stage -> global true, local false
    program.current_var_name = p[-1]


    if program.current_stage:#global constant
        if p[-1] in program.varTable:
            print('\033[91m' + "ERROR:" + '\033[0m' + " Variable already declared at line " + str(p.lexer.lineno) + ".")



    # if(program.current_stage){
    #   if(program.VarTable.Search(p[-1])) then error
    #  }else {
    #   if(program.class_stage){
    #    if(program.VarTable.Objects[].Search(p[-1])) then error
    #   }else{
    # if(program.functionTable.VarTable.Search(p[-1])) then error
    #   }
    #}
    #}

def p_let2(p):
    'let2   :'
    program.current_var.s_type = program.current_type
    program.current_var.address = program.globalMemory.get_next_address(program.current_type.spark_type)
    program.varTable.set(program.current_var_name, program.current_var)
    if program.current_stage:
        if program.current_type.spark_type == "Int":
            program.globalMemory.memory[program.current_var.address] = 0
        elif program.current_type.spark_type == "Float":
            program.globalMemory.memory[program.current_var.address] = 0.0
        else:
            program.globalMemory.memory[program.current_var.address] = False
    # ONLY WORKS FOR GLOBAL MEMORY
    # reset
    # current_var_name , value, type, etc?
    program.new_type()

def p_let3(p):
    'let3   :'
    #check semantic cube
    #CHECK MAYBE FAILS ON GLOBAL MEMORY
    result = program.semanticCube.checkResult("=", program.current_var.s_type.spark_type, program.current_type.spark_type)
    if result == "Error":
        print('\033[91m' + "ERROR:" + '\033[0m' + " Type Mismatch at line " + str(p.lexer.lineno) + ".")
    else:
        if result == "Int":
            program.globalMemory.memory[program.current_var.address] = math.floor(int(program.current_value))
        elif result == "Float":
            program.globalMemory.memory[program.current_var.address] = float(program.current_value)
        else:
            program.globalMemory.memory[program.current_var.address] = program.current_value

    # current_var_name = ""
    # current_var
    # Make assignment quad for variable

#################
#-------------------------------
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

# recursive statement
def p_block_a(p):
    '''
    block_a : statement block_a
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
    'class     : CLASS ID class1 class_a LB class_b init class_c class_d RB'

def p_class_a(p):
    '''
    class_a   : COL ID class2
    | empty
    '''

def p_class_b(p):
    '''
    class_b : class_e class_f class_b
    | empty
    '''

def p_class_e(p):
    '''
    class_e : PRIVATE class3
    | empty
    '''

def p_class_f(p):
    '''
    class_f : var class4
    | let class4
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
    class_d : class_e function class5 class4 class_d
    | class6
    '''

#-----------------------------------------------------------------------
# Neuro points for class
#################

def p_class1(p):
    'class1 :'
    if p[-1] in program.ClassDir:
        print("ERROR : Class Already declared")
    else:
        program.current_class_name = p[-1]
        program.new_class()
        program.current_stage = False
        program.class_stage = True
        print(p[-1])
def p_class2(p):
    'class2 :'
    #This is inheritance copy all as deepcopy
    program.inherit_class(current_class_name,p[-1])

def p_class3(p):
    'class3 :'
    program.current_security = True

def p_class4(p):
    'class4 :'
    program.current_security = False

def p_class5(p):
    'class5 :'

    program.current_class.funDir[program.current_function_name] = program.current_function
def p_class6(p):
    'class6 :'
    #Better to add it at the end
    program.ClassDir[current_class_name] = program.current_class
    program.current_stage = True
    program.class_stage = False

def p_class7(p):
    'class7 :'
    program.current_function_name = program.current_class_name

def p_class8(p):
    'class8 :'
    program.current_function.add_params(program.current_params)

def p_class9(p):
    'class9 :'
    #this is wrong
    if current_class_name in program.funDir:
        program.fundir[current_class_name].append(program.current_function)
    else:
        program.fundir[current_class_name] = [program.current_function]
        #IS A LIST!!!!!!
    program.new_function()
#################
#-----------------------------------------------------------------------

def p_init(p):
    'init   : INIT class7 LP params RP class8 block class9'

def p_statement(p):
    '''
    statement : print
    | input
    | assignment
    | condition
    | loop
    | call_function
    | return
    '''

def p_return(p):
    'return : RETURN expression SEMICOL'

def p_obj(p):
    'obj : ID array attribute'

def p_assignement(p):
    'assignment : obj IS expression SEMICOL'

def p_print(p):
    'print : PRINT LP print_a RP SEMICOL'

def p_print_a(p):
    '''
    print_a : expression
    | CTE_S
    | empty
    '''
def p_input(p):
    'input  : INPUT LP obj RP SEMICOL'

def p_loop(p):
    'loop   : WHILE expression block'

def p_call_function(p):
    'call_function  : obj call_func SEMICOL'

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
    'elseif : ELSEIF expression block'

def p_else(p):
    'else   : ELSE block'

def p_expression(p):
    'expression : comparison expression_a'

def p_expression_a(p):
    '''
    expression_a    : AND comparison expression_a
    | OR comparison
    | empty
    '''

def p_comparison(p):
    'comparison    : exp comparison_a'

def p_comparison_a(p):
    '''
    comparison_a  : comparison_b exp comparison_a
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
    exp_a   : PLUS term exp_a
    | MINUS term exp_a
    | empty
    '''

def p_term(p):
    'term    : factor term_a'
def p_term_a(p):
    '''
    term_a   : MUL factor term_a
    | DIV factor term_a
    | empty
    '''

def p_factor(p):
    '''
    factor  : LP expression RP
    | factor_a var_cte
    '''
def p_factor_a(p):
    '''
    factor_a    : MINUS
    | NOT
    | empty
    '''
def p_var_cte(p):
    '''
    var_cte : obj call_func_optional
    | CTE_I
    | CTE_F
    | CTE_B
    '''
def p_array(p):
    '''
    array   : LC expression RC array_a
    | empty
    '''
def p_array_a(p):
    '''
    array_a  : LC expression RC
    | empty
    '''

def p_attribute(p):
    '''
    attribute   : DOT ID
    | empty
    '''

def p_call_func(p):
    'call_func : LP call_params RP'

def p_call_func_optional(p):
    '''
    call_func_optional : call_func
    | empty
    '''

#no need for comment since lexer ignores it


def p_empty(p):
    'empty :'

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Unexpected token '" + str(p.value) + "' at line " + str(p.lexer.lineno) + ".")
        #print(p.type)
    else:
        print("Syntax error at EOF")


# Build the parser
parser = yacc.yacc(start='program')


with open("program.sdfm", "r") as inputFile:
    data = inputFile.read()

result = parser.parse(data)

if result != None:
    print(result)
