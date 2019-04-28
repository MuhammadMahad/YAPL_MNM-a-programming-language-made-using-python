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
    'LPAREN',  # (
    'LT',  # <
    'MINUS',  # -
    'NOT',  # !
    'NUMBER',  #
    'OROR',  # ||
    'PLUS',  # +
    'RBRACE',  # }
    'RPAREN',  # )
    'SEMICOLON',  # ;
    'STRING',  #### Not used in this problem.
    'TIMES',  # *
    'MOD',  # %
    'PLUSPLUS', # ++
    'MINUSMINUS', # --
    'LSQUAREPAREN', # [
    'RSQUAREPAREN', # ]

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

}

tokens = list(tokens) + list(reserved.values())


def p_yapl_mnm(p):
    '''
    yapl_mnm : exp
             | assign_identifier
             | snake_list
             | snake_list_access
             | rel_exp
             | maybe
             | empty
    '''
    print(interpret(p[1]))

def p_maybe(p):
    '''
    conditional : MAYBE rel_exp statements
    '''
    p[0] = (p[1], p[2], p[3])

def p_or_maybe(p):
    '''
    conditional : MAYBE rel_exp statements OR statements
    '''
    p[0] = (p[1], p[4], p[2], p[3], p[5])

def p_statements(p):
    '''
    statements :  LBRACE exps LBRACE
    '''
    p[0] = (p[2])

def p_exps(p):
    '''
    exps : exp exps
         | empty
    '''
    p[0] = (p[1], p[2])

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
    num_snake : num_snake COMMA NUMBER
              | NUMBER
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


def p_assign_identifier_error(p):
    print('duplicate identifier detected')


def p_exp(p):
    '''
    exp : exp TIMES exp
        | exp DIVIDE exp
        | exp PLUS exp
        | exp MINUS exp
        | exp MOD exp
    '''
    p[0] = (p[2], p[1], p[3])

def p_parentheses(p):
    '''
    exp : LPAREN exp RPAREN
    '''
    p[0] = (p[1],p[2], p[3])

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

def p_error(p):
    print('Syntax Error found in input!')


env = {}

# Testing
yapl_mnm_lexer = lex.lex(module=yapl_mnm_tokens)
yapl_mnm_parser = yacc.yacc()


def interpret(p):
    global env
    if type(p) == tuple:
        if p[0] == '+':
            return interpret(p[1]) + interpret(p[2])
        elif p[0] == '-':
            return interpret(p[1]) - interpret(p[2])
        elif p[0] == '*':
            return interpret(p[1]) * interpret(p[2])
        elif p[0] == '/':
            return interpret(p[1]) / interpret(p[2])
        elif p[0] == '%':
            return interpret(p[1]) % interpret(p[2])
        elif p[0] == '++':
            return interpret(p[1]) + 1
        elif p[0] == '--':
            return interpret(p[1]) - 1
        elif p[0] == '>=':
            return interpret(p[1]) >= interpret(p[2])
        elif p[0] == '>':
            return interpret(p[1]) > interpret(p[2])
        elif p[0] == '<=':
            return interpret(p[1]) <= interpret(p[2])
        elif p[0] == '<':
            return interpret(p[1]) < interpret(p[2])
        elif p[0] == '==':
            return interpret(p[1]) == interpret(p[2])
        elif p[0] == '!' and p[1] == '=':
            return interpret(p[1]) != interpret(p[2])
        elif p[0] == 'suppose':
            if p[1] in env:
                print('duplicate identifier detected')
                exit()
                return ''
            env[p[1]] = interpret(p[2])
            return ''
        elif p[0] == 'snake':
            if p[1] in env:
                print('duplicate identifier detected')
                exit()
                return ''
            env[p[1]] = interpret(p[2])
            return ''
        elif p[0] == 'access':
            if p[1] in env:
                 index = interpret(p[2])
                 if index > len(env[p[1]]):
                     print("list index out of range")
                     exit()
                     return ''
                 return env[p[1]][int(index)]
        elif p[0] == '=':
            if p[1] in env:
                env[p[1]] = interpret(p[2])
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


while True:
    try:
        input_string = input('>> ')
    except EOFError:
        break
    yapl_mnm_ast = yapl_mnm_parser.parse(input_string, lexer=yapl_mnm_lexer)
    print(yapl_mnm_ast)

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