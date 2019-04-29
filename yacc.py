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
    'program   : prog0 program_a program_c program_d main quads'

def p_quads(p):
    'quads :'
    program.print_quads()

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
    program.add_pJump()
    program.add_quad()
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
    # //total space needed

def p_type3(p):
    'type3  :'
    program.current_type.spark_type = p[-1]


def p_type4(p):
    'type4  :'
    if p[-1] not in program.ClassDir:
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
    'main   : main0 MAIN LP RP function_block'


def p_main0(p):
    'main0   :'
    program.fill_quad(program.BASE)
    program.function_stage = True
    program.current_stage = True
    program.current_function_name = "Main"
    program.new_function()
    program.funDir.set(program.current_function_name, program.current_function)
    program.current_function.varTable.set()

def p_function(p):
    'function   : FUNCTION fun0 ID fun1 LP fun2 params fun3 RP function_a function_block fun6'

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
    program.function_stage = True
    program.current_function.address = program.BASE

def p_fun1(p):
    'fun1   :'
    program.current_function_name = p[-1]
    if program.current_stage:#  I'm in the global scope
        if program.current_function_name in program.funDir:
            print('\033[91m' + "ERROR:" + '\033[0m' + "Function already declared before.")
    else:
        if program.current_function_name in program.current_class.funDir:
            print('\033[91m' + "ERROR:" + '\033[0m' + "Function already declared before in class")


def p_fun2(p):
    'fun2   :'
    program.new_params()

def p_fun3(p):
    'fun3   :'
    program.current_function.add_params(program.current_params)

def p_fun4(p):
    'fun4   :'
    program.current_function.ret = program.current_type

def p_fun5(p):
    'fun5   :'
    program.new_type()
    program.current_type.spark_type = "void"
    program.current_function.ret = program.current_type
    program.new_type()

def p_fun6(p):
    'fun6   :'
    program.current_quad = ("ENDPROC", None, None, None)
    program.add_quad()
    if program.current_stage:
        program.funDir.set(program.current_function_name, program.current_function)
        #  print(program.funDir[program.current_function_name].varTable.directory)
    if program.class_stage:
        program.current_class.funDir.set(program.current_function_name, program.current_function)
    program.new_function()

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

def p_param2(p):
    'param2 :'
    program.current_var.s_type = program.current_type
    if program.current_var_name in program.current_params:
        print('\033[91m' + "ERROR:" + '\033[0m' + "Function already has a parameter with that name.")
    else:
        program.current_params.set(program.current_var_name, program.current_var)

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
        print('\033[91m' + "ERROR:" + '\033[0m' + ": Class Already declared")
    else:
        program.current_class_name = p[-1]
        program.new_class()
        program.current_stage = False
        program.class_stage = True
        print(p[-1])

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
    program.current_class.funDir.set(program.current_function_name,program.current_function)

def p_class6(p):
    'class6 :'
    #  Better to add it at the end
    program.ClassDir.set(program.current_class_name, program.current_class)
    program.current_stage = True
    program.class_stage = False
    print(program.current_class.varTable.directory)

def p_class7(p):
    'class7 :'
    program.current_function_name = program.current_class_name

def p_class8(p):
    'class8 :'
    #  program.current_function.add_params(program.current_params)
    program.new_params()

def p_class9(p):
    'class9 :'
    #  this is wrong
    if program.current_class_name in program.funDir:
        print('\033[91m' + "ERROR:" + '\033[0m' + ": Init function for class already declared")
    else:
        program.current_function.add_params(program.current_params)
        program.current_type.spark_type = program.current_class_name
        program.current_function.ret = program.current_type
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
    'return : RETURN expression SEMICOL'

def p_obj(p):
    'obj : ID obj1 array attribute'

#  -----------------------------------------------------------------------
#  Neuro points for  obj
#  ################

def p_obj1(p):
    'obj1 :'
    program.current_id = p[-1] #  TODO:  if
    program.current_type = program.varTable[program.current_id].s_type
    program.new_attr()
    if program.current_type.is_object():
        print(program.current_id)
        program.current_id_is_object = True
    if program.current_type.s_type.is_matrix():
        program.current_id_is_matrix = True
    elif program.current_type.s_type.is_array():
        program.current_id_is_array = True 
#  ################
#  -----------------------------------------------------------------------
def p_assignement(p):
    'assignment : obj IS expression SEMICOL'

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
    program.pType.append("cte_s")
    program.VP.append(p[-1] + "\n")

def p_print2(p):
    'print2 : '
    program.pType.append("cte_s")
    program.VP.append("\n")

def p_print3(p):
    'print3 : '
    result = program.VP.pop()
    result_type = program.pType.pop()
    program.current_quad = ("WRITE", result, None, None)
    program.add_quad()


def p_input(p):
    'input  : INPUT LP obj RP SEMICOL'

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
    if exp_type != "Bool":
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


def p_call_function(p):
    'call_function  : obj cf1 call_func SEMICOL'


def p_cf1(p):
    'cf1    :'

    if not program.current_id_is_array and not program.current_id_is_matrix:
        if program.current_id_is_object and program.current_id_has_attr:
            if program.class_stage:
                var_local_to_class_fun = program.ClassDir[program.current_class_name].funDir[program.current_function_name].varTable
                if program.current_id in var_local_to_class_fun.objects:
                    s_type = var_local_to_class_fun[program.current_id].s_type
                    if program.current_attribute in program.ClassDir[s_type.spark_type].funDir:
                        program.called_function = program.ClassDir[s_type.spark_type].funDir[program.current_attribute]
                        address = program.called_function.address
                        program.current_quad = ("ERA", address, None, None)
                        program.add_quad()
                    else:
                        print('\033[91m' + "ERROR:" + '\033[0m' + "Object class has no" + program.current_attribute + " function defined")
                elif program.current_id in program.ClassDir[program.current_class_name].varTable:
                    s_type = program.ClassDir[program.current_class_name].varTable[program.current_id].s_type
                    if program.current_attribute in program.ClassDir[s_type.spark_type].funDir:
                        program.called_function = program.ClassDir[s_type.spark_type].funDir[program.current_attribute]
                        address = program.called_function.address
                        program.current_quad = ("ERA", address, None, None)
                        program.add_quad()
                    else:
                        print('\033[91m' + "ERROR:" + '\033[0m' + "Object class has no" + program.current_attribute + " function defined")
                else:
                    print('\033[91m' + "ERROR:" + '\033[0m' + "Object does not exist")

            elif program.function_stage and program.current_stage:
                if program.current_id in program.funDir[program.current_function_name].varTable.objects:
                    s_type = program.funDir[program.current_function_name].varTable[program.current_id].s_type
                    if program.current_attribute in program.ClassDir[s_type.spark_type].funDir:
                        program.called_function = program.ClassDir[s_type.spark_type].funDir[program.current_attribute]
                        address = program.called_function.address
                        program.current_quad = ("ERA", address, None, None)
                        program.add_quad()
                    else:
                        print('\033[91m' + "ERROR:" + '\033[0m' + "Object class has no" + program.current_attribute + " function defined")
                elif program.current_id in program.varTable.objects:
                    s_type = program.varTable[program.current_id].s_type
                    if program.current_attribute in program.ClassDir[s_type.spark_type].funDir:
                        program.called_function = program.ClassDir[s_type.spark_type].funDir[program.current_attribute]
                        address = program.called_function.address
                        program.current_quad = ("ERA", address, None, None)
                        program.add_quad()
                    else:
                        print('\033[91m' + "ERROR:" + '\033[0m' + "Object class has no" + program.current_attribute + " function defined")
        elif not program.current_id_is_object:
            print("")




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
            right_operand = program.VP.pop()
            right_type = program.pType.pop()
            left_operand = program.VP.pop()
            left_type = program.pType.pop()
            operator = program.pOper.pop()
            result_type = program.semanticCube.checkResult(operator, left_type, right_type)
            if result_type == "Error":
                print("TYPE MISMATCH, HELP")
            else:
                result = 999 #AVAIL.NEXT
                program.current_quad = (operator, left_operand, right_operand, result)
                program.add_quad()
                program.VP.append(result)
                program.pType.append(result_type)

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
            right_operand = program.VP.pop()
            right_type = program.pType.pop()
            left_operand = program.VP.pop()
            left_type = program.pType.pop()
            operator = program.pOper.pop()
            result_type = program.semanticCube.checkResult(operator, left_type, right_type)
            if result_type == "Error":
                print("TYPE MISMATCH, HELP")
            else:
                result = 999 #AVAIL.NEXT
                program.current_quad = (operator, left_operand, right_operand, result)
                program.add_quad()
                program.VP.append(result)
                program.pType.append(result_type)

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
            right_operand = program.VP.pop()
            right_type = program.pType.pop()
            left_operand = program.VP.pop()
            left_type = program.pType.pop()
            operator = program.pOper.pop()
            result_type = program.semanticCube.checkResult(operator, left_type, right_type)
            if result_type == "Error":
                print("TYPE MISMATCH, HELP")
            else:
                result = 999 #AVAIL.NEXT
                program.current_quad = (operator, left_operand, right_operand, result)
                program.add_quad()
                program.VP.append(result)
                program.pType.append(result_type)

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
            right_operand = program.VP.pop()
            right_type = program.pType.pop()
            left_operand = program.VP.pop()
            left_type = program.pType.pop()
            operator = program.pOper.pop()
            result_type = program.semanticCube.checkResult(operator, left_type, right_type)
            if result_type == "Error":
                print("TYPE MISMATCH, HELP")
            else:
                result = 999 #AVAIL.NEXT
                program.current_quad = (operator, left_operand, right_operand, result)
                program.add_quad()
                program.VP.append(result)
                program.pType.append(result_type)

def p_term2(p):
    'term2   :'
    program.pOper.append(p[-1])

def p_factor(p):
    '''
    factor  : LP factor1 expression RP factor2
    | factor_a var_cte factor3
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

def p_factor3(p):
    'factor3   :'
    program.VP.append("id")
    program.pType.append("Bool")

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
    array   : LC expression RC array4 array_a
    | array1
    '''
def p_array_a(p):
    '''
    array_a  : LC expression RC array3
    | array2
    '''

#  -----------------------------------------------------------------------
#  Neuro points for array
#  ################

def p_array1(p):
    'array1 :'
    if program.current_id_is_matrix or program.current_id_is_array:
        print('\033[91m' + "ERROR:" + '\033[0m' + ": variable is dimensional")

def p_array2(p):
    'array2 :'
    if program.current_id_is_matrix:
        print('\033[91m' + "ERROR:" + '\033[0m' + ": variable is a 2D Matrix - only 1 dimension stated")
    program.new_type()

def p_array3(p):
    'array3 :'
    if program.current_id_is_array:
        print('\033[91m' + "ERROR:" + '\033[0m' + ": variable is an Array - 2 dimension stated")

    program.current_quad = ("VER", 0, program.current_type.col, program.VP.pop())
    program.pType.pop()
    program.add_quad()
    program.new_type()

def p_array4(p):
    'array4 :'
    program.current_quad = ("VER", 0, program.current_type.row, program.VP.pop())
    program.pType.pop()
    program.add_quad()

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
    program.current_id_has_attr = True
    program.current_attribute = p[-1]


#  ################
#  -----------------------------------------------------------------------
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


with open("program2.sdfm", "r") as inputFile:
    data = inputFile.read()

result = parser.parse(data)

if result is not None:
    print(result)
