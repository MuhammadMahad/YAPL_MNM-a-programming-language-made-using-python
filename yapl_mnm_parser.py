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

}

tokens = list(tokens) + list(reserved.values())



# def p_yapl_mnm(p):
#     'yapl_mnm : element yapl_mnm'
#     p[0] = [p[1]] + p[2]
#
# def p_yapl_mnm_empty(p):
#     'yapl_mnm : '
#     p[0] = [ ]
#
# def p_element_statement(p):
#     'element : stmt SEMICOLON'
#     p[0] = ('stmt', p[1])
#
# def p_stmt(p):
#     '''
#     stmt     : exp
#              | assign_identifier
#              | snake_list
#              | snake_list_access
#              | rel_exp
#              | empty
#
#     '''
#     p[0] = p[1]
#     #print(interpret(p[1]))

# def p_yapl_mnm(p):
#     '''yapl_mnm : element yapl_mnm
#                 | empty
#
#     '''
#
#
#     print(interpret(p[1]))
#
# def p_element_statement(p):
#     'element : stmt SEMICOLON'
#     p[0] = ('stmt', p[1])
#
# def p_stmt(p):
#     '''
#     stmt     : exp
#              | assign_identifier
#              | snake_list
#              | snake_list_access
#              | rel_exp
#              | empty
#
#     '''
#     p[0] = p[1]
    #print(interpret(p[1]))


def p_yapl_mnm(p):
    '''
    yapl_mnm : exp
             | til
             | assign_identifier
             | snake_list
             | snake_list_access
             | rel_exp
             | disp_var
             | empty
    '''
    # print (interpret(p[1]))
    p[0] = p[1]

                            # def p_conditional(p):
                            #     '''conditional : '''

                            # def p_stmt(p):
                            #         '''
                            # stmt         : exp statements
                            #              | assign_identifier statements
                            #              | snake_list statements statements
                            #              | snake_list_access statements
                            #              | rel_exp statements
                            #              | conditional statements
                            #              | til statements
                            #              | empty statements
                            #     '''
                            #         p[0] = p[1]
                            # def p_statements(p):
                            #     '''statements : stmt
                            #                   | empty
                            #
                            #     '''
                            #     #p[0] = [p[1]] + p[3]
                            #     p[0] = p[1]
                            #
                            # def p_stmt_maybe_then(p):
                            #     'conditional : MAYBE rel_exp LBRACE statements RBRACE'
                            #     if interpret(p[2]):
                            #         p[0] = p[4]
                            #
                            # def p_stmt_maybe_then_or(p):
                            #     'conditional : MAYBE rel_exp LBRACE statements RBRACE OR LBRACE statements RBRACE'
                            #     if interpret(p[2]):
                            #         p[0] = p[4]
                            #     else:
                            #         p[0] = p[8]
                            #
def p_til_loop(p):
    'til : TIL LPAREN assign_identifier rel_exp exp RPAREN compoundstmt'
    # while interpret(p[4]):
    p[0] = ('til', p[3], p[4], p[5], p[7])



# def p_stmt_maybe_then(p):
#     'conditional : MAYBE rel_exp compoundstmt'
#     p[0] = ('maybe-then', p[2], p[3])


# def p_stmt_maybe_then_or(p):
#     'conditional : MAYBE rel_exp compoundstmt OR compoundstmt'
#     p[0] = ('maybe-then-or', p[2], p[3], p[5])

#
# def p_compoundstmt(p):
#     'compoundstmt : LBRACE statements RBRACE'
#     p[0] = p[2]
#
#
# def p_statements(p):
#     'statements : yapl_mnm SEMICOLON statements'
#     #p[0] = [p[1]] + p[3]
#     p[0] = (p[1], p[3])
#
# def p_statements_empty(p):
#     'statements : empty'
#     p[0] = p[1]



# def p_exp_rel_exp(p):
#     '''
#     exp : rel_exp
#     '''
#     p[0] = (p[1])


# def p_statement(p):
#         '''
#     statement : exp
#               | assign_identifier
#               | snake_list
#               | snake_list_access
#               | rel_exp
#               | conditional
#               | statement
#               | empty
#         '''
#         p[0] = (p[1])
#
# # def p_statements(p):
# #     '''
# #     statements : LBRACE statement statements RBRACE
# #                | empty
# #
# #     '''
# #     p[0] = (p[1], p[2])
#
# def p_nested_parentheses(p):
#     '''
#     exp : LPAREN exp RPAREN
#     '''
#     p[0] = (p[1], p[3], p[2])
#
# def p_maybe(p):
#     '''
#     maybe_statement : MAYBE rel_exp perform_statement or_statement END
#     '''
#     p[0] = (p[1], p[2], p[3])
#
# def p_perform(p):
#     '''
#     perform_statement : PERFORM maybe_statement
#                       | PERFORM statement
#     '''
#
# def p_or(p):
#     '''
#     or_statement : OR statement
#                  | OR maybe_statement
#                  | empty
#     '''
#     p[0] = (p[1], p[2], p[3], p[4], p[5])
#

# def p_maybe(p):
#     '''
#     conditional : MAYBE rel_exp statements
#
#     '''
#     p[0] = (p[1], p[2], p[3])
#
# def p_or_maybe(p):
#     '''
#     conditional : MAYBE rel_exp statements OR statements
#
#     '''
#     p[0] = (p[1], p[4], p[2], p[3], p[5])
#
# def p_statements(p):
#     '''
#     statements :  LBRACE exps RBRACE
#     '''
#     p[0] = (p[2])
#
# def p_exps(p):
#     '''
#     exps : EXPS exp exps
#          | EXPS assign_identifier exps
#          | EXPS snake_list exps
#          | EXPS snake_list_access exps
#          | EXPS rel_exp exps
#          | EXPS conditional exps
#          | EXPS empty exps
#          | EXPS empty
#     '''
#     p[0] = ('exps', p[1], p[2])

def p_stmt(p):
    '''
    stmt : exp
             | til
             | assign_identifier
             | snake_list
             | snake_list_access
             | rel_exp
             | disp_var
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


# def p_assign_identifier_error(p):
#     print('duplicate identifier detected')

def p_disp_var(p):
    '''
    disp_var : DISP IDENTIFIER
    '''
    p[0] = ('disp', p[2])

# def p_disp_list(p):
#     '''
#     disp_list : DISP IDENTIFIER
#     '''
#     p[0] = ('disp_list', p[2])


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

# def p_if_then(p):
#     'stmt : MAYBE rel_exp compoundstmt'
#     p[0] = ('if-then', p[2], p[3])

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
    'yapl_mnm : MAYBE rel_exp compoundstmt'
    p[0] = ('if-then', p[2], p[3])
def p_yapl_if_then_else(p):
    'yapl_mnm : MAYBE rel_exp compoundstmt OR compoundstmt'
    p[0] = ('if-then-else', p[2], p[3], p[5])

def p_error(p):

    print('Syntax Error found in input!')


def interpret(p, env):
    #print(p)

    if type(p) == list:
        result = []
        for stm in p:
            result.append(interpret(stm, env))
        return result

    if type(p) == tuple:
        if p[0] == '+':
            return interpret(p[1], env) + interpret(p[2], env)
        elif p[0] == '-':
            return interpret(p[1], env) - interpret(p[2], env)
        elif p[0] == '*':
            return interpret(p[1], env) * interpret(p[2], env)
        elif p[0] == '/':
            return interpret(p[1], env) / interpret(p[2], env)
        elif p[0] == '%':
            return interpret(p[1], env) % interpret(p[2], env)
        elif p[0] == '++' and p[1] and p[1][0] == 'identifier':
            if p[1][1] not in env:
                print('Undefined variable {0}'.format(p[1][1]))
                exit()
            value = env[p[1][1]]
            env[p[1][1]] += 1
            return value
        elif p[0] == '--':
            return interpret(p[1], env) - 1
        elif p[0] == '>=':
            return interpret(p[1], env) >= interpret(p[2], env)
        elif p[0] == '>':
            return interpret(p[1], env) > interpret(p[2], env)
        elif p[0] == '<=':
            return interpret(p[1], env) <= interpret(p[2], env)
        elif p[0] == '<':
            return interpret(p[1], env) < interpret(p[2], env)
        elif p[0] == '==':
            return interpret(p[1], env) == interpret(p[2], env)
        elif p[0] == '!' and p[1] == '=':
            return interpret(p[1], env) != interpret(p[2], env)
        elif p[0] == '(' and p[1] == ')':
            return interpret(p[2], env)
        elif p[0] == 'disp':
            if p[1] not in env:
                print('undeclared variable!')
                exit()
            print(env[p[1]])
        # elif p[0] == 'disp_list':
        #     if p[1] not in env:
        #         print('undeclared variable!')
        #         exit()
        #     for i in env[p[1]]:
        #         print(env[i])

        # elif p[0] == 'til':
        #         return interpret(p[4])
        elif p[0] == 'if-then':
            if interpret(p[1], env) == True:
                return interpret(p[2], env)
        elif p[0] == 'if-then-else':
            if interpret(p[1], env) == True:
                return interpret(p[2], env)
            else:
                return interpret(p[3], env)

        elif p[0] == 'til':
            interpret(p[1], env)
            _results = []
            while(interpret(p[2], env)):
                _results.append(interpret(p[4], env))
                interpret(p[3], env)
            return _results
            # if interpret(p[1], env) == True:
            #     return interpret(p[2], env)


        # elif p[0] == 'maybe-then':
        #
        #        if p[1] == True:
        #            return interpret(p[2], env)
        #        else:
        #            return
        # elif p[0] == 'stmt':
        #     return  interpret(p[1], env)

        # elif p[0] == 'maybe' and p[3] == 'or':
        #     pass
        # elif p[0] == 'exps':
        #     interpret(p[1], env)
        # elif p[0] == 'maybe':
        #     if(interpret(p[1], env) == True):
        #         interpret(p[2], env)
        #     else:
        #         return ''
        # elif p[0] == 'maybe' and p[1] == 'or':
        #     pass
        elif p[0] == 'suppose':
            if p[1] in env:
                print('duplicate identifier detected')
                exit()
                return ''
            env[p[1]] = interpret(p[2], env)
            return ''
        elif p[0] == 'snake':
            if p[1] in env:
                print('duplicate identifier detected')
                exit()
                return ''
            env[p[1]] = interpret(p[2], env)
            return ''
        elif p[0] == 'access':
            if p[1] in env:
                 index = interpret(p[2], env)
                 if index > len(env[p[1]]):
                     print("list index out of range")
                     exit()
                     return ''
                 return env[p[1]][int(index)]
        elif p[0] == '=':
            if p[1] in env:
                env[p[1]] = interpret(p[2], env)
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

env = {}

while True:

    # Testing

    try:
        input_string = input('>> ')
    except EOFError:
        break
    if not input_string:
        continue
    yapl_mnm_ast = yapl_mnm_parser.parse(input_string, lexer=yapl_mnm_lexer)
    interpret(yapl_mnm_ast, env)
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