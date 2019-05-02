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
    'PLUSPLUS',  # ++
    'MINUSMINUS',  # --
    'LSQUAREPAREN',  # [
    'RSQUAREPAREN',  # ]
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
    'g1': 'G1',
    'perform': 'PERFORM',
    'end': 'END',
    'disp': 'DISP',
    'pop': 'POP',
    'push': 'PUSH',
    'slice': 'SLICE',
    'leave': 'LEAVE',
    'displ': 'DISPL',
    'new': 'NEW',

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
    p[0] = ('til', p[3], p[4], p[5], p[7],p.lineno(1))


def p_work_until_loop(p):
    'until : WORK compoundstmt UNTIL LPAREN rel_exp RPAREN'
    p[0] = ('work', p[2], p[5], p.lineno(1))


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
    p[0] = ('snake', p[2], p[4],p.lineno(1))


#
# def p_assign_snake(p):
#     pass


def p_access_snake(p):
    '''
    snake_list_access : ACCESS IDENTIFIER NUMBER
    '''
    p[0] = ('access', p[2], p[3],p.lineno(1))


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
    assign_identifier : SUPPOSE IDENTIFIER EQUAL stmt
    '''
    p[0] = ('suppose', p[2], p[4], p.lineno(1))


def p_assign_identifier(p):
    '''
    assign_identifier : IDENTIFIER EQUAL stmt
    '''
    p[0] = ('=', p[1], p[3],p.lineno(1))


def p_disp_var(p):
    '''
    disp_var : DISP IDENTIFIER
    '''
    p[0] = ('disp_var', p[2],p.lineno(1))


def p_disp_string(p):
    '''
    disp_string : DISP STRING
    '''
    p[0] = ('disp_string', p[2],p.lineno(1))


def p_disp_list(p):
    '''
    disp_list : DISPL IDENTIFIER
    '''
    p[0] = ('disp_list', p[2],p.lineno(1))


def p_exp(p):
    '''
    exp : exp TIMES exp
        | exp DIVIDE exp
        | exp PLUS exp
        | exp MINUS exp
        | exp MOD exp
    '''
    p[0] = (p[2], p[1], p[3], p.lineno(1))


def p_exp_increment_decrement(p):
    '''
    exp : exp PLUSPLUS
        | exp MINUSMINUS
    '''
    p[0] = (p[2], p[1], p.lineno(1))


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
    p[0] = ('identifier', p[1],p.lineno(1))


def p_rel_exp(p):
    '''

    rel_exp : exp GE exp
            | exp GT exp
            | exp LE exp
            | exp LT exp
            | exp EQUALEQUAL exp

    '''

    p[0] = (p[2], p[1], p[3], p.lineno(1))


def p_rel_exp_not_equal(p):
    '''
    rel_exp : exp NOT EQUAL exp
    '''
    p[0] = (p[2], p[3], p[1], p[4], p.lineno(1))


def p_stmt_if_then(p):
    'stmt : MAYBE rel_exp compoundstmt'
    p[0] = ('if-then', p[2], p[3], p.lineno(1))


def p_stmt_if_then_else(p):
    'stmt : MAYBE rel_exp compoundstmt OR compoundstmt'
    p[0] = ('if-then-else', p[2], p[3], p[5], p.lineno(1))


def p_compoundstmt(p):
    'compoundstmt : LBRACE statements RBRACE'
    p[0] = p[2]


def p_statements(p):
    'statements : stmt SEMICOLON statements'
    if p[3] is not None:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]


def p_statements_empty(p):
    'statements : empty'
    p[0] = p[1]


def p_yapl_if_then(p):
    'main_statement : MAYBE rel_exp compoundstmt'
    p[0] = ('if-then', p[2], p[3], p.lineno(1))


def p_yapl_if_then_else(p):
    'main_statement : MAYBE rel_exp compoundstmt OR compoundstmt'
    p[0] = ('if-then-else', p[2], p[3], p[5], p.lineno(1))


def p_yapl_pop_list(p):
    'main_statement : POP IDENTIFIER NUMBER'
    p[0] = ('pop', p[2], p[3],p.lineno(1))


def p_stmt_pop_list(p):
    'stmt : POP IDENTIFIER NUMBER'
    p[0] = ('pop', p[2], p[3], p.lineno(1))


def p_yapl_push_list(p):
    'main_statement : IDENTIFIER PUSH NUMBER'
    p[0] = (p[2], p[1], p[3], p.lineno(1))


def p_stmt_push_list(p):
    'stmt : IDENTIFIER PUSH NUMBER'
    p[0] = (p[2], p[1], p[3], p.lineno(1))


def p_yapl_slice_list(p):
    'main_statement : IDENTIFIER SLICE NUMBER NUMBER'
    p[0] = (p[2], p[1], p[3], p[4],p.lineno(1))


def p_stmt_slice_list(p):
    'stmt : IDENTIFIER SLICE NUMBER NUMBER'
    p[0] = (p[2], p[1], p[3], p[4], p.lineno(1))


def p_stmt_slice_list_eq(p):
    'stmt : IDENTIFIER EQUAL IDENTIFIER SLICE NUMBER NUMBER'
    p[0] = ('slice_copy', p[1], p[3], p[5], p[6], p.lineno(1))


def p_func_definition(p):
    'stmt : MACHINE IDENTIFIER LPAREN optparams RPAREN compoundstmt'
    p[0] = ('machine', p[2], p[4], p[6], p.lineno(1))


def p_optparams(p):
    'optparams : params'
    p[0] = p[1]


def p_optparams_empty(p):
    'optparams : empty'
    p[0] = []


def p_params(p):
    'params : stmt COMMA params'
    p[0] = [p[1]] + p[3]


def p_params_last(p):
    'params : stmt'
    p[0] = [p[1]]


def p_func_call(p):
    "stmt : IDENTIFIER LPAREN optparams RPAREN"
    p[0] = ('machine_run', p[1], p[3], p.lineno(1))


# def p_func_call_assign(p):
#     'stmt : SUPPOSE IDENTIFIER EQUAL IDENTIFIER LPAREN optparams RPAREN'
#     p[0] = ('suppose_machine_run', p[2], p[4],p[6])

def p_return(p):
    'stmt : FIRE stmt'
    p[0] = ('fire', p[2], p.lineno(1))


def p_struct_define(p):
    'stmt : COMPLEX IDENTIFIER LBRACE attributes RBRACE'
    p[0] = ('complex', p[2], p[4], p.lineno(1))


def p_attributes(p):
    'attributes : IDENTIFIER SEMICOLON attributes'
    if p[3] == None:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_attribute_last(p):
    'attributes : IDENTIFIER SEMICOLON'
    p[0] = [p[1]]


def p_attributes_empty(p):
    'attributes : empty'
    p[0] = p[1]


def p_struct_make(p):
    'stmt : NEW IDENTIFIER IDENTIFIER'
    p[0] = ('new', p[2], p[3], p.lineno(1))


def p_struct_obj_set_attr(p):
    'stmt : IDENTIFIER ACCESS IDENTIFIER EQUAL exp'
    p[0] = ('struct_set_attr', p[1], p[3], p[5], p.lineno(1))


def p_disp_attr(p):
    'stmt : DISP IDENTIFIER ACCESS IDENTIFIER'
    p[0] = ('disp_attr', p[2], p[4],p.lineno(1))


def p_struct_obj_get_attr(p):
    'stmt : IDENTIFIER ACCESS IDENTIFIER'
    p[0] = ('struct_obj_get_attr', p[1], p[3], p.lineno(1))


def p_error(p):
    if p != None:
        print("Syntax Error found in input on line " + str(p.lineno))


def env_lookup(vname, env):
    # (parent, dictionary)
    if vname in env[1]:
        return env[1][vname]
    elif env[0] == None:
        return None
    else:
        return env_lookup(vname, env[0])


def env_update(vname, value, env):
    if vname in env[1]:
        env[1][vname] = value
    elif not env[0] == None:
        env_update(vname, value, env[0])


def add_to_env(vname, value, env):
    if vname in env[1]:
        print("duplicate variable!")
        exit()
    env[1][vname] = value


def interpret(p, env_tuple):
    # print(p)

    if type(p) == list:
        result = []
        for stm in p:
            _result = interpret(stm, env_tuple)
            if stm == 'leave':
                return _result
            result.append(_result)
        return result

    if type(p) == tuple:
        if p[0] == '+':
            return interpret(p[1], env_tuple) + interpret(p[2], env_tuple)
        elif p[0] == '-':
            return interpret(p[1], env_tuple) - interpret(p[2], env_tuple)
        elif p[0] == '*':
            return interpret(p[1], env_tuple) * interpret(p[2], env_tuple)
        elif p[0] == '/':
            return interpret(p[1], env_tuple) / interpret(p[2], env_tuple)
        elif p[0] == '%':
            return interpret(p[1], env_tuple) % interpret(p[2], env_tuple)
        elif p[0] == '++' and p[1] and p[1][0] == 'identifier':
            stored_value = env_lookup(p[1][1], env_tuple)
            if stored_value == None:
                print('Undefined variable at {0}'.format(p[1][1])  )
                # get value from lookup, +1 it and then update it
                exit()
            incremented_value = stored_value + 1
            env_update(p[1][1], incremented_value, env_tuple)
            return stored_value
        elif p[0] == '--' and p[1] and p[1][0] == 'identifier':
            stored_value = env_lookup(p[1][1], env_tuple)
            if stored_value == None:
                print('Undefined variable {0}'.format(p[1][1]))
                # get value from lookup, +1 it and then update it
                exit()
            decremented_value = stored_value - 1
            env_update(p[1][1], decremented_value, env_tuple)
            return stored_value
        elif p[0] == '>=':
            return interpret(p[1], env_tuple) >= interpret(p[2], env_tuple)
        elif p[0] == '>':
            return interpret(p[1], env_tuple) > interpret(p[2], env_tuple)
        elif p[0] == '<=':
            return interpret(p[1], env_tuple) <= interpret(p[2], env_tuple)
        elif p[0] == '<':
            return interpret(p[1], env_tuple) < interpret(p[2], env_tuple)
        elif p[0] == '==':
            return interpret(p[1], env_tuple) == interpret(p[2], env_tuple)
        elif p[0] == '!' and p[1] == '=':
            return interpret(p[1], env_tuple) != interpret(p[2], env_tuple)
        elif p[0] == '(' and p[1] == ')':
            return interpret(p[2], env_tuple)
        elif p[0] == 'disp_var':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value == None:
                print('undeclared variable!')
                exit()
            print(stored_value)
        elif p[0] == 'disp_string':
            print(p[1])
        elif p[0] == 'disp_list':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value == None:
                print('undeclared variable!')
                exit()
            for item in stored_value:
                print(item)
        elif p[0] == 'if-then':
            if interpret(p[1], env_tuple) == True:
                return interpret(p[2], env_tuple)
        elif p[0] == 'if-then-else':
            if interpret(p[1], env_tuple) == True:
                return interpret(p[2], env_tuple)
            else:
                return interpret(p[3], env_tuple)
        elif p[0] == 'pop':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value == None:
                return 'undeclared variable!'
            if interpret(p[2], env_tuple) == 0:
                poped_value = stored_value.pop(0)
                env_update(p[1], poped_value, env_tuple)
                return poped_value
            elif interpret(p[2], env_tuple) == 1:
                poped_value = stored_value.pop(-1)
                env_update(p[1], poped_value, env_tuple)
                return poped_value
        elif p[0] == 'push':
            stored_value = env_lookup(p[1])
            if stored_value == None:
                return 'undeclared variable!'
            number_to_push = interpret(p[2], env_tuple)
            pushed_value = stored_value.append(number_to_push)
            env_update(p[1], pushed_value, env_tuple)
        elif p[0] == 'slice':
            stored_value = env_lookup(p[1])
            if stored_value == None:
                return 'undeclared variable!'
            start = interpret(p[2], env_tuple)
            end = interpret(p[3], env_tuple)
            sliced_value = stored_value[int(start):int(end)]
            env_update(p[1], sliced_value, env_tuple)
            return sliced_value
        elif p[0] == 'slice_copy':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value == None:
                return 'undeclared variable!'
            start = interpret(p[3], env_tuple)
            end = interpret(p[4], env_tuple)
            stored_value_2 = env_lookup(p[2], env_tuple)
            value_spliced_from_2 = stored_value_2[int(start):int(end) + 1]
            env_update(p[1], value_spliced_from_2, env_tuple)

        elif p[0] == 'leave':
            return p[0]
        elif p[0] == 'til':
            interpret(p[1], env_tuple)
            _results = []
            while (interpret(p[2], env_tuple)):
                _result = interpret(p[4], env_tuple)
                if _result == "leave":
                    break
                _results.append(_result)
                interpret(p[3], env_tuple)
            return _results
        elif p[0] == 'machine':

            if p[2] is None:
                return add_to_env(p[1], {
                    "statements": p[3],
                    "parameters": []
                }, env_tuple)
            else:
                return add_to_env(p[1], {
                    "statements": p[3],
                    "parameters": p[2]
                }, env_tuple)

        elif p[0] == 'machine_run':
            func_name = p[1]
            _function = env_lookup(func_name, env_tuple)
            if not _function:
                print('Undefined function call')
                exit()

            parameters = p[2]
            function_env = {}

            index = 0
            for param in _function["parameters"]:
                if param is not None:
                    function_env[param[1]] = parameters[index]
                index += 1

            return_value = None
            for statement in _function["statements"]:
                return_value = interpret(statement, (env_tuple, function_env))
                if statement[0] and statement[0] == 'fire':
                    return return_value
            return return_value

        elif p[0] == 'complex':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value != None:
                print('duplicate structure detected')
                exit()

            struct_dict = {"attributes": p[2]}
            add_to_env(p[1], struct_dict, env_tuple)

        elif p[0] == 'new':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value == None:
                print('undeclared structure!')
                exit()
            stored_value_2 = env_lookup(p[2], env_tuple)
            if stored_value_2 != None:
                print('duplicate structure object of type ' + str(p[1]))
                exit()

            struct_attrs = stored_value["attributes"]
            obj_dict = {}
            for attribute in struct_attrs:
                obj_dict[attribute] = None

            add_to_env(p[2], obj_dict, env_tuple)

        elif p[0] == 'struct_set_attr':
            struct_attr_dict = env_lookup(p[1], env_tuple)
            if struct_attr_dict == None:
                print('undeclared structure object!')
                exit()

            if p[2] not in struct_attr_dict:
                print('no such variable declared in structure definition')
                exit()

            value_to_set = interpret(p[3], env_tuple)
            struct_attr_dict[p[2]] = value_to_set

            env_update(p[1], struct_attr_dict, env_tuple)

        elif p[0] == 'struct_obj_get_attr':
            struct_attr_dict = env_lookup(p[1], env_tuple)
            if struct_attr_dict == None:
                print('undeclared structure object!')
                exit()

            if p[2] not in struct_attr_dict:
                print('no such variable declared in structure definition')
                exit()
            value_to_get = struct_attr_dict[p[2]]

            return value_to_get

        elif p[0] == 'disp_attr':
            struct_attr_dict = env_lookup(p[1], env_tuple)
            if struct_attr_dict == None:
                print('undeclared structure object!')
                exit()

            if p[2] not in struct_attr_dict:
                print('no such variable declared in structure definition')
                exit()
            value_to_get = struct_attr_dict[p[2]]

            print(value_to_get)



        elif p[0] == 'fire':
            return interpret(p[1], env_tuple)



        elif p[0] == 'work':
            _results = []
            _results.append(interpret(p[1], env_tuple))
            while (interpret(p[2], env_tuple)):
                _result = interpret(p[1], env_tuple)
                if _result == "leave":
                    break
                _results.append(_result)
            return _results
        elif p[0] == 'suppose':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value != None:
                print('duplicate identifier detected on line ' + str(p[3]))
                exit()
            value_to_store = interpret(p[2], env_tuple)
            add_to_env(p[1], value_to_store, env_tuple)
            return ''
        elif p[0] == 'snake':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value != None:
                print('duplicate identifier detected')
                exit()
            result = []
            for item in p[2]:
                part = interpret(item, env_tuple)
                result.append(part)
            add_to_env(p[1], result, env_tuple)
            # return ''
        elif p[0] == 'access':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value != None:
                index = interpret(p[2], env_tuple)
                if index > len(stored_value):
                    print("list index out of range")
                    exit()
                    return ''
                print(stored_value[int(index)])
                return stored_value[int(index)]
        elif p[0] == '=':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value != None:
                value_to_store = interpret(p[2], env_tuple)
                env_update(p[1], value_to_store, env_tuple)
            else:
                print('cannot assign undeclared variable')
                exit()
        elif p[0] == 'identifier':
            stored_value = env_lookup(p[1], env_tuple)
            if stored_value == None:
                return 'undeclared variable!'
            else:
                return stored_value
    else:
        return p


yapl_mnm_lexer = lex.lex(module=yapl_mnm_tokens)
yapl_mnm_parser = yacc.yacc()

env_tuple = (None, {})

# test = open("test.txt", "r")
# test_list_methods = open("test_list_methods.txt", "r")
# test_list = open("test_list.txt", "r")
# test_var_dec =open("test_var_dec.txt", "r")
# test_do_while = open("test_do_while.txt", "r")
# test_if_for = open("test_if_for.txt", "r")
# test_func= open("test_func.txt", "r")
test_recur = open("test_recur.txt", "r")
# test_struct = open("test_struct.txt", "r")

# input_string = test.read()
# input_string = test_list_methods.read()
# input_string = test_list.read()
# input_string = test_var_dec.read()
# input_string = test_do_while.read()
# input_string = test_if_for.read()
# input_string = test_func.read()
input_string = test_recur.read()
# input_string = test_struct.read()

# input_string = input('>> ')

yapl_mnm_ast = yapl_mnm_parser.parse(input_string, lexer=yapl_mnm_lexer)
interpret(yapl_mnm_ast, env_tuple)
# print(yapl_mnm_ast)


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
# print(yapl_mnm_ast)


# while True:
#     try:
#         input_string = input('<< ')
#     except EOFError:
#         break
#     yapl_mnm_ast = yapl_mnm_parser.parse(input_string,lexer=yapl_mnm_lexer)
#     print(yapl_mnm_ast)

# if else statements
# make relation expressions
# look at BASIC example for if and for
