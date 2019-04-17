
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND ARROW BOOL CLASS COL COMMA CTE_B CTE_F CTE_I CTE_S DIV DOT ELSE ELSEIF EQUAL FLOAT FUNCTION GEQ GT ID IF INIT INPUT INT IS LB LC LEQ LET LP LT MAIN MINUS MUL NEQ NOT OR PLUS PRINT PRIVATE RB RC RETURN RP SEMICOL VAR WHILEprogram   : prog0 program_a lol program_c program_d mainlol   : \n    program_a  : program_b program_a\n    | empty\n    \n    program_b  : let prog1\n    | class prog2\n    \n    program_c  : var prog3 program_c\n    | empty\n    \n    program_d  : function prog4 program_d\n    | empty\n    prog0    :prog1  :prog2  :prog3  :prog4  :\n    type    : type0 atomic\n    \n    typeM    : type0 LC CTE_I RC LC CTE_I RC atomic type1\n    | type0 LC CTE_I RC atomic type2\n    | type0 ID type4\n    type0  :type1  :type2  :type3  :type4  :\n    atomic  : INT type3\n    | FLOAT type3\n    | BOOL type3\n    \n    var    : VAR ID var1 COL type var2 var_a SEMICOL\n    |  VAR ID var1 COL typeM SEMICOL var2\n    \n    var_a   : IS var_b var3\n    | empty\n    \n    var_b   : CTE_I var4\n    | CTE_F var5\n    | CTE_B var6\n    var1    :var2    :var3    :var4   :var5   :var6   :let    : LET ID let1 COL type let2 IS var_b SEMICOL let3let1   :let2   :let3   :main   : MAIN LP RP function_blockfunction   : FUNCTION ID LP params RP function_a function_block\n    function_a   : ARROW type\n    | empty\n    \n    params   : ID COL type params_a\n    | empty\n    \n    params_a   : COMMA params\n    | empty\n    block  : LB block_a RB\n    block_a : statement block_a\n    | empty\n    function_block   : LB function_block_a block_a RB\n    function_block_a   : function_block_b function_block_a\n    | empty\n    \n    function_block_b : var\n    | let\n    class     : CLASS ID class1 class_a LB class_b init class_c class_d RB\n    class_a   : COL ID\n    | empty\n    \n    class_b : class_e class_f class_b\n    | empty\n    \n    class_e : PRIVATE\n    | empty\n    \n    class_f : var\n    | let\n    \n    class_c : init class_c\n    | empty\n    \n    class_d : class_e function class_d\n    | empty\n    class1 :init   : INIT LP params RP block\n    statement : print\n    | input\n    | assignment\n    | condition\n    | loop\n    | call_function\n    | return\n    return : RETURN expression SEMICOLobj : ID array attributeassignment : obj IS expression SEMICOLprint : PRINT LP print_a RP SEMICOL\n    print_a : expression\n    | CTE_S\n    | empty\n    input  : INPUT LP obj RP SEMICOLloop   : WHILE expression blockcall_function  : obj call_func SEMICOL\n    call_params    : expression call_params_a\n    | empty\n    \n    call_params_a  : COMMA expression call_params_a\n    | empty\n    condition  : IF expression block condition_a condition_b\n    condition_a  : elseif condition_a\n    | empty\n    \n    condition_b : else\n    | empty\n    elseif : ELSEIF expression blockelse   : ELSE blockexpression : comparison expression_a\n    expression_a    : AND comparison expression_a\n    | OR comparison\n    | empty\n    comparison    : exp comparison_a\n    comparison_a  : comparison_b exp comparison_a\n    | empty\n    \n    comparison_b  : GEQ\n    | LEQ\n    | GT\n    | LT\n    | EQUAL\n    | NEQ\n    exp    : term exp_a\n    exp_a   : PLUS term exp_a\n    | MINUS term exp_a\n    | empty\n    term    : factor term_a\n    term_a   : MUL factor term_a\n    | DIV factor term_a\n    | empty\n    \n    factor  : LP expression RP\n    | factor_a var_cte\n    \n    factor_a    : MINUS\n    | NOT\n    | empty\n    \n    var_cte : obj call_func_optional\n    | CTE_I\n    | CTE_F\n    | CTE_B\n    \n    array   : LC expression RC array_a\n    | empty\n    \n    array_a  : LC expression RC\n    | empty\n    \n    attribute   : DOT ID\n    | empty\n    call_func : LP call_params RP\n    call_func_optional : call_func\n    | empty\n    empty :'
    
_lr_action_items = {'LET':([0,2,4,6,7,12,13,40,52,53,54,68,69,70,72,76,89,91,92,100,103,135,138,139,],[-11,8,8,-12,-13,-5,-6,-143,8,-67,-66,-143,-68,-69,8,-36,8,-59,-60,-29,-44,-28,-41,-61,]),'CLASS':([0,2,4,6,7,12,13,103,138,139,],[-11,9,9,-12,-13,-5,-6,-44,-41,-61,]),'VAR':([0,2,3,4,5,6,7,10,11,12,13,17,26,40,52,53,54,68,69,70,72,76,89,91,92,100,103,135,138,139,],[-11,-143,-2,-143,-4,-12,-13,19,-3,-5,-6,-14,19,-143,19,-67,-66,-143,-68,-69,19,-36,19,-59,-60,-29,-44,-28,-41,-61,]),'FUNCTION':([0,2,3,4,5,6,7,10,11,12,13,16,17,18,23,26,34,36,54,66,76,83,84,85,100,103,107,109,110,133,135,138,139,140,142,169,243,],[-11,-143,-2,-143,-4,-12,-13,-143,-3,-5,-6,25,-14,-8,-15,-143,25,-7,-66,-143,-36,-143,-143,-71,-29,-44,-70,25,-67,-46,-28,-41,-61,-143,-56,-75,-53,]),'MAIN':([0,2,3,4,5,6,7,10,11,12,13,16,17,18,22,23,24,26,34,36,43,76,100,103,133,135,138,139,142,],[-11,-143,-2,-143,-4,-12,-13,-143,-3,-5,-6,-143,-14,-8,33,-15,-10,-143,-143,-7,-9,-36,-29,-44,-46,-28,-41,-61,-56,]),'$end':([1,32,71,142,],[0,-1,-45,-56,]),'ID':([8,9,19,25,30,44,45,61,72,76,86,88,89,90,91,92,100,103,113,115,116,117,118,119,120,121,125,126,127,129,131,135,138,144,145,146,148,154,155,156,157,158,162,170,174,177,180,181,183,184,187,189,190,191,192,193,194,196,197,200,201,209,210,212,220,223,225,226,227,228,243,244,245,247,248,249,251,259,264,265,],[14,15,27,35,41,56,-20,78,-143,-36,56,128,-143,-58,-59,-60,-29,-44,128,-76,-77,-78,-79,-80,-81,-82,-143,-143,-143,-57,56,-28,-41,-143,128,-143,-143,-143,128,-127,-128,-129,-143,128,-129,-92,-129,-143,-143,-143,-143,-111,-112,-113,-114,-115,-116,-143,-143,-143,-143,-91,-83,240,-85,-143,-143,-143,-99,-143,-53,-86,-90,-97,-100,-101,-98,-143,-103,-102,]),'COL':([14,15,20,21,27,37,56,],[-42,-74,28,30,-35,45,73,]),'LB':([15,21,29,31,41,47,48,49,50,55,63,64,65,74,94,96,128,134,141,149,150,151,152,153,159,161,163,182,185,186,188,195,198,199,202,204,205,206,207,208,211,213,221,229,230,231,232,233,234,235,236,237,238,239,240,241,250,252,253,254,255,256,257,258,260,261,268,],[-74,-143,40,-63,-62,-16,-23,-23,-23,72,-25,-26,-27,-143,72,-48,-143,-47,170,170,-143,-143,-143,-143,170,-143,-135,-104,-107,-108,-110,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,-143,-106,-143,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,170,170,-105,-109,-118,-119,-122,-123,-134,-137,-136,]),'INT':([28,39,45,61,73,95,137,242,],[-20,48,-20,48,-20,-20,48,48,]),'FLOAT':([28,39,45,61,73,95,137,242,],[-20,49,-20,49,-20,-20,49,49,]),'BOOL':([28,39,45,61,73,95,137,242,],[-20,50,-20,50,-20,-20,50,50,]),'LP':([33,35,67,122,123,124,125,126,127,128,144,146,148,154,161,162,163,183,184,187,189,190,191,192,193,194,196,197,200,201,205,211,213,223,228,240,241,259,260,261,268,],[42,44,86,144,145,148,154,154,154,-143,154,154,154,154,-143,154,-135,154,154,154,-111,-112,-113,-114,-115,-116,154,154,154,154,148,-84,-139,154,154,-138,-143,154,-134,-137,-136,]),'IS':([38,46,47,48,49,50,59,63,64,65,75,124,128,161,163,211,213,240,241,260,261,268,],[-43,62,-16,-23,-23,-23,-36,-25,-26,-27,98,146,-143,-143,-135,-84,-139,-138,-143,-134,-137,-136,]),'PRIVATE':([40,66,68,69,70,76,83,84,85,100,103,107,133,135,138,140,142,169,243,],[54,-143,54,-68,-69,-36,-143,54,-71,-29,-44,-70,-46,-28,-41,54,-56,-75,-53,]),'INIT':([40,51,53,66,68,69,70,76,83,87,100,103,135,138,169,243,],[-143,67,-65,67,-143,-68,-69,-36,67,-64,-29,-44,-28,-41,-75,-53,]),'RP':([42,44,47,48,49,50,57,58,63,64,65,86,93,111,128,130,131,132,144,148,150,151,152,153,161,163,164,171,172,173,174,175,178,179,180,182,185,186,188,195,198,199,202,203,204,205,206,207,208,211,213,221,222,224,229,230,231,232,233,234,235,236,237,238,239,240,241,246,253,254,255,256,257,258,260,261,263,268,],[55,-143,-16,-23,-23,-23,74,-50,-25,-26,-27,-143,-143,141,-143,-49,-143,-52,-143,-143,-143,-143,-143,-143,-143,-135,-51,218,-87,-88,-89,219,221,-143,-94,-104,-107,-108,-110,-117,-120,-121,-124,236,-126,-143,-131,-132,-133,-84,-139,-140,-93,-96,-143,-106,-143,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-143,-105,-109,-118,-119,-122,-123,-134,-137,-95,-136,]),'LC':([45,61,128,137,241,],[-20,77,162,166,259,]),'SEMICOL':([47,48,49,50,59,60,63,64,65,75,78,79,80,81,82,97,99,102,104,105,106,128,136,147,150,151,152,153,160,161,163,165,167,176,182,185,186,188,195,198,199,202,204,205,206,207,208,211,213,216,218,219,221,229,230,231,232,233,234,235,236,237,238,239,240,241,253,254,255,256,257,258,260,261,262,267,268,],[-16,-23,-23,-23,-36,76,-25,-26,-27,-143,-24,103,-38,-39,-40,135,-31,-19,-32,-33,-34,-143,-37,177,-143,-143,-143,-143,210,-143,-135,-30,-22,220,-104,-107,-108,-110,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-18,244,245,-140,-143,-106,-143,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-105,-109,-118,-119,-122,-123,-134,-137,-21,-17,-136,]),'COMMA':([47,48,49,50,63,64,65,93,128,150,151,152,153,161,163,179,182,185,186,188,195,198,199,202,204,205,206,207,208,211,213,221,229,230,231,232,233,234,235,236,237,238,239,240,241,246,253,254,255,256,257,258,260,261,268,],[-16,-23,-23,-23,-25,-26,-27,131,-143,-143,-143,-143,-143,-143,-135,223,-104,-107,-108,-110,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,-143,-106,-143,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,223,-105,-109,-118,-119,-122,-123,-134,-137,-136,]),'CTE_I':([62,77,98,125,126,127,144,146,148,154,155,156,157,158,162,166,174,180,183,184,187,189,190,191,192,193,194,196,197,200,201,223,228,259,],[80,101,80,-143,-143,-143,-143,-143,-143,-143,206,-127,-128,-129,-143,215,-129,-129,-143,-143,-143,-111,-112,-113,-114,-115,-116,-143,-143,-143,-143,-143,-143,-143,]),'CTE_F':([62,98,125,126,127,144,146,148,154,155,156,157,158,162,174,180,183,184,187,189,190,191,192,193,194,196,197,200,201,223,228,259,],[81,81,-143,-143,-143,-143,-143,-143,-143,207,-127,-128,-129,-143,-129,-129,-143,-143,-143,-111,-112,-113,-114,-115,-116,-143,-143,-143,-143,-143,-143,-143,]),'CTE_B':([62,98,125,126,127,144,146,148,154,155,156,157,158,162,174,180,183,184,187,189,190,191,192,193,194,196,197,200,201,223,228,259,],[82,82,-143,-143,-143,-143,-143,-143,-143,208,-127,-128,-129,-143,-129,-129,-143,-143,-143,-111,-112,-113,-114,-115,-116,-143,-143,-143,-143,-143,-143,-143,]),'RB':([66,72,76,83,84,85,88,89,90,91,92,100,103,107,108,110,112,113,114,115,116,117,118,119,120,121,129,133,135,138,140,142,143,168,169,170,177,181,209,210,217,220,225,226,227,243,244,245,247,248,249,251,264,265,],[-143,-143,-36,-143,-143,-71,-143,-143,-58,-59,-60,-29,-44,-70,139,-73,142,-143,-55,-76,-77,-78,-79,-80,-81,-82,-57,-46,-28,-41,-143,-56,-54,-72,-75,-143,-92,-143,-91,-83,243,-85,-143,-143,-99,-53,-86,-90,-97,-100,-101,-98,-103,-102,]),'PRINT':([72,76,88,89,90,91,92,100,103,113,115,116,117,118,119,120,121,129,135,138,170,177,181,209,210,220,225,226,227,243,244,245,247,248,249,251,264,265,],[-143,-36,122,-143,-58,-59,-60,-29,-44,122,-76,-77,-78,-79,-80,-81,-82,-57,-28,-41,122,-92,-143,-91,-83,-85,-143,-143,-99,-53,-86,-90,-97,-100,-101,-98,-103,-102,]),'INPUT':([72,76,88,89,90,91,92,100,103,113,115,116,117,118,119,120,121,129,135,138,170,177,181,209,210,220,225,226,227,243,244,245,247,248,249,251,264,265,],[-143,-36,123,-143,-58,-59,-60,-29,-44,123,-76,-77,-78,-79,-80,-81,-82,-57,-28,-41,123,-92,-143,-91,-83,-85,-143,-143,-99,-53,-86,-90,-97,-100,-101,-98,-103,-102,]),'IF':([72,76,88,89,90,91,92,100,103,113,115,116,117,118,119,120,121,129,135,138,170,177,181,209,210,220,225,226,227,243,244,245,247,248,249,251,264,265,],[-143,-36,125,-143,-58,-59,-60,-29,-44,125,-76,-77,-78,-79,-80,-81,-82,-57,-28,-41,125,-92,-143,-91,-83,-85,-143,-143,-99,-53,-86,-90,-97,-100,-101,-98,-103,-102,]),'WHILE':([72,76,88,89,90,91,92,100,103,113,115,116,117,118,119,120,121,129,135,138,170,177,181,209,210,220,225,226,227,243,244,245,247,248,249,251,264,265,],[-143,-36,126,-143,-58,-59,-60,-29,-44,126,-76,-77,-78,-79,-80,-81,-82,-57,-28,-41,126,-92,-143,-91,-83,-85,-143,-143,-99,-53,-86,-90,-97,-100,-101,-98,-103,-102,]),'RETURN':([72,76,88,89,90,91,92,100,103,113,115,116,117,118,119,120,121,129,135,138,170,177,181,209,210,220,225,226,227,243,244,245,247,248,249,251,264,265,],[-143,-36,127,-143,-58,-59,-60,-29,-44,127,-76,-77,-78,-79,-80,-81,-82,-57,-28,-41,127,-92,-143,-91,-83,-85,-143,-143,-99,-53,-86,-90,-97,-100,-101,-98,-103,-102,]),'ARROW':([74,],[95,]),'RC':([101,128,150,151,152,153,161,163,182,185,186,188,195,198,199,202,204,205,206,207,208,211,213,214,215,221,229,230,231,232,233,234,235,236,237,238,239,240,241,253,254,255,256,257,258,260,261,266,268,],[137,-143,-143,-143,-143,-143,-143,-135,-104,-107,-108,-110,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,241,242,-140,-143,-106,-143,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-105,-109,-118,-119,-122,-123,-134,-137,268,-136,]),'MINUS':([125,126,127,128,144,146,148,152,153,154,161,162,163,183,184,187,189,190,191,192,193,194,196,197,199,200,201,202,204,205,206,207,208,211,213,221,223,228,232,233,234,235,236,237,238,239,240,241,257,258,259,260,261,268,],[156,156,156,-143,156,156,156,197,-143,156,-143,156,-135,156,156,156,-111,-112,-113,-114,-115,-116,156,156,-121,156,156,-124,-126,-143,-131,-132,-133,-84,-139,-140,156,156,197,197,-143,-143,-125,-130,-141,-142,-138,-143,-122,-123,156,-134,-137,-136,]),'NOT':([125,126,127,144,146,148,154,162,183,184,187,189,190,191,192,193,194,196,197,200,201,223,228,259,],[157,157,157,157,157,157,157,157,157,157,157,-111,-112,-113,-114,-115,-116,157,157,157,157,157,157,157,]),'DOT':([128,161,163,241,260,261,268,],[-143,212,-135,-143,-134,-137,-136,]),'MUL':([128,153,161,163,204,205,206,207,208,211,213,221,234,235,236,237,238,239,240,241,260,261,268,],[-143,200,-143,-135,-126,-143,-131,-132,-133,-84,-139,-140,200,200,-125,-130,-141,-142,-138,-143,-134,-137,-136,]),'DIV':([128,153,161,163,204,205,206,207,208,211,213,221,234,235,236,237,238,239,240,241,260,261,268,],[-143,201,-143,-135,-126,-143,-131,-132,-133,-84,-139,-140,201,201,-125,-130,-141,-142,-138,-143,-134,-137,-136,]),'PLUS':([128,152,153,161,163,199,202,204,205,206,207,208,211,213,221,232,233,234,235,236,237,238,239,240,241,257,258,260,261,268,],[-143,196,-143,-143,-135,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,196,196,-143,-143,-125,-130,-141,-142,-138,-143,-122,-123,-134,-137,-136,]),'GEQ':([128,151,152,153,161,163,195,198,199,202,204,205,206,207,208,211,213,221,231,232,233,234,235,236,237,238,239,240,241,255,256,257,258,260,261,268,],[-143,189,-143,-143,-143,-135,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,189,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-118,-119,-122,-123,-134,-137,-136,]),'LEQ':([128,151,152,153,161,163,195,198,199,202,204,205,206,207,208,211,213,221,231,232,233,234,235,236,237,238,239,240,241,255,256,257,258,260,261,268,],[-143,190,-143,-143,-143,-135,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,190,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-118,-119,-122,-123,-134,-137,-136,]),'GT':([128,151,152,153,161,163,195,198,199,202,204,205,206,207,208,211,213,221,231,232,233,234,235,236,237,238,239,240,241,255,256,257,258,260,261,268,],[-143,191,-143,-143,-143,-135,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,191,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-118,-119,-122,-123,-134,-137,-136,]),'LT':([128,151,152,153,161,163,195,198,199,202,204,205,206,207,208,211,213,221,231,232,233,234,235,236,237,238,239,240,241,255,256,257,258,260,261,268,],[-143,192,-143,-143,-143,-135,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,192,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-118,-119,-122,-123,-134,-137,-136,]),'EQUAL':([128,151,152,153,161,163,195,198,199,202,204,205,206,207,208,211,213,221,231,232,233,234,235,236,237,238,239,240,241,255,256,257,258,260,261,268,],[-143,193,-143,-143,-143,-135,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,193,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-118,-119,-122,-123,-134,-137,-136,]),'NEQ':([128,151,152,153,161,163,195,198,199,202,204,205,206,207,208,211,213,221,231,232,233,234,235,236,237,238,239,240,241,255,256,257,258,260,261,268,],[-143,194,-143,-143,-143,-135,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,194,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-118,-119,-122,-123,-134,-137,-136,]),'AND':([128,150,151,152,153,161,163,186,188,195,198,199,202,204,205,206,207,208,211,213,221,229,231,232,233,234,235,236,237,238,239,240,241,254,255,256,257,258,260,261,268,],[-143,183,-143,-143,-143,-143,-135,-108,-110,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,183,-143,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-109,-118,-119,-122,-123,-134,-137,-136,]),'OR':([128,150,151,152,153,161,163,186,188,195,198,199,202,204,205,206,207,208,211,213,221,229,231,232,233,234,235,236,237,238,239,240,241,254,255,256,257,258,260,261,268,],[-143,184,-143,-143,-143,-143,-135,-108,-110,-117,-120,-121,-124,-126,-143,-131,-132,-133,-84,-139,-140,184,-143,-143,-143,-143,-143,-125,-130,-141,-142,-138,-143,-109,-118,-119,-122,-123,-134,-137,-136,]),'CTE_S':([144,],[173,]),'ELSEIF':([181,226,243,265,],[228,228,-53,-102,]),'ELSE':([181,225,226,227,243,251,265,],[-143,250,-143,-99,-53,-98,-102,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'prog0':([0,],[2,]),'program_a':([2,4,],[3,11,]),'program_b':([2,4,],[4,4,]),'empty':([2,4,10,16,21,26,34,40,44,66,68,72,74,75,83,84,86,88,89,93,113,125,126,127,128,131,140,144,146,148,150,151,152,153,154,161,162,170,179,181,183,184,187,196,197,200,201,205,223,225,226,228,229,231,232,233,234,235,241,246,259,],[5,5,18,24,31,18,24,53,58,85,53,90,96,99,85,110,58,114,90,132,114,158,158,158,163,58,110,174,158,180,185,188,198,202,158,213,158,114,224,227,158,158,158,158,158,158,158,239,158,249,227,158,185,188,198,198,202,202,261,224,158,]),'let':([2,4,52,72,89,],[6,6,70,92,92,]),'class':([2,4,],[7,7,]),'lol':([3,],[10,]),'prog1':([6,],[12,]),'prog2':([7,],[13,]),'program_c':([10,26,],[16,36,]),'var':([10,26,52,72,89,],[17,17,69,91,91,]),'let1':([14,],[20,]),'class1':([15,],[21,]),'program_d':([16,34,],[22,43,]),'function':([16,34,109,],[23,23,140,]),'prog3':([17,],[26,]),'class_a':([21,],[29,]),'main':([22,],[32,]),'prog4':([23,],[34,]),'var1':([27,],[37,]),'type':([28,45,73,95,],[38,59,93,134,]),'type0':([28,45,73,95,],[39,61,39,39,]),'let2':([38,],[46,]),'atomic':([39,61,137,242,],[47,47,167,262,]),'class_b':([40,68,],[51,87,]),'class_e':([40,68,84,140,],[52,52,109,109,]),'params':([44,86,131,],[57,111,164,]),'typeM':([45,],[60,]),'type3':([48,49,50,],[63,64,65,]),'init':([51,66,83,],[66,83,83,]),'class_f':([52,],[68,]),'function_block':([55,94,],[71,133,]),'var2':([59,76,],[75,100,]),'var_b':([62,98,],[79,136,]),'class_c':([66,83,],[84,107,]),'function_block_a':([72,89,],[88,129,]),'function_block_b':([72,89,],[89,89,]),'function_a':([74,],[94,]),'var_a':([75,],[97,]),'type4':([78,],[102,]),'var4':([80,],[104,]),'var5':([81,],[105,]),'var6':([82,],[106,]),'class_d':([84,140,],[108,168,]),'block_a':([88,113,170,],[112,143,217,]),'statement':([88,113,170,],[113,113,113,]),'print':([88,113,170,],[115,115,115,]),'input':([88,113,170,],[116,116,116,]),'assignment':([88,113,170,],[117,117,117,]),'condition':([88,113,170,],[118,118,118,]),'loop':([88,113,170,],[119,119,119,]),'call_function':([88,113,170,],[120,120,120,]),'return':([88,113,170,],[121,121,121,]),'obj':([88,113,145,155,170,],[124,124,175,205,124,]),'params_a':([93,],[130,]),'let3':([103,],[138,]),'call_func':([124,205,],[147,238,]),'expression':([125,126,127,144,146,148,154,162,223,228,259,],[149,159,160,172,176,179,203,214,246,252,266,]),'comparison':([125,126,127,144,146,148,154,162,183,184,223,228,259,],[150,150,150,150,150,150,150,150,229,230,150,150,150,]),'exp':([125,126,127,144,146,148,154,162,183,184,187,223,228,259,],[151,151,151,151,151,151,151,151,151,151,231,151,151,151,]),'term':([125,126,127,144,146,148,154,162,183,184,187,196,197,223,228,259,],[152,152,152,152,152,152,152,152,152,152,152,232,233,152,152,152,]),'factor':([125,126,127,144,146,148,154,162,183,184,187,196,197,200,201,223,228,259,],[153,153,153,153,153,153,153,153,153,153,153,153,153,234,235,153,153,153,]),'factor_a':([125,126,127,144,146,148,154,162,183,184,187,196,197,200,201,223,228,259,],[155,155,155,155,155,155,155,155,155,155,155,155,155,155,155,155,155,155,]),'array':([128,],[161,]),'var3':([136,],[165,]),'block':([141,149,159,250,252,],[169,181,209,264,265,]),'print_a':([144,],[171,]),'call_params':([148,],[178,]),'expression_a':([150,229,],[182,253,]),'comparison_a':([151,231,],[186,254,]),'comparison_b':([151,231,],[187,187,]),'exp_a':([152,232,233,],[195,255,256,]),'term_a':([153,234,235,],[199,257,258,]),'var_cte':([155,],[204,]),'attribute':([161,],[211,]),'type2':([167,],[216,]),'call_params_a':([179,246,],[222,263,]),'condition_a':([181,226,],[225,251,]),'elseif':([181,226,],[226,226,]),'call_func_optional':([205,],[237,]),'condition_b':([225,],[247,]),'else':([225,],[248,]),'array_a':([241,],[260,]),'type1':([262,],[267,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> prog0 program_a lol program_c program_d main','program',6,'p_program','yacc.py',15),
  ('lol -> <empty>','lol',0,'p_lol','yacc.py',18),
  ('program_a -> program_b program_a','program_a',2,'p_program_a','yacc.py',25),
  ('program_a -> empty','program_a',1,'p_program_a','yacc.py',26),
  ('program_b -> let prog1','program_b',2,'p_program_b','yacc.py',30),
  ('program_b -> class prog2','program_b',2,'p_program_b','yacc.py',31),
  ('program_c -> var prog3 program_c','program_c',3,'p_program_c','yacc.py',35),
  ('program_c -> empty','program_c',1,'p_program_c','yacc.py',36),
  ('program_d -> function prog4 program_d','program_d',3,'p_program_d','yacc.py',41),
  ('program_d -> empty','program_d',1,'p_program_d','yacc.py',42),
  ('prog0 -> <empty>','prog0',0,'p_prog0','yacc.py',48),
  ('prog1 -> <empty>','prog1',0,'p_prog1','yacc.py',56),
  ('prog2 -> <empty>','prog2',0,'p_prog2','yacc.py',62),
  ('prog3 -> <empty>','prog3',0,'p_prog3','yacc.py',70),
  ('prog4 -> <empty>','prog4',0,'p_prog4','yacc.py',75),
  ('type -> type0 atomic','type',2,'p_type','yacc.py',84),
  ('typeM -> type0 LC CTE_I RC LC CTE_I RC atomic type1','typeM',9,'p_typeM','yacc.py',90),
  ('typeM -> type0 LC CTE_I RC atomic type2','typeM',6,'p_typeM','yacc.py',91),
  ('typeM -> type0 ID type4','typeM',3,'p_typeM','yacc.py',92),
  ('type0 -> <empty>','type0',0,'p_type0','yacc.py',101),
  ('type1 -> <empty>','type1',0,'p_type1','yacc.py',106),
  ('type2 -> <empty>','type2',0,'p_type2','yacc.py',113),
  ('type3 -> <empty>','type3',0,'p_type3','yacc.py',120),
  ('type4 -> <empty>','type4',0,'p_type4','yacc.py',127),
  ('atomic -> INT type3','atomic',2,'p_atomic','yacc.py',137),
  ('atomic -> FLOAT type3','atomic',2,'p_atomic','yacc.py',138),
  ('atomic -> BOOL type3','atomic',2,'p_atomic','yacc.py',139),
  ('var -> VAR ID var1 COL type var2 var_a SEMICOL','var',8,'p_var','yacc.py',152),
  ('var -> VAR ID var1 COL typeM SEMICOL var2','var',7,'p_var','yacc.py',153),
  ('var_a -> IS var_b var3','var_a',3,'p_var_a','yacc.py',159),
  ('var_a -> empty','var_a',1,'p_var_a','yacc.py',160),
  ('var_b -> CTE_I var4','var_b',2,'p_var_b','yacc.py',165),
  ('var_b -> CTE_F var5','var_b',2,'p_var_b','yacc.py',166),
  ('var_b -> CTE_B var6','var_b',2,'p_var_b','yacc.py',167),
  ('var1 -> <empty>','var1',0,'p_var1','yacc.py',174),
  ('var2 -> <empty>','var2',0,'p_var2','yacc.py',190),
  ('var3 -> <empty>','var3',0,'p_var3','yacc.py',196),
  ('var4 -> <empty>','var4',0,'p_var4','yacc.py',199),
  ('var5 -> <empty>','var5',0,'p_var5','yacc.py',214),
  ('var6 -> <empty>','var6',0,'p_var6','yacc.py',225),
  ('let -> LET ID let1 COL type let2 IS var_b SEMICOL let3','let',10,'p_let','yacc.py',234),
  ('let1 -> <empty>','let1',0,'p_let1','yacc.py',239),
  ('let2 -> <empty>','let2',0,'p_let2','yacc.py',264),
  ('let3 -> <empty>','let3',0,'p_let3','yacc.py',278),
  ('main -> MAIN LP RP function_block','main',4,'p_main','yacc.py',286),
  ('function -> FUNCTION ID LP params RP function_a function_block','function',7,'p_function','yacc.py',289),
  ('function_a -> ARROW type','function_a',2,'p_function_a','yacc.py',293),
  ('function_a -> empty','function_a',1,'p_function_a','yacc.py',294),
  ('params -> ID COL type params_a','params',4,'p_params','yacc.py',299),
  ('params -> empty','params',1,'p_params','yacc.py',300),
  ('params_a -> COMMA params','params_a',2,'p_params_a','yacc.py',305),
  ('params_a -> empty','params_a',1,'p_params_a','yacc.py',306),
  ('block -> LB block_a RB','block',3,'p_block','yacc.py',310),
  ('block_a -> statement block_a','block_a',2,'p_block_a','yacc.py',315),
  ('block_a -> empty','block_a',1,'p_block_a','yacc.py',316),
  ('function_block -> LB function_block_a block_a RB','function_block',4,'p_function_block','yacc.py',320),
  ('function_block_a -> function_block_b function_block_a','function_block_a',2,'p_function_block_a','yacc.py',324),
  ('function_block_a -> empty','function_block_a',1,'p_function_block_a','yacc.py',325),
  ('function_block_b -> var','function_block_b',1,'p_function_block_b','yacc.py',330),
  ('function_block_b -> let','function_block_b',1,'p_function_block_b','yacc.py',331),
  ('class -> CLASS ID class1 class_a LB class_b init class_c class_d RB','class',10,'p_class','yacc.py',341),
  ('class_a -> COL ID','class_a',2,'p_class_a','yacc.py',345),
  ('class_a -> empty','class_a',1,'p_class_a','yacc.py',346),
  ('class_b -> class_e class_f class_b','class_b',3,'p_class_b','yacc.py',351),
  ('class_b -> empty','class_b',1,'p_class_b','yacc.py',352),
  ('class_e -> PRIVATE','class_e',1,'p_class_e','yacc.py',357),
  ('class_e -> empty','class_e',1,'p_class_e','yacc.py',358),
  ('class_f -> var','class_f',1,'p_class_f','yacc.py',363),
  ('class_f -> let','class_f',1,'p_class_f','yacc.py',364),
  ('class_c -> init class_c','class_c',2,'p_class_c','yacc.py',369),
  ('class_c -> empty','class_c',1,'p_class_c','yacc.py',370),
  ('class_d -> class_e function class_d','class_d',3,'p_class_d','yacc.py',375),
  ('class_d -> empty','class_d',1,'p_class_d','yacc.py',376),
  ('class1 -> <empty>','class1',0,'p_class1','yacc.py',384),
  ('init -> INIT LP params RP block','init',5,'p_init','yacc.py',395),
  ('statement -> print','statement',1,'p_statement','yacc.py',399),
  ('statement -> input','statement',1,'p_statement','yacc.py',400),
  ('statement -> assignment','statement',1,'p_statement','yacc.py',401),
  ('statement -> condition','statement',1,'p_statement','yacc.py',402),
  ('statement -> loop','statement',1,'p_statement','yacc.py',403),
  ('statement -> call_function','statement',1,'p_statement','yacc.py',404),
  ('statement -> return','statement',1,'p_statement','yacc.py',405),
  ('return -> RETURN expression SEMICOL','return',3,'p_return','yacc.py',409),
  ('obj -> ID array attribute','obj',3,'p_obj','yacc.py',412),
  ('assignment -> obj IS expression SEMICOL','assignment',4,'p_assignement','yacc.py',415),
  ('print -> PRINT LP print_a RP SEMICOL','print',5,'p_print','yacc.py',418),
  ('print_a -> expression','print_a',1,'p_print_a','yacc.py',422),
  ('print_a -> CTE_S','print_a',1,'p_print_a','yacc.py',423),
  ('print_a -> empty','print_a',1,'p_print_a','yacc.py',424),
  ('input -> INPUT LP obj RP SEMICOL','input',5,'p_input','yacc.py',427),
  ('loop -> WHILE expression block','loop',3,'p_loop','yacc.py',430),
  ('call_function -> obj call_func SEMICOL','call_function',3,'p_call_function','yacc.py',433),
  ('call_params -> expression call_params_a','call_params',2,'p_call_params','yacc.py',437),
  ('call_params -> empty','call_params',1,'p_call_params','yacc.py',438),
  ('call_params_a -> COMMA expression call_params_a','call_params_a',3,'p_call_params_a','yacc.py',442),
  ('call_params_a -> empty','call_params_a',1,'p_call_params_a','yacc.py',443),
  ('condition -> IF expression block condition_a condition_b','condition',5,'p_condition','yacc.py',446),
  ('condition_a -> elseif condition_a','condition_a',2,'p_condition_a','yacc.py',450),
  ('condition_a -> empty','condition_a',1,'p_condition_a','yacc.py',451),
  ('condition_b -> else','condition_b',1,'p_condition_b','yacc.py',456),
  ('condition_b -> empty','condition_b',1,'p_condition_b','yacc.py',457),
  ('elseif -> ELSEIF expression block','elseif',3,'p_elseif','yacc.py',461),
  ('else -> ELSE block','else',2,'p_else','yacc.py',464),
  ('expression -> comparison expression_a','expression',2,'p_expression','yacc.py',467),
  ('expression_a -> AND comparison expression_a','expression_a',3,'p_expression_a','yacc.py',471),
  ('expression_a -> OR comparison','expression_a',2,'p_expression_a','yacc.py',472),
  ('expression_a -> empty','expression_a',1,'p_expression_a','yacc.py',473),
  ('comparison -> exp comparison_a','comparison',2,'p_comparison','yacc.py',477),
  ('comparison_a -> comparison_b exp comparison_a','comparison_a',3,'p_comparison_a','yacc.py',481),
  ('comparison_a -> empty','comparison_a',1,'p_comparison_a','yacc.py',482),
  ('comparison_b -> GEQ','comparison_b',1,'p_comparison_b','yacc.py',486),
  ('comparison_b -> LEQ','comparison_b',1,'p_comparison_b','yacc.py',487),
  ('comparison_b -> GT','comparison_b',1,'p_comparison_b','yacc.py',488),
  ('comparison_b -> LT','comparison_b',1,'p_comparison_b','yacc.py',489),
  ('comparison_b -> EQUAL','comparison_b',1,'p_comparison_b','yacc.py',490),
  ('comparison_b -> NEQ','comparison_b',1,'p_comparison_b','yacc.py',491),
  ('exp -> term exp_a','exp',2,'p_exp','yacc.py',495),
  ('exp_a -> PLUS term exp_a','exp_a',3,'p_exp_a','yacc.py',499),
  ('exp_a -> MINUS term exp_a','exp_a',3,'p_exp_a','yacc.py',500),
  ('exp_a -> empty','exp_a',1,'p_exp_a','yacc.py',501),
  ('term -> factor term_a','term',2,'p_term','yacc.py',505),
  ('term_a -> MUL factor term_a','term_a',3,'p_term_a','yacc.py',508),
  ('term_a -> DIV factor term_a','term_a',3,'p_term_a','yacc.py',509),
  ('term_a -> empty','term_a',1,'p_term_a','yacc.py',510),
  ('factor -> LP expression RP','factor',3,'p_factor','yacc.py',515),
  ('factor -> factor_a var_cte','factor',2,'p_factor','yacc.py',516),
  ('factor_a -> MINUS','factor_a',1,'p_factor_a','yacc.py',520),
  ('factor_a -> NOT','factor_a',1,'p_factor_a','yacc.py',521),
  ('factor_a -> empty','factor_a',1,'p_factor_a','yacc.py',522),
  ('var_cte -> obj call_func_optional','var_cte',2,'p_var_cte','yacc.py',526),
  ('var_cte -> CTE_I','var_cte',1,'p_var_cte','yacc.py',527),
  ('var_cte -> CTE_F','var_cte',1,'p_var_cte','yacc.py',528),
  ('var_cte -> CTE_B','var_cte',1,'p_var_cte','yacc.py',529),
  ('array -> LC expression RC array_a','array',4,'p_array','yacc.py',533),
  ('array -> empty','array',1,'p_array','yacc.py',534),
  ('array_a -> LC expression RC','array_a',3,'p_array_a','yacc.py',538),
  ('array_a -> empty','array_a',1,'p_array_a','yacc.py',539),
  ('attribute -> DOT ID','attribute',2,'p_attribute','yacc.py',544),
  ('attribute -> empty','attribute',1,'p_attribute','yacc.py',545),
  ('call_func -> LP call_params RP','call_func',3,'p_call_func','yacc.py',549),
  ('call_func_optional -> call_func','call_func_optional',1,'p_call_func_optional','yacc.py',553),
  ('call_func_optional -> empty','call_func_optional',1,'p_call_func_optional','yacc.py',554),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',561),
]
