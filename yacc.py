# ------------------------------------------------------------
# yacc.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------
from copy import deepcopy

import ply.yacc as yacc
from lex import tokens
from program import Program
from varTable import Var
from sparky_type import SparkyType
from virtualMachine import VirtualMachine
import math
import sys

program = Program()
error_message = '\033[91m' + "ERROR: " + '\033[0m' 
error = False

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
    program.current_class_name = ""

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
    global error
    if p[-1] not in program.ClassDir:
        print(error_message + " Object Class has not been declared in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
        
         
         
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
    var_class   : VAR ID var_c1 COL type var_c2 SEMICOL
    |  VAR ID var_c1 COL typeM var_c2 SEMICOL
    '''


# -----------------------------------------------------------------------
# Neuro points var stage
#################

def p_var_c1(p):
    'var_c1    :'
    global error
    if program.current_scope == "global":
        if p[-1] in program.current_class.varTable.directory:
            print(error_message + "Variable already declared in line " + str(p.lexer.lineno) + ".")
            error = True
            sys.exit(0)

             
             
        else:
            program.current_var_name = p[-1]

    if program.current_scope == "function":
        if p[-1] in program.current_function.varTable:
            print(error_message + "Variable already declared in line " + str(p.lexer.lineno) + ".")
            error = True
            sys.exit(0)
             
             
        else:
            program.current_var_name = p[-1]


def p_var_c2(p):
    'var_c2    :'
    global error
    if program.current_scope == "global":
        program.current_var.s_type = program.current_type
        program.current_var.address = program.current_class.claMemory.get_next_address(program.current_var.s_type)
        if program.current_var.address is None:
            error = True
            sys.exit(0)
        if program.current_var.s_type.is_object():
                print(error_message + "Object class does not support objects in line " + str(p.lexer.lineno) + ".")
                error = True
                sys.exit(0)
                 
                 
        program.current_class.varTable.set(program.current_var_name, program.current_var)

    if program.current_scope == "function":
        program.current_var.s_type = program.current_type
        if program.current_var.s_type.is_object():
            program.new_object()
            s_type = program.current_var.s_type
            program.current_object.s_type = s_type;
            program.current_object.varTable.directory.update(deepcopy(program.ClassDir[s_type.type].varTable.directory))
            for key in program.ClassDir[program.current_var.s_type.type].varTable.directory:
                v_type      = program.current_object.varTable[key].s_type
                old_memo    = program.current_object.varTable[key].address
                address     = program.current_function.funMemory.get_next_address(v_type)
                if address is None:
                    error = True
                    sys.exit(0)
                program.current_object.memMap[address] = old_memo
                program.current_object.varTable[key].address = address
            program.current_function.varTable.objects[program.current_var_name] = program.current_object
        else:
            program.current_var.address = program.current_function.funMemory.get_next_address(program.current_type)
            if program.current_var.address is None:
                error = True
                sys.exit(0)

        program.current_function.varTable.set(program.current_var_name, program.current_var)

    program.current_var = Var()
    program.current_var_name = ""
    program.new_type()

#################
# -----------------------------------------------------------------------


def p_var(p):
    '''
    var    : VAR ID var1 COL type var2 SEMICOL
    |  VAR ID var1 COL typeM var2 SEMICOL
    '''
    
#-----------------------------------------------------------------------
# Neuro points var stage
#################

def p_var1(p):
    'var1    :'
    global error
    if program.current_scope == "global":
        if p[-1] in program.varTable:
            print(error_message + "Variable already declared in line " + str(p.lexer.lineno) + ".")
            error = True
            sys.exit(0)
             
             
        else:
            program.current_var_name = p[-1]
    if program.current_scope == "function":

        if p[-1] in program.current_function.varTable:
            print(error_message + "Variable already declared in line " + str(p.lexer.lineno) + ".")
            error = True
            sys.exit(0)
             
             
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
    global error
    if program.current_scope == "global":
        program.current_var.address = program.globalMemory.get_next_address(program.current_type)
        if program.current_var.address is None:
            error = True
            sys.exit(0)
        program.current_var.s_type = program.current_type
        program.varTable.set(program.current_var_name, program.current_var)
    if program.current_scope == "function":
        program.current_var.s_type = program.current_type
        if program.current_var.s_type.is_object():
            program.current_var.address = program.current_var_name
            program.new_object()
            s_type = program.current_var.s_type
            program.current_object.s_type = s_type;
            program.current_object.varTable.directory.update(deepcopy(program.ClassDir[s_type.type].varTable.directory))
            for key in program.ClassDir[program.current_var.s_type.type].varTable.directory:
                v_type      = program.current_object.varTable[key].s_type
                old_memo    = program.current_object.varTable[key].address
                address     = program.current_function.funMemory.get_next_address(v_type)
                if address is None:
                    error = True
                    sys.exit(0)
                program.current_object.memMap[address] = old_memo
                program.current_object.varTable[key].address = address
            program.current_function.varTable.objects[program.current_var_name] = program.current_object
        else:
            program.current_var.address = program.current_function.funMemory.get_next_address(program.current_type)
            if program.current_var.address is None:
                error = True
                sys.exit(0)

        program.current_function.varTable.set(program.current_var_name, program.current_var)



    program.current_var = Var()
    program.new_object()
    program.current_var_name = ""
    program.new_type()


def p_var4(p):
    'var4   :'
    program.current_value = ("cte", int(p[-1]))
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
    program.current_value = ("cte", float(p[-1]))
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
    if p[-1] == "true":
        program.current_value = ("cte", True)
    else:
        program.current_value = ("cte", False)
    program.current_type.type = "Bool"
    #current_assignation_right = "Bool"
    #  Same as 5 and 4 but could be
    #  initialized in memory from start

#################
#-----------------------------------------------------------------------

def p_let(p):
    'let    : LET ID let1 COL type let2 IS let_b SEMICOL let3'

def p_let_b(p):
    '''
    let_b   : CTE_I var4
    | CTE_F var5
    | CTE_B var6
    '''
#-----------------------------------------------------------------------
# Neuro points let stage
#################
def p_let1(p):
    'let1   :'
    global error
    program.current_var = Var()
    program.current_var.constant = True
    # current_stage -> global true, local false
    program.current_var_name = p[-1]

    if program.current_scope == "global":#global constant
        if p[-1] in program.varTable:
            print(error_message + " Variable already declared at line " + str(p.lexer.lineno) + ".")
            error = True
            sys.exit(0)
             
             
    elif program.current_scope == "function":
        if p[-1] in program.current_function.varTable:
            print(error_message + " Variable already declared at line " + str(p.lexer.lineno) + ".")
            error = True
            sys.exit(0)
             
             


def p_let2(p):
    'let2   :'
    global error
    program.current_var.s_type = program.current_type
    if program.current_scope == "global":
        program.current_var.address = program.globalMemory.get_next_address(program.current_type)
        if program.current_var.address is None:
            error = True
            sys.exit(0)
        program.varTable.set(program.current_var_name, program.current_var)
    elif program.current_scope == "function":
        #print("function:")
        #print(program.current_function.address)
        program.current_var.address = program.current_function.funMemory.get_next_address(program.current_type)
        if program.current_var.address is None:
            error = True
            sys.exit(0)
        program.current_function.varTable.set(program.current_var_name, program.current_var)
    
    # ONLY WORKS FOR GLOBAL MEMORY
    # reset
    # current_var_name , value, type, etc?
    program.new_type()

def p_let3(p):
    'let3   :'
    global error
    #check semantic cube
    #CHECK MAYBE FAILS ON GLOBAL MEMORY
    result = program.semanticCube.checkResult("=", program.current_var.s_type.type, program.current_type.type)
    if result == "Error":
        print(error_message + " Type missmatch at line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         

    #ya se salio, entonces... hacer el cuadruplo con
    if program.current_scope == "global":
        quad = ("=", program.current_value, None, program.current_var.address)
        program.pendingQuads.append(quad)
    elif program.current_scope == "function":
        program.current_quad = ("=", program.current_value, None, program.current_var.address)
        program.add_quad()

    program.new_var()


    

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
    program.current_scope = "function"
    program.current_function_name = "main"
    for quad in list(program.pendingQuads):
        program.current_quad = quad
        program.add_quad()
        program.pendingQuads.remove(quad)
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
    program.current_function.address = program.BASE


def p_fun1(p):
    'fun1   :'
    global error
    program.current_function_name = p[-1]
    if program.current_scope == "global" and program.current_class_name == "":
        if program.current_function_name in program.funDir:
            print(error_message + "Function already declared before in line " + str(p.lexer.lineno) + ".")
            error = True
            sys.exit(0)
             
             
        else:
            program.funDir.set(program.current_function_name, program.current_function)
    else:
        if program.current_function_name in program.current_class.funDir:
            print(error_message + "Function already declared before in class in line " + str(p.lexer.lineno) + ".")            
            error = True
            sys.exit(0)
             
             

    program.current_scope = "function"

def p_fun3(p):
    'fun3   :'

def p_fun4(p):
    'fun4   :'
    global error
    program.current_function.return_type = program.current_type
    program.new_var()
    program.current_var_name = program.current_function.address
    t = program.current_function.return_type
    program.current_var.address = program.globalMemory.get_next_address(t)
    if program.current_var.address is None:
        error = True
        sys.exit(0)
    program.current_var.s_type = program.current_type
    program.varTable.set(program.current_var_name, program.current_var)
    #pide memoria global con nombre
    program.new_var()

def p_fun5(p):
    'fun5   :'
    program.new_var()
    program.current_function.return_type.type = "void"

def p_fun6(p):
    'fun6   :'
    program.current_quad = ("ENDPROC", None, None, None)
    program.add_quad()
    program.current_scope = "global"

# ################
#  ------------------------------------------------------------------------


def p_params(p):
    '''
    params   : param0 ID param1 COL params_b param2 params_a
    | empty
    '''

def p_params_a(p):
    '''
    params_a   : COMMA params
    | empty
    '''
    

def p_params_b(p):
    '''
    params_b   : typeM
    | type
    '''
#  -----------------------------------------------------------------------
#  Neuro points for params in function
#  ################

def p_param0(p):
    'param0 :'
    program.new_var()

def p_param1(p):
    'param1 :'
    global error
    program.current_var_name = p[-1]
    if program.current_var_name in program.current_function.varTable.directory:
        print(error_message + "Function already has a parameter with that name in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         

def p_param2(p):
    'param2 :'
    global error
    program.current_var.is_param = True
    program.current_var.s_type = program.current_type
    s_type = program.current_type
    #program.current_var.address = program.current_function.funMemory.get_next_address(s_type)
    #program.current_function.varTable.set(program.current_var_name, program.current_var)
    #program.current_function.param_key.append((s_type, program.current_var.address))
    if s_type.is_object():
        program.new_object()
        program.current_object.s_type = s_type
        program.current_object.varTable.directory.update(deepcopy(program.ClassDir[s_type.type].varTable.directory))
        for key in program.ClassDir[program.current_var.s_type.type].varTable.directory:
            v_type = program.current_object.varTable[key].s_type
            old_memo = program.current_object.varTable[key].address
            address = program.current_function.funMemory.get_next_address(v_type)
            if address is None:
                error = True
                sys.exit(0)
            program.current_object.memMap[address] = old_memo
            program.current_object.varTable[key].address = address
        program.current_function.varTable.objects[program.current_var_name] = program.current_object

        program.current_function.param_key.append((s_type, program.current_object.memMap))
        program.new_object()
    else:
        program.current_var.address = program.current_function.funMemory.get_next_address(s_type)
        if program.current_var.address is None:
            error = True
            sys.exit(0)
        program.current_function.param_key.append((s_type, program.current_var.address))

    program.current_function.varTable.set(program.current_var_name, program.current_var)

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
    class_b : class_f class_b
    | empty
    '''

def p_class_f(p):
    'class_f : var_class'

# class_d = optional ->  recursive(optional(private)function)
def p_class_d(p):
    '''
    class_d : function class5 class_d
    | class6
    '''

#-----------------------------------------------------------------------
# Neuro points for class
#################

def p_class1(p):
    'class1 :'
    global error
    program.new_class()
    program.class_stage = True
    if p[-1] in program.ClassDir:
        print(error_message + "Class already declared in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
    else:
        program.current_class_name = p[-1]

def p_class2(p):
    'class2 :'
    global error
    if p[-1] not in program.ClassDir:
        print(error_message + "Father class has not been declared in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
    #  This is inheritance copy all as deepcopy
    program.inherit_class(p[-1])

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
    global error
    if program.current_class_name in program.funDir:
        print(error_message + "Init function for class already declared in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
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
    'init   : INIT class7 LP RP class8 SEMICOL class9'

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
    global error
    result = program.VP.pop()
    result_type = program.pType.pop()
    if result_type.check_type(program.current_function.return_type):
        program.current_quad = ("RETURN", result, None, program.varTable[program.current_function.address].address)
        program.add_quad()
    else:
        print(error_message + "Type missmatch in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         


def p_obj(p):
    'obj : ID obj1 array attribute obj2'



#  -----------------------------------------------------------------------
#  Neuro points for  obj
#  ################

def p_obj1(p):
    'obj1 :'
    program.pOper.append("$")
    program.pIDs.append((p[-1],False, False, None))

def p_obj2(p):
    'obj2 :'
    program.pOper.pop()

#  ################
#  -----------------------------------------------------------------------
def p_assignment(p):
    'assignment : obj IS assignment1 expression assignment2 SEMICOL'

def p_assignment1(p):
    'assignment1 :'
    global error
    # OBJ = . EXPRESSION ;
    #buscar que exista en tabla de variables local y asi

    if program.pIDs[-1][0] in program.current_function.varTable:
        
        #id = . expression
        #is_object
        t = program.current_function.varTable[program.pIDs[-1][0]].s_type
        if t.row > 0:
            #print("array or matrix")
            program.pOper.append("=")

        elif t.is_object():
            #id is object
            #TODO: CHECAR QUE OBJETO EXISTA
            if not program.pIDs[-1][3] is None:
                if program.pIDs[-1][3] in program.current_function.varTable.objects[program.pIDs[-1][0]].varTable:
                    attribute_address = program.current_function.varTable.objects[program.pIDs[-1][0]].varTable[program.pIDs[-1][3]].address
                    attribute_type = program.current_function.varTable.objects[program.pIDs[-1][0]].varTable[program.pIDs[-1][3]].s_type

                    program.VP.append(attribute_address)
                    program.pType.append(attribute_type)
                    program.pOper.append("=")
                else:
                    print(error_message + "Unkown attribute " + program.pIDs[-1][3] + " for object " + program.pIDs[-1][0] + " in line " + str(p.lexer.lineno) + ".")
                    error = True
                    sys.exit(0)
            else:
                print(error_message + "You are trying to assign value to object in line " + str(p.lexer.lineno) + ".")
                error = True
                sys.exit(0)

        else:
            program.VP.append(program.current_function.varTable[program.pIDs[-1][0]].address)
            program.pType.append(program.current_function.varTable[program.pIDs[-1][0]].s_type)
            program.pOper.append("=")
    elif program.current_class_name != "":
        if program.pIDs[-1][0] in program.current_class.varTable:
            var = program.current_class.varTable[program.pIDs[-1][0]]
            t = program.current_class.varTable[program.pIDs[-1][0]].s_type
            if t.row > 0:
                #print("array or matrix")
                program.pOper.append("=")
                # program.pType.append(program.current_function.varTable[program.pIDs[-1][0]].s_type)
                # print("ERROR YOU ARE TRYING TO ASSIGN VALUE TO ARRAY OBJECT")
            elif t.is_object():
                # id is object
                print(error_message + "You are trying to assign value to object in line " + str(p.lexer.lineno) + ".")
                error = True
                sys.exit(0)
                 
                 
            else:
                program.VP.append(program.current_class.varTable[program.pIDs[-1][0]].address)
                program.pType.append(program.current_class.varTable[program.pIDs[-1][0]].s_type)
                program.pOper.append("=")

    elif program.pIDs[-1][0] in program.varTable:
        print("Global")
    else:
        print(error_message + "Variable not declared in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
    #program.current_id = ""
    

def p_assignment2(p):
    'assignment2 :'
    global error
    #var = program.current_function.varTable[program.pIDs[-1][0]]
    if program.pIDs[-1][0] in program.current_function.varTable:
        var = program.current_function.varTable[program.pIDs[-1][0]]
    elif program.current_class_name != "":
        if program.pIDs[-1][0] in program.current_class.varTable:
            var = program.current_class.varTable[program.pIDs[-1][0]]
        elif program.pIDs[-1][0] in program.varTable:
            var = program.varTable[program.pIDs[-1][0]]
        else:
            print(error_message + "Unkown variable "+ program.pIDs[-1][0] + " in line " + str(p.lexer.lineno) + ".")
            error = True
            sys.exit(0)
    elif program.pIDs[-1][0] in program.varTable:
        var = program.varTable[program.pIDs[-1][0]]
    else:
        print(error_message + "Unkown variable "+ program.pIDs[-1][0] + " in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)

    if var.constant:
        print(error_message + "Cannot assign value to a constant: "+ program.pIDs[-1][0] + " in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)

    #se sale con el sys.exit(0)
    program.pIDs.pop()
    right_type = program.pType.pop()
    right_operand = program.VP.pop()
    left_type = program.pType.pop()
    left_operand = program.VP.pop()
    operator = program.pOper.pop()
    result_type = program.semanticCube.checkResult(operator, left_type.type, right_type.type)
    if result_type == "Error":
        print(error_message + "Type missmatch in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
        
         
    else:
        #if var.is_param:
        #    program.current_quad = (operator, right_operand, None, ("pointer", left_operand))
        #else:
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
    global error
    x = program.pIDs.pop()
    if not x[1] and not x[2]:
        #id simple
        if x[0] in program.current_function.varTable:
            address = program.current_function.varTable[x[0]].address
            type = program.current_function.varTable[x[0]].s_type.type
            program.current_quad = ("INPUT", type, None, address)
            program.add_quad()
        else:
            print(error_message + "Variable not declared in line " + str(p.lexer.lineno) + ".")
            error = True
            sys.exit(0)
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
    global error
    exp_type = program.pType.pop()
    if exp_type.type != "Bool":
        print(error_message + "Type missmatch in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
        
         
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
    program.pOper.pop()
    program.pIDs.pop()
    era_return = program.pEras.pop()
    program.current_quad = ("GOSUB", era_return[1], None, None)
    program.add_quad()
    if era_return[3][0]:
        for paramo in era_return[3][2]:
            #print(paramo)
            program.current_quad = paramo
            program.add_quad()
        program.current_quad = ("GOSUBO", era_return[3][0], None, None)
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
    global error
    if (program.current_param_num + 1) > len(program.called_function.param_key):
        print(error_message + "Function has 1 more argument than expected in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         

    popped_type = program.pType.pop()
    fun_param_type = program.called_function.param_key[program.current_param_num][0]
    
    if fun_param_type.check_type(popped_type):
        if popped_type.is_object():
            #aosdnasijdnsioadfj
            id = program.VP.pop()
            paramID = 0
            for var in program.current_function.varTable.objects[id].memMap:
                l = list(program.called_function.param_key[program.current_param_num][1].items())
                togo = l[paramID][0]
                program.current_quad = ("PARAM", var, None, togo)
                program.add_quad()
                paramID += 1
            program.current_param_num += 1
        else:
            #print("not object ")
            if popped_type.row is 0:
                program.current_quad = ("PARAM", program.VP.pop(), None, program.called_function.param_key[program.current_param_num][1])
                #print(program.called_function.param_key[program.current_param_num][0].type)
                program.add_quad()
                program.current_param_num += 1
            else:
                total = 1;
                if popped_type.col > 0:
                    total = popped_type.row * popped_type.col;
                else:
                    total = popped_type.row
                program.current_quad = ("PARAM", program.VP.pop(), total, program.called_function.param_key[program.current_param_num][1])
                #print(program.called_function.param_key[program.current_param_num][0].type)
                program.add_quad()
                program.current_param_num += 1
    else:
        print(error_message + "Parameter given is of wrong type in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         



def p_call_param2(p):
    'call_param2    :'
    global error
    if len(program.called_function.param_key) != program.current_param_num:
        print(error_message + "Function expecting another parameter in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         

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
    global error
    program.pJumps.append("$")
    exp_type = program.pType.pop()
    if exp_type.type != "Bool":
        print(error_message + "Type missmatch in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
    else:
        result = program.VP.pop()
        program.add_pJump()
        program.current_quad = ("GOTOF", result, None, None)
        program.add_quad()

def p_condition2(p):
    'condition2 : '
    global error
    program.fill_quad(program.BASE + 1)
    program.add_pJump()
    program.current_quad = ("GOTO", None, None, None)
    program.add_quad()

def p_condition5(p):
    'condition5 : '
    exp_type = program.pType.pop()
    if exp_type.type != "Bool":
        print(error_message + "Type missmatch in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
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
    'elseif : ELSEIF condition2 expression condition5 block'

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
            solveOperation(p)

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
            solveOperation(p)

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
            solveOperation(p)

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
            solveOperation(p)

def p_term2(p):
    'term2   :'
    program.pOper.append(p[-1])

def p_factor(p):
    '''
    factor  : LP factor1 expression RP factor2
    | factor_a var_cte
    '''

def p_factor_a(p):
    '''
    factor_a    : MINUS factor3
    | NOT factor3
    | empty factor4
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
    'factor3 : '
    #TODO: FONDO FALSO?
    program.pOper.append("$")
    program.pOper.append(p[-1])

def p_factor4(p):
    'factor4 : '
    #TODO: FONDO FALSO?
    program.pOper.append("$")

def p_var_cte(p):
    '''
    var_cte : obj call_func_optional var_cte1 var_cte5
    | CTE_I var_cte2 var_cte5
    | CTE_F var_cte3 var_cte5
    | CTE_B var_cte4 var_cte5
    '''

def p_var_cte1(p):
    'var_cte1   :'
    global error
    if program.current_id_is_func:
        print("func")
    else:
        #NOT FUNC
        if program.pIDs[-1][3] is None:
            #id
            if len(program.pIDs[-1]) > 4:#function
                #todo: checar que sea función
                v_id = program.pIDs[-1][4]
                #program.VP.append(program.varTable[v_id].address)
                t = SparkyType()
                t = program.varTable[v_id].s_type
                program.pType.append(t)
            elif not program.pIDs[-1][1] and not program.pIDs[-1][2]:
                #checar que no sea array de verdad
                if program.current_scope == "function":
                    if program.pIDs[-1][0] in program.current_function.varTable:
                        tp = program.current_function.varTable[program.pIDs[-1][0]].s_type
                        address = program.current_function.varTable[program.pIDs[-1][0]].address
                        program.VP.append(address)
                        t = SparkyType()
                        t = program.current_function.varTable[program.pIDs[-1][0]].s_type
                        program.pType.append(t)
                    elif program.current_class_name != "":


                        if program.pIDs[-1][0] in program.current_class.varTable:
                            tp = program.current_class.varTable[program.pIDs[-1][0]].s_type
                            address = program.current_class.varTable[program.pIDs[-1][0]].address
                            program.VP.append(address)
                            t = SparkyType()
                            t = program.current_class.varTable[program.pIDs[-1][0]].s_type
                            program.pType.append(t)
                        elif program.pIDs[-1][0] in program.varTable:
                            tp = program.varTable[program.pIDs[-1][0]].s_type
                            address = program.varTable[program.pIDs[-1][0]].address
                            program.VP.append(address)
                            t = SparkyType()
                            t = program.varTable[program.pIDs[-1][0]].s_type
                            program.pType.append(t)
                        else:
                            print(error_message + "Unkown variable "+ program.pIDs[-1][0] + " in line " + str(p.lexer.lineno) + ".")
                            error = True
                    elif program.pIDs[-1][0] in program.varTable:
                        tp = program.varTable[program.pIDs[-1][0]].s_type
                        address = program.varTable[program.pIDs[-1][0]].address
                        program.VP.append(address)
                        t = SparkyType()
                        t = program.varTable[program.pIDs[-1][0]].s_type
                        program.pType.append(t)
                    else:
                        print(error_message + "Unkown variable "+ program.pIDs[-1][0] + " in line " + str(p.lexer.lineno) + ".")
                        error = True
                        sys.exit(0)
                else:

                 #not array and not matrix
                    if program.pIDs[-1][0] in program.current_function.varTable.directory:
                        if program.current_function.varTable[program.pIDs[-1][0]].s_type.is_object():
                            print(error_message + "Cannot print object" + " in line " + str(p.lexer.lineno) + ".")
                            error = True
                            sys.exit(0)
                             
                             
                        else:
                            address = program.current_function.varTable[program.pIDs[-1][0]].address
                            program.VP.append(address)
                            t = SparkyType()
                            t = program.current_function.varTable[program.pIDs[-1][0]].s_type
                            program.pType.append(t)
                    else:
                        address = program.current_class.varTable[program.pIDs[-1][0]].address
                        program.VP.append(address)
                        t = SparkyType()
                        t = program.current_class.varTable[program.pIDs[-1][0]].s_type
                        program.pType.append(t)


        else:
            if len(program.pIDs[-1]) > 4:#function
                v_id = program.pIDs[-1][4]
                #program.VP.append(program.varTable[v_id].address)
                t = SparkyType()
                t = program.varTable[v_id].s_type
                program.pType.append(t)
            else:

                #TODO: CHECAR que si sea un atributo valido jeje
                attribute_address = program.current_function.varTable.objects[program.pIDs[-1][0]].varTable[program.pIDs[-1][3]].address
                attribute_type = program.current_function.varTable.objects[program.pIDs[-1][0]].varTable[program.pIDs[-1][3]].s_type
                program.VP.append(attribute_address)
                program.pType.append(attribute_type)
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
    if p[-1] == "true":
        program.VP.append(("cte", True))
    else:
        program.VP.append(("cte", False))
    t = SparkyType()
    t.type = "Bool"
    program.pType.append(t)

def p_var_cte5(p):
    'var_cte5   :'
    global error
    if len(program.pOper) > 0:
        operator = program.pOper[-1]
        if operator == "-" or operator == "!":
            operator = program.pOper.pop()
            result = program.VP.pop()
            t = program.pType.pop()
            res_address = program.current_function.tempMemory.get_next_address(t)
            if res_address is None:
                error = True
                sys.exit(0)
            program.current_quad = (operator, result, None, res_address)
            program.add_quad()
            program.VP.append(res_address)
            program.pType.append(t)

    program.pOper.pop()





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
    global error
    #verifica que id es una variable dimensionada

    program.pOper.append('$')
    program.pArray.append(program.pIDs[-1][0])

    #changing
    x = program.pIDs.pop()
    program.pIDs.append((x[0], True, False, None))

    var = program.current_function.varTable[program.pIDs[-1][0]]
    row_type = program.pType[-1].type
    if row_type != "Int":
        print(error_message + "To access array you need to provide Int index in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
    else:
        
        program.current_quad = ("VER", 0, var.s_type.row - 1, program.VP[-1])
        
        program.add_quad()

def p_array2(p):
    'array2 :'
    global error
    #changing
    x = program.pIDs.pop()
    program.pIDs.append((x[0], False, True, None))
    var = program.current_function.varTable[program.pIDs[-1][0]]

    col_type = program.pType[-1].type
    if col_type != "Int":
        print(error_message + "To access array you need to provide Int index in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
    else:
        program.current_quad = ("VER", 0, var.s_type.col - 1, program.VP[-1])
        program.add_quad()

def p_array3(p):
    'array3 :'
    global error
    current_array = program.pArray.pop()
    base_address = program.current_function.varTable[current_array].address
    total_rows = program.current_function.varTable[current_array].s_type.row
    var = program.current_function.varTable[program.pIDs[-1][0]]

    if program.pIDs[-1][1]:
        rows = program.VP.pop()
        rows_type = program.pType.pop()
        t = SparkyType()
        t.type = "Int"
        result = program.current_function.tempMemory.get_next_address(t)
        if result is None:
            error = True
            sys.exit(0)
        if var.is_param:
            program.current_quad = ("+", rows, ("pointer", base_address), result)
        else:
            program.current_quad = ("+", rows, ("cte", base_address), result)
        program.add_quad()
        program.VP.append(("pointer", result))
        
        t = SparkyType()
        t.type = program.current_function.varTable[program.pIDs[-1][0]].s_type.type
        t.row = 0
        t.col = 0
        #t.row = program.current_function.varTable[program.pIDs[-1][0]].s_type.type
        #t.col = program.current_function.varTable[program.pIDs[-1][0]].s_type.type
        program.pType.append(t)

    elif program.pIDs[-1][2]:
        #array
        cols = program.VP.pop()
        cols_type = program.pType.pop()
        rows = program.VP.pop()
        rows_type = program.pType.pop()
        t = SparkyType()
        t.type = "Int"
        result = program.current_function.tempMemory.get_next_address(t)
        if result is None:
            error = True
            sys.exit(0)
        program.current_quad = ("*", rows, ("cte", total_rows), result)
        program.add_quad()

        result2 = program.current_function.tempMemory.get_next_address(t)
        if result2 is None:
            error = True
            sys.exit(0)
        program.current_quad = ("+", result, cols, result2)
        program.add_quad()

        result3 = program.current_function.tempMemory.get_next_address(t)
        if result3 is None:
            error = True
            sys.exit(0)
        if var.is_param:
            program.current_quad = ("+", result2, ("pointer", base_address), result3)
        else:
            program.current_quad = ("+", result2, ("cte", base_address), result3)
        #program.current_quad = ("+", result2, ("cte", base_address), result3)
        program.add_quad()

        program.VP.append(("pointer", result3))
        t = SparkyType()
        t = program.current_function.varTable[program.pIDs[-1][0]].s_type
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
    x = program.pIDs.pop()
    program.pIDs.append((x[0], x[1], x[2], p[-1]))


#  ################
#  -----------------------------------------------------------------------
def p_call_func(p):
    'call_func : call_f1 LP call_params RP'


def p_call_f1(p):
    'call_f1    :'
    global error
    #TODO : checar si la función existe en la funcDir Neccesaria o en clase
    program.pOper.append("$")
    if program.pIDs[-1][3] is None:
        program.called_function = program.funDir[program.pIDs[-1][0]]
        # program.funDir[program.pIDs.pop()]
        x = program.pIDs.pop()
        program.pIDs.append((x[0], x[1], x[2], x[3], program.called_function.address))
        program.current_param_num = 0
        program.current_quad = ("ERA", program.called_function.address, None, None)
        program.add_quad()
        program.pEras.append((program.called_function.return_type, program.called_function.address, False, (False,)))
    else:
        #id . id ( * )
        current_id = program.pIDs[-1][0]
        attribute = program.pIDs[-1][3]
        s_type = program.current_function.varTable[current_id].s_type
        program.current_quad = ("ERAO", current_id, None, None)
        program.add_quad()
        paramo_list = []
        if current_id in program.current_function.varTable.objects:
            for address in program.current_function.varTable.objects[current_id].memMap:
                old_memo = program.current_function.varTable.objects[current_id].memMap[address]
                program.current_quad = ("PARAMO", address, None, old_memo)
                program.add_quad()
                paramo_list.append(("=", old_memo, None, address))
            # Termina PARAMOs
            program.called_function = program.ClassDir[s_type.type].funDir[attribute]
            #program.called_function = program.funDir[program.pIDs[-1][0]]
            x = program.pIDs.pop()
            program.pIDs.append((x[0], x[1], x[2], x[3], program.called_function.address))
            program.current_param_num = 0
            program.current_quad = ("ERA", program.called_function.address, None, None)
            program.add_quad()
            program.pEras.append((program.called_function.return_type, program.called_function.address, True, (True, current_id, paramo_list)))
        else:
            print(error_message + "Function not found for variable " + current_id + " in line " +  str(p.lexer.lineno) + ".")
            error = True
            sys.exit(0)



def p_call_func_optional(p):
    '''
    call_func_optional : call_func call_f3
    | empty
    '''

def p_call_f3(p):
    'call_f3    :'
    global error
    program.pOper.pop()
    era_return = program.pEras.pop()
    program.current_quad = ("GOSUB", era_return[1], None, None)
    program.add_quad()
    if era_return[0].type == "void":
        print(error_message + "Type missmatch in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
        # pide memoria para tipo temporal
    if era_return[3][0]:
        for paramo in era_return[3][2]:
            #print(paramo)
            program.current_quad = paramo
            program.add_quad()
        program.current_quad = ("GOSUBO", era_return[3][1], None, None)
        program.add_quad()
    address = program.current_function.tempMemory.get_next_address(era_return[0])
    if address is None:
        error = True
        sys.exit(0)
    program.current_quad = ("=", program.varTable[era_return[1]].address, None, address)
    program.add_quad()
    program.VP.append(address)

    #if era_return[2]:
    #    t = era_return[0]
    #    program.pType.append(t)


#no need for comment since lexer ignores it


def p_empty(p):
    'empty :'

# Error rule for syntax errors
def p_error(p):
    global error
    if p:
        print(error_message + "Unexpected token '" + str(p.value) + "' at line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
        #print(p.type)
    else:
        print(error_message + "Syntax error at EOF")
        error = True
        sys.exit(0)
         
         


# Build the parser
parser = yacc.yacc(start='program')

def solveOperation(p):
    global error
    right_operand = program.VP.pop()
    right_type = program.pType.pop()
    left_operand = program.VP.pop()
    left_type = program.pType.pop()
    operator = program.pOper.pop()
    result_type = program.semanticCube.checkResult(operator, left_type.type, right_type.type)
    if result_type == "Error":
        print(error_message + "Type missmatch in operation in line " + str(p.lexer.lineno) + ".")
        error = True
        sys.exit(0)
         
         
    else:
        t = SparkyType()
        t.type = result_type
        result = program.current_function.tempMemory.get_next_address(t)
        if result is None:
            error = True
            sys.exit(0)
        program.current_quad = (operator, left_operand, right_operand, result)
        program.add_quad()
        program.VP.append(result)
        program.pType.append(t)


if len(sys.argv) != 2:
    print(error_message + "Please provide exactly one argument")
    error = True
    sys.exit(0)
     
     
else:
    with open(sys.argv[1], "r") as inputFile:
        data = inputFile.read()
    try:
        result = parser.parse(data)
    finally:
        if not error:
            #print("VirtualMachine.execute()")
            #program.print_quads()
            #print("pJumps")
            #for x in program.pJumps:
            #    print(x)
            #print("VP")
            #for x in program.VP:
            #    print(x)
            #print("pOpers")
            #for x in program.pOper:
            #    print(x)
            #print("pType")
            #for x in program.pType:
            #    print(x)
            #print("pType")
            #for x in program.pArray:
            #    print(x)
            #print("pIDs")
            #for x in program.pIDs:
            #    print(x)
            #print("pendingQuads")
            #for x in program.pendingQuads:
            #    print(x)
            #print("eras")
            #for x in program.pEras:
            #    print(x)
            #for cla in program.ClassDir.directory:
            #    print("Class: " + cla + "{")
            #    for var in program.ClassDir[cla].varTable.directory:
            #        if program.ClassDir[cla].varTable[var].s_type.is_object():
            #            print("object: " + var)
            #            for o_var in program.ClassDir[cla].varTable.objects[var].varTable.directory:
            #                print('{:.40s} {}'.format('\tvar: '+o_var + (' ' + '.' * 10), "address: " + str(program.ClassDir[cla].varTable.objects[var].varTable[o_var].address)))
            #        else:
            #            print('{:.40s} {}'.format('  var: ' + var + (' ' + '.' * 10), "address: " + str(program.ClassDir[cla].varTable[var].address)))
            #    for fun in program.ClassDir[cla].funDir.directory:
            #        print()
            #        print("function: " + fun+"{")
            #        for var in program.ClassDir[cla].funDir[fun].varTable.directory:
            #            if program.ClassDir[cla].funDir[fun].varTable[var].s_type.is_object():
            #                print("object: " + var)
            #                for o_var in program.ClassDir[cla].funDir[fun].varTable.objects[var].varTable.directory:
            #                    print('{:.40s} {}'.format('\tvar: ' + o_var + (' ' + '.' * 10), "address: " + str(
            #                        program.ClassDir[cla].funDir[fun].varTable.objects[var].varTable[o_var].address)))
            #            else:
            #                print('{:.40s} {}'.format('var: ' + var + (' ' + '.' * 10),
            #                                          "address: " + str(program.ClassDir[cla].funDir[fun].varTable[var].address)))
            #        print("}")
            #    print("}"+ "class "+ cla + " END")
            #for fun in program.funDir.directory:
            #    print()
            #    print("function: " + fun+"{")
            #    for var in program.funDir[fun].varTable.directory:
            #        print(var)
            #        print(program.funDir[fun].varTable[var].s_type.is_object())
            #        print(program.funDir[fun].varTable[var].s_type.type)
            #        print(program.funDir[fun].varTable[var].s_type.row)
            #        print(program.funDir[fun].varTable[var].s_type.col)
            #        if program.funDir[fun].varTable[var].s_type.is_object():
            #            print("object: " + var)
            #            for o_var in program.funDir[fun].varTable.objects[var].varTable.directory:
            #                print('{:.40s} {}'.format('\tvar: '+o_var + (' ' + '.' * 10), "address: " + str(program.funDir[fun].varTable.objects[var].varTable[o_var].address)))
            #        else:
            #            print('{:.40s} {}'.format('var: ' + var + (' ' + '.' * 10), "address: " + str(program.funDir[fun].varTable[var].address)))
            #    print("}")
            vm = VirtualMachine()
            vm.quads = program.Quads
            vm.execute()


    if result is not None:
        print(result)




