import yapl_mnm_tokens
import ply.lex as lex
import ply.yacc as yacc

start = 'yapl_mnm'

precedence = (
    ('left', 'OROR'),
    ('left', 'ANDAND'),
    ('left', 'EQUALEQUAL'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'UMINUS'),  # Unary minus operator
    ('right', 'NOT'),
)

tokens = (
    # BASIC LANG STUFF
    'ANDAND',  # &&
    'COMMA',  # ,
    'DIVIDE',  # /
    'EQUAL',  # =
    'EQUALEQUAL',  # ==
    'GE',  # >=
    'GT',  # >
    'IDENTIFIER',  #
    'LBRACE',  # {
    'LE',  # <=

    'LT',  # <
    'MINUS',  # -
    'NOT',  # !
    'NUMBER',  #
    'OROR',  # ||
    'PLUS',  # +
    'RBRACE',  # }

    'SEMICOLON',  # ;
    'STRING',  #### Not used in this problem.
    'TIMES',  # *
    'MOD',  # %
    'PLUSPLUS', # ++
    'MINUSMINUS', # --
    'LSQUAREPAREN', # [
    'RSQUAREPAREN', # ]
    'LPAREN',  # (
    'RPAREN',  # )

)

reserved = {

    'suppose': 'SUPPOSE',
    'maybe': 'MAYBE',
    'or': 'OR',
    'til': 'TIL',
    'until': 'UNTIL',
    'work': 'WORK',
    'machine': 'MACHINE',
    'fire': 'FIRE',
    'complex': 'COMPLEX',
    'snake': 'SNAKE',
    'True': 'TRUE',
    'False': 'FALSE',
    'access': 'ACCESS',
    'exps': 'EXPS',
    'g1' : 'G1',
    'perform': 'PERFORM',
    'end': 'END',
    'disp': 'DISP',
    'pop': 'POP',
    'push': 'PUSH',
    'slice': 'SLICE',
    'leave':'LEAVE',
    'displ': 'DISPL',

}

tokens = list(tokens) + list(reserved.values())

def p_yapl_mnm(p):
    '''
    yapl_mnm : main_statement
    '''
    # print (interpret(p[1]))
    p[0] = p[1]

def p_stmt_break(p):
    '''stmt : LEAVE '''
    p[0] = p[1]


def p_main_statement(p):
    'main_statement :  statements '
    p[0] = p[1]

def p_til_loop(p):
    'til : TIL LPAREN assign_identifier rel_exp exp RPAREN compoundstmt'
    # while interpret(p[4]):
    p[0] = ('til', p[3], p[4], p[5], p[7])

def p_work_until_loop(p):
    'until : WORK compoundstmt UNTIL LPAREN rel_exp RPAREN'
    p[0] = ('work', p[2], p[5])

def p_stmt(p):
    '''
    stmt :     exp
             | til
             | until
             | assign_identifier
             | snake_list
             | snake_list_access
             | rel_exp
             | disp_var
             | disp_string
             | disp_list
             | empty
    '''
    p[0] = p[1]

def p_intialize_snake(p):
    '''
    snake_list : SNAKE IDENTIFIER EQUAL num_snake
               | SNAKE IDENTIFIER EQUAL string_snake
               | SNAKE IDENTIFIER EQUAL bool_snake
    '''
    p[0] = ('snake', p[2], p[4])


def p_assign_snake(p):
    pass


def p_access_snake(p):
    '''
    snake_list_access : ACCESS IDENTIFIER NUMBER
    '''
    p[0] = ('access', p[2], p[3])

def p_num_snake(p):
    '''
    num_snake : num_snake COMMA exp
              | exp
              | empty
    '''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

# int string bool
def p_string_snake(p):
    '''
    string_snake : string_snake COMMA STRING
                 | STRING
                 | empty
    '''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

def p_bool_snake(p):
    '''
    bool_snake : bool_snake COMMA bool
               | bool
    '''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

def p_empty(p):
    'empty :'
    p[0] = None

def p_initialize_identifier(p):
    '''
    assign_identifier : SUPPOSE IDENTIFIER EQUAL exp
    '''
    p[0] = ('suppose', p[2], p[4])

def p_assign_identifier(p):
    '''
    assign_identifier : IDENTIFIER EQUAL exp
    '''
    p[0] = ('=', p[1], p[3])

def p_disp_var(p):
    '''
    disp_var : DISP IDENTIFIER
    '''
    p[0] = ('disp_var', p[2])

def p_disp_string(p):
    '''
    disp_string : DISP STRING
    '''
    p[0] = ('disp_string', p[2])

def p_disp_list(p):
    '''
    disp_list : DISPL IDENTIFIER
    '''
    p[0] = ('disp_list', p[2])

def p_exp(p):
    '''
    exp : exp TIMES exp
        | exp DIVIDE exp
        | exp PLUS exp
        | exp MINUS exp
        | exp MOD exp
    '''
    p[0] = (p[2], p[1], p[3])

def p_exp_increment_decrement(p):
    '''
    exp : exp PLUSPLUS
        | exp MINUSMINUS
    '''
    p[0] = (p[2], p[1])

def p_exp_uminus(p):
    'exp : MINUS exp %prec UMINUS'
    p[0] = -p[2]


def p_exp_number(p):
    '''
    exp : NUMBER
    '''
    p[0] = p[1]


def p_exp_string(p):
    '''
    exp : STRING
    '''
    p[0] = p[1]


def p_exp_bool(p):
    '''
    exp : bool
    bool : TRUE
         | FALSE
    '''
    p[0] = p[1]

def p_exp_identifier(p):
    '''
    exp : IDENTIFIER
    '''
    p[0] = ('identifier', p[1])

def p_rel_exp(p):
    '''

    rel_exp : exp GE exp
            | exp GT exp
            | exp LE exp
            | exp LT exp
            | exp EQUALEQUAL exp

    '''

    p[0] = (p[2],p[1],p[3])

def p_rel_exp_not_equal(p):
    '''
    rel_exp : exp NOT EQUAL exp
    '''
    p[0] = (p[2],p[3],p[1],p[4])

def p_stmt_if_then(p):
    'stmt : MAYBE rel_exp compoundstmt'
    p[0] = ('if-then', p[2], p[3])
def p_stmt_if_then_else(p):
    'stmt : MAYBE rel_exp compoundstmt OR compoundstmt'
    p[0] = ('if-then-else', p[2], p[3], p[5])

def p_compoundstmt(p):
    'compoundstmt : LBRACE statements RBRACE'
    p[0] = p[2]

def p_statements(p):
    'statements : stmt SEMICOLON statements'
    if p[3] is not None:
        p[0] = [ p[1] ] + p[3]
    else:
        p[0] = [p[1]]

def p_statements_empty(p):
    'statements : empty'
    p[0] = p[1]

def p_yapl_if_then(p):
    'main_statement : MAYBE rel_exp compoundstmt'
    p[0] = ('if-then', p[2], p[3])

def p_yapl_if_then_else(p):
    'main_statement : MAYBE rel_exp compoundstmt OR compoundstmt'
    p[0] = ('if-then-else', p[2], p[3], p[5])

def p_yapl_pop_list(p):
    'main_statement : POP IDENTIFIER NUMBER'
    p[0] = ('pop', p[2], p[3])

def p_stmt_pop_list(p):
    'stmt : POP IDENTIFIER NUMBER'
    p[0] = ('pop', p[2], p[3])

def p_yapl_push_list(p):
    'main_statement : IDENTIFIER PUSH NUMBER'
    p[0] = (p[2], p[1], p[3])

def p_stmt_push_list(p):
    'stmt : IDENTIFIER PUSH NUMBER'
    p[0] = (p[2], p[1], p[3])

def p_yapl_slice_list(p):
    'main_statement : IDENTIFIER SLICE NUMBER NUMBER'
    p[0] = (p[2], p[1], p[3],p[4])

def p_stmt_slice_list(p):
    'stmt : IDENTIFIER SLICE NUMBER NUMBER'
    p[0] = (p[2], p[1], p[3],p[4])

def p_stmt_slice_list_eq(p):
    'stmt : IDENTIFIER EQUAL IDENTIFIER SLICE NUMBER NUMBER'
    p[0] = ('slice_copy', p[1],p[3],p[5],p[6])

def p_func_definition(p):
    'stmt : MACHINE IDENTIFIER LPAREN optparams RPAREN compoundstmt'
    p[0] = ('machine', p[2], p[4], p[6])

def p_optparams(p):
    'optparams : params'
    p[0] = p[1]

def p_optparams_empty(p):
    'optparams : empty'
    p[0] = []

def p_params(p):
    'params : IDENTIFIER COMMA params'
    p[0] = [ p[1] ] + p[3]

def p_params_last(p):
    'params : IDENTIFIER'
    p[0] = [ p[1] ]

def p_error(p):

    print('Syntax Error found in input!')

def env_lookup(vname, env):
    # (parent, dictionary)
    if vname in env[1]:
        return env[1][vname]
    elif env[0] == None:
        return None
    else:
        return env_lookup(vname,env[0])

def env_update(vname,value,env):
    if vname in env[1]:
        env[1][vname] = value
    elif not env[0] == None:
        env_update(vname,value,env[0])


def interpret(p, env_tuple):
    #print(p)

    if type(p) == list:
        result = []
        for stm in p:
            _result = interpret(stm,env_tuple)
            if _result == 'leave':
                return 'leave'
            result.append(_result)
        return result

    if type(p) == tuple:
        if p[0] == '+':
            return interpret(p[1],env_tuple) + interpret(p[2],env_tuple)
        elif p[0] == '-':
            return interpret(p[1],env_tuple) - interpret(p[2],env_tuple)
        elif p[0] == '*':
            return interpret(p[1],env_tuple) * interpret(p[2],env_tuple)
        elif p[0] == '/':
            return interpret(p[1],env_tuple) / interpret(p[2],env_tuple)
        elif p[0] == '%':
            return interpret(p[1], env_tuple) % interpret(p[2],env_tuple)
        elif p[0] == '++' and p[1] and p[1][0] == 'identifier':
            if p[1][1] not in env:
                print('Undefined variable {0}'.format(p[1][1]))
                #get value from lookup, +1 it and then
                exit()
            value = env[p[1][1]]
            env[p[1][1]] += 1
            return value
        elif p[0] == '--' and p[1] and p[1][0] == 'identifier':
            if p[1][1] not in env:
                print('Undefined variable {0}'.format(p[1][1]))
                exit()
            value = env[p[1][1]]
            env[p[1][1]] -= 1
            return value
        elif p[0] == '>=':
            return interpret(p[1],env_tuple) >= interpret(p[2],env_tuple)
        elif p[0] == '>':
            return interpret(p[1],env_tuple) > interpret(p[2],env_tuple)
        elif p[0] == '<=':
            return interpret(p[1],env_tuple) <= interpret(p[2],env_tuple)
        elif p[0] == '<':
            return interpret(p[1],env_tuple) < interpret(p[2],env_tuple)
        elif p[0] == '==':
            return interpret(p[1],env_tuple) == interpret(p[2],env_tuple)
        elif p[0] == '!' and p[1] == '=':
            return interpret(p[1],env_tuple) != interpret(p[2],env_tuple)
        elif p[0] == '(' and p[1] == ')':
            return interpret(p[2],env_tuple)
        elif p[0] == 'disp_var':
            if p[1] not in env:
                print('undeclared variable!')
                exit()
            print(env[p[1]])
        elif p[0] == 'disp_string':
            print(p[1])
        elif p[0] == 'disp_list':
            if p[1] not in env:
                print('undeclared variable!')
                exit()
            for item in env[p[1]]:
                print(item)
        elif p[0] == 'if-then':
            if interpret(p[1],env_tuple) == True:
                return interpret(p[2],env_tuple)
        elif p[0] == 'if-then-else':
            if interpret(p[1],env_tuple) == True:
                return interpret(p[2],env_tuple)
            else:
                return interpret(p[3],env_tuple)
        elif p[0] == 'pop':
            if p[1] not in env:
                return 'undeclared variable!'
            if interpret(p[2],env_tuple) == 0:
                return env[p[1]].pop(0)
            elif interpret(p[2],env_tuple) == 1:
                return env[p[1]].pop(-1)
        elif p[0] == 'push':
            if p[1] not in env:
                return 'undeclared variable!'
            number_to_push = interpret(p[2],env_tuple)
            env[p[1]].append(number_to_push)
        elif p[0] == 'slice':
            if p[1] not in env:
                return 'undeclared variable!'
            start = interpret(p[2],env_tuple)
            end = interpret(p[3],env_tuple)
            return env[p[1]][int(start):int(end)]
        elif p[0] == 'slice_copy':
            if p[1] not in env:
                return 'undeclared variable!'
            if p[1] in env:
                start = interpret(p[3],env_tuple)
                end = interpret(p[4],env_tuple)
                env[p[1]] = env[p[2]][int(start):int(end)+1]

        elif p[0] == 'leave':
            return p[0]
        elif p[0] == 'til':
            interpret(p[1],env_tuple)
            _results = []
            while(interpret(p[2],env_tuple)):
                _result = interpret(p[4],env_tuple)
                if _result == "leave":
                    break
                _results.append(_result)
                interpret(p[3],env_tuple)
            return _results
        elif p[0] == 'work':
            _results = []
            _results.append(interpret(p[1],env_tuple))
            while (interpret(p[2],env_tuple)):
                _result = interpret(p[1],env_tuple)
                if _result == "leave":
                    break
                _results.append(_result)
            return _results
        elif p[0] == 'suppose':
            if p[1] in env:
                print('duplicate identifier detected')
                exit()
                return ''
            env[p[1]] = interpret(p[2],env_tuple)
            return ''
        elif p[0] == 'snake':
            if p[1] in env:
                print('duplicate identifier detected')
                exit()
                #return ''
            result = []
            for item in p[2]:
                part = interpret(item,env_tuple)
                result.append(part)
            env[p[1]] = result
            #return ''
        elif p[0] == 'access':
            if p[1] in env:
                 index = interpret(p[2],env_tuple)
                 if index > len(env[p[1]]):
                     print("list index out of range")
                     exit()
                     return ''
                 print(env[p[1]][int(index)])
                 return env[p[1]][int(index)]
        elif p[0] == '=':
            if p[1] in env:
                env[p[1]] = interpret(p[2],env_tuple)
            else:
                print('cannot assign undeclared variable')
                exit()
            return ''
        elif p[0] == 'identifier':
            if p[1] not in env:
                return 'undeclared variable!'
            else:
                return env[p[1]]
    else:
        return p


yapl_mnm_lexer = lex.lex(module=yapl_mnm_tokens)
yapl_mnm_parser = yacc.yacc()



env_tuple = (None, {})



# test = open("test.txt", "r")
# test_list_methods = open("test_list_methods.txt", "r")
# test_list = open("test_list", "r")
# test_var_dec =open("test_var_dec.txt", "r")
# test_do_while = open("test_do_while.txt", "r")
# test_if_for = open("test_if_for.txt", "r")
# test_func= open("test_func_test.txt", "r")
# test_recur = open("test_recur.txt", "r")
# test_struct = open("test_struct.txt", "r")

# input_string = test.read()
# input_string = test_list_methods.read()
# input_string = test_list.read()
# input_string = test_var_dec.read()
# input_string = test_do_while.read()
# input_string = test_if_for.read()
# input_string = test_func.read()
# input_string = test_recur.read()
# input_string = test_struct.read()

#input_string = input('>> ')

yapl_mnm_ast = yapl_mnm_parser.parse(input_string, lexer=yapl_mnm_lexer)
interpret(yapl_mnm_ast,env_tuple)
#print(yapl_mnm_ast)



# while True:
#
#     # Testing
#
#     try:
#         # input_string = input('>> ')
#           input_string = test_var_dec
#     except EOFError:
#         break
#     if not input_string:
#         continue
#     yapl_mnm_ast = yapl_mnm_parser.parse(input_string, lexer=yapl_mnm_lexer)
#     interpret(yapl_mnm_ast, env)
    #print(yapl_mnm_ast)





# while True:
#     try:
#         input_string = input('<< ')
#     except EOFError:
#         break
#     yapl_mnm_ast = yapl_mnm_parser.parse(input_string,lexer=yapl_mnm_lexer)
#     print(yapl_mnm_ast)

#if else statements
#make relation expressions
#look at BASIC example for if and for

