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
from sparky_type import SparkyType
from virtualMachine import VirtualMachine
import math
import sys
import pprint

program = Program()

def p_program(p):
    'program   : prog0 program_a program_c program_d main end'

def p_end(p):
    'end :'
    program.current_quad = ("END", None, None, None)
    program.add_quad()

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
    program_d  : function program_d
    | empty
    '''
#-----------------------------------------------------------------------
# Neuro points program stage
#################
def p_prog0(p):
    'prog0    :'
    program.current_quad = ("GOTO", None, None, None)
    program.add_pJump()
    program.add_quad()
    program.current_scope = "global"
    # Goto is missing the operator add to pending operators List
    # increment program.BASE +1
def p_prog1(p):
    'prog1  :'
    # Tabla metes
    # new variable object!
    #

def p_prog2(p):
    'prog2  :'
    program.ClassDir.set(program.current_class_name, program.current_class)
    program.new_class()
    program.class_name = ""

def p_prog3(p):
    'prog3  :'
    # same as prog2
    # Add to var sub dictionary of program dictionary


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
    #program.current_type.type = p[-1]
    program.current_type.row = int(p[-6])
    program.current_type.col = int(p[-3])
    # //total space needed

def p_type2(p):
    'type2  :'
    #program.current_type.type = p[-1]
    program.current_type.row = int(p[-3])
    # //total space needed

def p_type3(p):
    'type3  :'
    program.current_type.type = p[-1]


def p_type4(p):
    'type4  :'
    if p[-1] not in program.ClassDir:
        print('\033[91m' + "ERROR:" + '\033[0m' + " Object Class has not been declared at line " + str(p.lexer.lineno) + ".")
    program.current_type.type = p[-1]

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

def p_var_class(p):
    '''
    var_class   : VAR ID var_c1 COL type var_class_a var_c2 SEMICOL
    |  VAR ID var_c1 COL typeM var_c2 SEMICOL
    '''

#assignment in declaration
def p_var_class_a(p):
    '''
    var_class_a   : IS var_class_b
    | empty
    '''
# Possible name change to cte_vars
def p_var_class_b(p):
    '''
    var_class_b   : CTE_I var_c4
    | CTE_F var_c5
    | CTE_B var_c6
    '''


# -----------------------------------------------------------------------
# Neuro points var stage
#################

def p_var_c1(p):
    'var_c1    :'
    if program.current_scope == "global":
        if p[-1] in program.current_class.varTable.directory:
            print("ERROR VARIABLE DECLARADA ANTERIORMENTE")
        else:
            program.current_var_name = p[-1]

    if program.current_scope == "function":
        if p[-1] in program.current_function.varTable:
            print("ERROR VARIABLE DECLARADA ANTERIORMENTE")
        else:
            program.current_var_name = p[-1]


def p_var_c2(p):
    'var_c2    :'
    if program.current_scope == "global":
        program.current_var.address = -1
        program.current_var.s_type = program.current_type
        if program.current_var.s_type.is_object():
                print("ERROR: Object class does not support objects")

        program.current_class.varTable.set(program.current_var_name, program.current_var)

    if program.current_scope == "function":
        program.current_var.address = program.current_function.funMemory.get_next_address(program.current_type.type,
                                                                                          program.current_type.row,
                                                                                          program.current_type.col)
        program.current_var.s_type = program.current_type
        program.current_function.varTable.set(program.current_var_name, program.current_var)

    program.current_var = Var()
    program.current_var_name = ""
    program.new_type()

def p_var_c4(p):
    'var_c4   :'
    program.current_value = p[-1]
    program.current_type.type = "Int"

def p_var_c5(p):
    'var_c5   :'
    program.current_value = p[-1]
    program.current_type.type = "Float"


def p_var_c6(p):
    'var_c6   :'
    program.current_value = p[-1]
    program.current_type.type = "Bool"


#################
# -----------------------------------------------------------------------


def p_var(p):
    '''
    var    : VAR ID var1 COL type var_a var2 SEMICOL
    |  VAR ID var1 COL typeM var2 SEMICOL
    '''

#assignment in declaration
def p_var_a(p):
    '''
    var_a   : IS var_b
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
    if program.current_scope == "global":
        if p[-1] in program.varTable:
            print("ERROR VARIABLE DECLARADA ANTERIORMENTE")
        else:
            program.current_var_name = p[-1]
    if program.current_scope == "function":
        if p[-1] in program.current_function.varTable:
            print("ERROR VARIABLE DECLARADA ANTERIORMENTE")
        else:
            program.current_var_name = p[-1]
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
    if program.current_scope == "global":
        program.current_var.address = program.globalMemory.get_next_address(program.current_type.type, program.current_type.row, program.current_type.col)
        program.current_var.s_type = program.current_type
        program.varTable.set(program.current_var_name, program.current_var)
    if program.current_scope == "function":
        program.current_var.address = program.current_function.funMemory.get_next_address(program.current_type.type, program.current_type.row, program.current_type.col)
        program.current_var.s_type = program.current_type
        program.current_function.varTable.set(program.current_var_name, program.current_var)

    program.current_var = Var()
    program.current_var_name = ""
    program.new_type()

    # current_var.type = current_type
    # current_var_name = p[-1]
    # add (current_var_name, current_var)
    # current_var = new var


def p_var4(p):
    'var4   :'
    program.current_value = p[-1]
    program.current_type.type = "Int"
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
    program.current_type.type = "Float"
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
    program.current_type.type = "Bool"
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


    if program.current_scope == "global":#global constant
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
    program.current_var.address = program.globalMemory.get_next_address(program.current_type.type, 0, 0)
    program.varTable.set(program.current_var_name, program.current_var)
    if program.current_scope == "global":
        if program.current_type.type == "Int":
            program.globalMemory.memory[program.current_var.address] = 0
        elif program.current_type.type == "Float":
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
    result = program.semanticCube.checkResult("=", program.current_var.s_type.type, program.current_type.type)
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
    'main   : main0 MAIN LP RP function_block'

    for cla in program.ClassDir.directory:
        print("class: " + cla)
        for var_key in program.ClassDir[cla].funDir.directory:
             print("var: " + var_key)
             print("address: " + str(program.ClassDir[cla].funDir[var_key].address))


def p_main0(p):
    'main0   :'
    program.fill_quad(program.BASE)
    program.current_scope = "function"
    program.current_function_name = "main"
    program.new_function()
    program.funDir.set(program.current_function_name, program.current_function)

def p_function(p):
    'function   : FUNCTION fun0 ID fun1 LP params fun3 RP function_a function_block fun6'

def p_function_a(p):
    '''
    function_a   : ARROW type fun4
    | fun5
    '''
#  -----------------------------------------------------------------------
#  Neuro points for function
#  ################

def p_fun0(p):
    'fun0   :'
    program.new_function()
    program.new_params()
    program.current_function.address = program.BASE


def p_fun1(p):
    'fun1   :'
    program.current_function_name = p[-1]
    if program.current_scope == "global":
        if program.current_function_name in program.funDir:
            print('\033[91m' + "ERROR:" + '\033[0m' + "Function already declared before.")
        else:
            program.funDir.set(program.current_function_name, program.current_function)
    else:
        if program.current_function_name in program.current_class.funDir:
            print('\033[91m' + "ERROR:" + '\033[0m' + "Function already declared before in class")

    program.current_scope = "function"

def p_fun3(p):
    'fun3   :'
    program.current_function.add_params(program.current_params)

def p_fun4(p):
    'fun4   :'
    program.current_function.return_type = program.current_type
    program.new_var()
    program.current_var_name = program.current_function.address
    t = program.current_function.return_type
    program.current_var.address =  program.globalMemory.get_next_address(t.type, t.row, t.col)
    program.current_var.s_type = program.current_type
    program.varTable.set(program.current_var_name, program.current_var)
    program.new_var()
    #pide memoria global con nombre

def p_fun5(p):
    'fun5   :'
    program.new_type()
    program.current_type.type = "void"
    program.current_function.return_type = program.current_type

def p_fun6(p):
    'fun6   :'
    program.current_quad = ("ENDPROC", None, None, None)
    program.add_quad()

# ################
#  ------------------------------------------------------------------------


def p_params(p):
    '''
    params   : param0 ID param1 COL type param2 params_a
    | empty
    '''

def p_params_a(p):
    '''
    params_a   : COMMA params
    | empty
    '''
#  -----------------------------------------------------------------------
#  Neuro points for params in function
#  ################

def p_param0(p):
    'param0 :'
    program.new_var()

def p_param1(p):
    'param1 :'
    program.current_var_name = p[-1]
    if program.current_var_name in program.current_params:
        print('\033[91m' + "ERROR:" + '\033[0m' + "Function already has a parameter with that name.")

def p_param2(p):
    'param2 :'
    program.current_var.s_type = program.current_type
    s_type = program.current_type
    program.current_var.address = program.current_function.funMemory.get_next_address(s_type.type, s_type.row, s_type.col)
    program.current_function.varTable.set(program.current_var_name, program.current_var)
    program.current_function.param_key.append((s_type, program.current_var.address))

# ################
#  ------------------------------------------------------------------------

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
    'class     : CLASS ID class1 class_a LB class_b init class_d RB'

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
    class_f : var_class class4
    | let class4
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
    program.new_class()
    program.class_stage = True
    if p[-1] in program.ClassDir:
        print('\033[91m' + "ERROR:" + '\033[0m' + ": Class Already declared")
    else:
        program.current_class_name = p[-1]

def p_class2(p):
    'class2 :'
    if p[-1] not in program.ClassDir:
        print('\033[91m' + "ERROR:" + '\033[0m' + ": Father Class has not been declared")
    #  This is inheritance copy all as deepcopy
    program.inherit_class(p[-1])

def p_class3(p):
    'class3 :'
    program.current_security = True
    program.current_function.private = "private"

def p_class4(p):
    'class4 :'
    program.current_security = False
    program.current_function.private = "public"

def p_class5(p):
    'class5 :'
    program.current_class.funDir.set(program.current_function_name, program.current_function)
    program.current_scope = "global"

def p_class6(p):
    'class6 :'
    #  Better to add it at the end

def p_class7(p):
    'class7 :'
    program.new_function()
    program.current_function_name = program.current_class_name

def p_class8(p):
    'class8 :'
    program.current_function.add_params(program.current_params)
    program.new_params()

def p_class9(p):
    'class9 :'
    #  this is wrong
    if program.current_class_name in program.funDir:
        print('\033[91m' + "ERROR:" + '\033[0m' + ": Init function for class already declared")
    else:
        program.current_function.add_params(program.current_params)
        program.current_type.type = program.current_class_name
        program.current_function.return_type = program.current_type
        program.funDir.set(program.current_class_name, program.current_function)
    program.new_function()
    program.new_params()
    program.new_type()
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
    'return : RETURN expression return1 SEMICOL'

def p_return1(p):
    'return1 : '
    result = program.VP.pop()
    result_type = program.pType.pop()
    if result_type.check_type(program.current_function.return_type):
        program.current_quad = ("RETURN", result, None, program.varTable[program.current_function.address].address)
        program.add_quad()
    else:
        print("ERROR!! type Mismatch!!")


def p_obj(p):
    'obj : ID obj1 array attribute obj2'

#  -----------------------------------------------------------------------
#  Neuro points for  obj
#  ################

def p_obj1(p):
    'obj1 :'
    program.current_id = p[-1]
    program.pOper.append("$")
    program.pIDs.append((p[-1],False, False))

def p_obj2(p):
    'obj2 :'
    program.pOper.pop()

#  ################
#  -----------------------------------------------------------------------
def p_assignement(p):
    'assignment : obj IS assignement1 expression assignement2 SEMICOL'

def p_assignement1(p):
    'assignement1 :'
    # OBJ = . EXPRESSION ;
    #buscar que exista en tabla de variables local y asi
    if program.current_id in program.current_function.varTable:
        #id = . expression
        #is_object
        t = program.current_function.varTable[program.current_id].s_type
        if t.row > 0:
            if t.col > 0:
                #matrix
                print("matrix")
                program.pOper.append("=")
            else:
                print("array")
                program.pOper.append("=")
            #print("ERROR YOU ARE TRYING TO ASSIGN VALUE TO ARRAY OBJECT")
        elif t.is_object():
            #id is object
            print("ERROR YOU ARE TRYING TO ASSIGN VALUE TO OBJECT")
        else:
            program.VP.append(program.current_function.varTable[program.current_id].address)
            program.pType.append(program.current_function.varTable[program.current_id].s_type)
            program.pOper.append("=")

    elif program.current_id in program.varTable:
        print("Global")
    else:
        print("ERROR variable no declarada")
    program.current_id = ""
    program.current_attribute = ""
    program.pIDs.pop()

def p_assignement2(p):
    'assignement2 :'
    right_type = program.pType.pop()
    right_operand = program.VP.pop()
    left_type = program.pType.pop()
    left_operand = program.VP.pop()
    operator = program.pOper.pop()
    result_type = program.semanticCube.checkResult(operator, left_type.type, right_type.type)
    if result_type == "Error":
        print("Error Type Mismatch")
    else:

        program.current_quad = (operator, right_operand, None, left_operand)
        program.add_quad()

def p_print(p):
    'print : PRINT LP print_a RP print3 SEMICOL'

def p_print_a(p):
    '''
    print_a : expression
    | CTE_S print1
    | empty print2
    '''
#  -----------------------------------------------------------------------
#  Neuro points for print
#  ################

def p_print1(p):
    'print1 : '
    t = SparkyType()
    t.type = "cte_s"
    program.pType.append(t)
    program.VP.append(p[-1])

def p_print2(p):
    'print2 : '
    t = SparkyType()
    t.type = "cte_s"
    program.pType.append(t)
    program.VP.append("")

def p_print3(p):
    'print3 : '
    result = program.VP.pop()
    result_type = program.pType.pop()
    program.current_quad = ("PRINT", result, None, None)
    program.add_quad()


def p_input(p):
    'input  : INPUT LP obj RP input1 SEMICOL'

def p_input1(p):
    'input1 : '
    x = program.pIDs.pop()
    if not x[1] and not x[2]:
        #id simple
        address = program.current_function.varTable[x[0]].address
        type = program.current_function.varTable[x[0]].s_type.type
        program.current_quad = ("INPUT", type, None, address)
        program.add_quad()
    else:
        address = program.VP.pop()
        s_type = program.pType.pop()
        program.current_quad = ("INPUT", s_type.type, None, address)
        program.add_quad()

def p_loop(p):
    'loop   : WHILE loop1 expression loop2 block loop3'

#  -----------------------------------------------------------------------
#  Neuro points for  loop
#  ################

def p_loop1(p):
    'loop1 : '
    program.add_pJump()

def p_loop2(p):
    'loop2 : '
    exp_type = program.pType.pop()
    if exp_type.type != "Bool":
        print("ERROR TYPE MISMATCH")
    else:
        result = program.VP.pop()
        program.add_pJump()
        program.current_quad = ("GOTOF", result, None, None)
        program.add_quad()

def p_loop3(p):
    'loop3 : '
    program.fill_quad(program.BASE + 1)
    returnQuad = program.pJumps.pop()
    program.current_quad = ("GOTO", None, None, returnQuad)
    program.add_quad()
#  -----------------------------------------------------------------------

def p_call_function(p):
    'call_function  : obj call_func SEMICOL call_f2'

def p_call_f2(p):
    'call_f2    :'
    program.pIDs.pop()
    era_return = program.pEras.pop()
    program.current_quad = ("GOSUB", era_return[1], None, None)
    program.add_quad()

def p_call_params(p):
    '''
    call_params    : expression call_param1 call_params_a
    | call_param2
    '''
def p_call_params_a(p):
    '''
    call_params_a  : COMMA expression call_param1 call_params_a
    | call_param2
    '''

def p_call_param1(p):
    'call_param1    :'
    if (program.current_param_num + 1) > len(program.called_function.param_key):
        print("ERROR : Function has 1 more argument than expected")

    popped_type = program.pType.pop()
    fun_param_type = program.called_function.param_key[program.current_param_num][0]
    if fun_param_type.check_type(popped_type):
        program.current_quad = ("PARAM", program.VP.pop(), None, program.called_function.param_key[program.current_param_num][1])
        #print(program.called_function.param_key[program.current_param_num][0].type)
        program.add_quad()
        program.current_param_num += 1
    else:
        print("ERROR : Parameter given is of wrong type")



def p_call_param2(p):
    'call_param2    :'
    if len(program.called_function.param_key) != program.current_param_num:
        print("ERROR : Function expecting another parameter")

def p_condition(p):
    'condition  : IF expression condition1 block condition_a condition_b condition4'

def p_condition_a(p):
    '''
    condition_a  : elseif condition_a
    | empty
    '''

def p_condition_b(p):
    '''
    condition_b : condition3 else
    | empty
    '''

#  -----------------------------------------------------------------------
#  Neuro points for  loop
#  ################

def p_condition1(p):
    'condition1 : '
    program.pJumps.append("$")
    exp_type = program.pType.pop()
    if exp_type.type != "Bool":
        print("ERROR TYPE MISMATCH")
    else:
        result = program.VP.pop()
        program.add_pJump()
        program.current_quad = ("GOTOF", result, None, None)
        program.add_quad()

def p_condition2(p):
    'condition2 : '
    program.fill_quad(program.BASE + 1)
    program.add_pJump()
    program.current_quad = ("GOTO", None, None, None)
    program.add_quad()

    exp_type = program.pType.pop()
    if exp_type.type != "Bool":
        print("ERROR TYPE MISMATCH")
    else:
        result = program.VP.pop()
        program.add_pJump()
        program.current_quad = ("GOTOF", result, None, None)
        program.add_quad()

def p_condition3(p):
    'condition3 : '
    program.fill_quad(program.BASE + 1)
    program.add_pJump()
    program.current_quad = ("GOTO", None, None, None)
    program.add_quad()

def p_condition4(p):
    'condition4 : '
    while program.pJumps[-1] != "$":
        program.fill_quad(program.BASE)
    program.pJumps.pop()

#  -----------------------------------------------------------------------

def p_elseif(p):
    'elseif : ELSEIF expression condition2 block'

def p_else(p):
    'else   : ELSE block'

def p_expression(p):
    'expression : comparison expression1 expression_a'

def p_expression_a(p):
    '''
    expression_a    : AND expression2 comparison expression1 expression_a
    | OR expression2 comparison expression1 expression_a
    | empty
    '''
#-----------------------------------------------------------------------
# Neuro points comparison stage
#################
def p_expression1(p):
    'expression1   :'
    if len(program.pOper) != 0:
        if program.pOper[-1] == "&&" or program.pOper[-1] == "||":
            solveOperation()

def p_expression2(p):
    'expression2   :'
    program.pOper.append(p[-1])

def p_comparison(p):
    'comparison    : exp comparison1 comparison_a'

def p_comparison_a(p):
    '''
    comparison_a  : comparison_b exp comparison1 comparison_a
    | empty
    '''
def p_comparison_b(p):
    '''
    comparison_b  : GEQ comparison2
    | LEQ comparison2
    | GT comparison2
    | LT comparison2
    | EQUAL comparison2
    | NEQ comparison2
    '''

#-----------------------------------------------------------------------
# Neuro points comparison stage
#################
def p_comparison1(p):
    'comparison1   :'
    if len(program.pOper) != 0:
        if program.pOper[-1] == ">=" or program.pOper[-1] == "<=" or program.pOper[-1] == ">" or program.pOper[-1] == "<" or program.pOper[-1] == "==" or program.pOper[-1] == "!=":
            solveOperation()

def p_comparison2(p):
    'comparison2   :'
    program.pOper.append(p[-1])

def p_exp(p):
    'exp    : term exp1 exp_a'

def p_exp_a(p):
    '''
    exp_a   : PLUS exp2 term exp1 exp_a
    | MINUS exp2 term exp1 exp_a
    | empty
    '''

#-----------------------------------------------------------------------
# Neuro points exp stage
#################
def p_exp1(p):
    'exp1   :'
    if len(program.pOper) != 0:
        if program.pOper[-1] == "+" or program.pOper[-1] == "-":
            solveOperation()

def p_exp2(p):
    'exp2   :'
    program.pOper.append(p[-1])

def p_term(p):
    'term    : factor term1 term_a'
def p_term_a(p):
    '''
    term_a   : MUL term2 factor term1 term_a
    | DIV term2 factor term1 term_a
    | empty
    '''

#-----------------------------------------------------------------------
# Neuro points term stage
#################
def p_term1(p):
    'term1   :'
    if len(program.pOper) != 0:
        if program.pOper[-1] == "*" or program.pOper[-1] == "/":
            solveOperation()

def p_term2(p):
    'term2   :'
    program.pOper.append(p[-1])

def p_factor(p):
    '''
    factor  : LP factor1 expression RP factor2
    | factor_a var_cte
    '''

#-----------------------------------------------------------------------
# Neuro points factor stage
#################
def p_factor1(p):
    'factor1   :'
    program.pOper.append("(")

def p_factor2(p):
    'factor2   :'
    p = program.pOper.pop()

def p_factor_a(p):
    '''
    factor_a    : MINUS
    | NOT
    | empty
    '''

def p_var_cte(p):
    '''
    var_cte : obj call_func_optional var_cte1
    | CTE_I var_cte2
    | CTE_F var_cte3
    | CTE_B var_cte4
    '''

def p_var_cte1(p):
    'var_cte1   :'
    if program.current_id_is_func:
        print("func")
    else:
        #NOT FUNC
        if program.current_attribute == "":
            #id

            if len(program.pIDs[-1]) > 3:
                v_id = program.pIDs[-1][3]
                #program.VP.append(program.varTable[v_id].address)
                t = SparkyType()
                t.type = program.varTable[v_id].s_type.type
                program.pType.append(t)

            elif not program.pIDs[-1][1] and not program.pIDs[-1][2]:
                address = program.current_function.varTable[program.current_id].address
                program.VP.append(address)
                t = SparkyType()
                t.type = program.current_function.varTable[program.pIDs[-1][0]].s_type.type
                program.pType.append(t)
            #elif program.current_id_is_matrix:


        else:
            print("id with attribute")
            #id.id
            #id[1].id
            #id[1][2].id

    program.pIDs.pop()



def p_var_cte2(p):
    'var_cte2   :'
    #buscarla en memoria global, si no, meterla
    program.VP.append(("cte", int(p[-1])))
    t = SparkyType()
    t.type = "Int"
    program.pType.append(t)

def p_var_cte3(p):
    'var_cte3   :'
    #buscarla en memoria global, si no, meterla
    program.VP.append(("cte", float(p[-1])))
    t = SparkyType()
    t.type = "Float"
    program.pType.append(t)

def p_var_cte4(p):
    'var_cte4   :'
    #buscarla en memoria global, si no, meterla
    program.VP.append(("cte", bool(p[-1])))
    t = SparkyType()
    t.type = "Bool"
    program.pType.append(t)

def p_array(p):
    '''
    array   : LC expression array1 RC array_a array3
    | empty
    '''
def p_array_a(p):
    '''
    array_a  : LC expression array2 RC
    | empty
    '''

#  -----------------------------------------------------------------------
#  Neuro points for array
#  ################

def p_array1(p):
    'array1 :'
    #verifica que id es una variable dimensionada

    program.pOper.append('$')
    program.pArray.append(program.pIDs[-1][0])

    #changing
    x = program.pIDs.pop()
    program.pIDs.append((x[0], True, False))

    var = program.current_function.varTable[program.pIDs[-1][0]]
    row_type = program.pType[-1].type
    if row_type != "Int":
        print("ERROR to access array you need to provide Int index")
    else:
        program.current_quad = ("VER", 0, var.s_type.row - 1, program.VP[-1])
        program.add_quad()

def p_array2(p):
    'array2 :'
    #changing
    x = program.pIDs.pop()
    program.pIDs.append((x[0], False, True))
    var = program.current_function.varTable[program.pIDs[-1][0]]

    col_type = program.pType[-1].type
    if col_type != "Int":
        print("ERROR to access array you need to provide Int index")
    else:
        program.current_quad = ("VER", 0, var.s_type.col - 1, program.VP[-1])
        program.add_quad()

def p_array3(p):
    'array3 :'
    current_array = program.pArray.pop()
    base_address = program.current_function.varTable[current_array].address
    total_rows = program.current_function.varTable[current_array].s_type.row

    if program.pIDs[-1][1]:
        rows = program.VP.pop()
        rows_type = program.pType.pop()
        result = program.current_function.tempMemory.get_next_address(rows_type.type, 0, 0)
        program.current_quad = ("+", rows, ("cte", base_address), result)
        program.add_quad()
        program.VP.append(("pointer", result))
        
        t = SparkyType()
        "t.type = program.current_function.varTable[program.pIDs[-1][0]].s_type.type"
        #t.row = program.current_function.varTable[program.pIDs[-1][0]].s_type.type
        #t.col = program.current_function.varTable[program.pIDs[-1][0]].s_type.type
        program.pType.append(t)

    elif program.pIDs[-1][2]:
        #array
        cols = program.VP.pop()
        cols_type = program.pType.pop()
        rows = program.VP.pop()
        rows_type = program.pType.pop()
        result = program.current_function.tempMemory.get_next_address("Int", 0, 0)
        program.current_quad = ("*", rows, ("cte", total_rows), result)
        program.add_quad()

        result2 = program.current_function.tempMemory.get_next_address("Int", 0, 0)
        program.current_quad = ("+", result, cols, result2)
        program.add_quad()

        result3 = program.current_function.tempMemory.get_next_address("Int", 0, 0)
        program.current_quad = ("+", result2, ("cte", base_address), result3)
        program.add_quad()

        program.VP.append(("pointer", result3))
        t = SparkyType()
        t.type = program.current_function.varTable[program.pIDs[-1][0]].s_type.type
        program.pType.append(t)
    program.pOper.pop()


#  ################
#  -----------------------------------------------------------------------

def p_attribute(p):
    '''
    attribute   : DOT ID att1
    | empty
    '''


#  -----------------------------------------------------------------------
#  Neuro points for array
#  ################

def p_att1(p):
    'att1   :'
    #program.current_id_has_attr = True
    program.current_attribute = p[-1]


#  ################
#  -----------------------------------------------------------------------
def p_call_func(p):
    'call_func : call_f1 LP call_params RP'


def p_call_f1(p):
    'call_f1    :'
    program.called_function = program.funDir[program.pIDs[-1][0]]
    # program.funDir[program.pIDs.pop()]
    x = program.pIDs.pop()
    program.pIDs.append((x[0], x[1], x[2], program.called_function.address))
    program.current_param_num = 0
    program.current_quad = ("ERA", program.called_function.address, None, None)
    program.add_quad()
    program.pEras.append((program.called_function.return_type,program.called_function.address))

def p_call_func_optional(p):
    '''
    call_func_optional : call_func call_f3
    | empty
    '''

def p_call_f3(p):
    'call_f3    :'
    era_return = program.pEras.pop()
    program.current_quad = ("GOSUB", era_return[1], None, None)
    program.add_quad()
    if era_return[0].type == "void":
        print("ERROR Type MISMATCH")
        # pide memoria para tipo temporal
    address = program.current_function.tempMemory.get_next_address(era_return[0].type, era_return[0].row, era_return[0].col)
    program.current_quad = ("=", program.varTable[era_return[1]].address, None, address)
    program.add_quad()
    for x in program.VP:
        print(x)
    print(program.varTable[era_return[1]].address)
    program.VP.append(address)


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

def solveOperation():
    right_operand = program.VP.pop()
    right_type = program.pType.pop()
    left_operand = program.VP.pop()
    left_type = program.pType.pop()
    operator = program.pOper.pop()
    result_type = program.semanticCube.checkResult(operator, left_type.type, right_type.type)
    if result_type == "Error":
        print("TYPE MISMATCH, HELP in operation")
    else:
        result = program.current_function.tempMemory.get_next_address(result_type, 0, 0)
        program.current_quad = (operator, left_operand, right_operand, result)
        program.add_quad()
        program.VP.append(result)
        t = SparkyType()
        t.type = result_type
        program.pType.append(t)


if len(sys.argv) != 2:
    print("please provide exactly one argument")
else:
    with open(sys.argv[1], "r") as inputFile:
        data = inputFile.read()
    print(sys.argv[1])
    try:
        result = parser.parse(data)
    finally:
        print("VirtualMachine.execute()")
        program.print_quads()
        print("pJumps")
        for x in program.pJumps:
            print(x)
        print("VP")
        for x in program.VP:
            print(x)
        print("pOpers")
        for x in program.pOper:
            print(x)
        print("pType")
        for x in program.pType:
            print(x)
        print("pType")
        for x in program.pArray:
            print(x)
        print("pIDs")
        for x in program.pIDs:
            print(x)
        #vm = VirtualMachine()
        #vm.quads = program.Quads
        #vm.execute()

    if result is not None:
        print(result)
