import yapl_mnm_tokens
import ply.lex as lex
import ply.yacc as yacc

start = 'yapl_mnm'

precedence = (
    ('left', 'OROR'),
    ('left', 'ANDAND'),
    ('left', 'EQUALEQUAL'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'), #Unary minus operator
    ('right', 'NOT'),
)

tokens = (
    # BASIC LANG STUFF
    'ANDAND',  # &&
    'COMMA',  # ,
    'DIVIDE',  # /
    'EQUAL',  # =
    'EQUALEQUAL',  # ==
    'FALSE',  # false
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
    'TRUE',  # true

)

def p_yapl_mnm(p):
    '''
    yapl_mnm : exp
             | assign_identifier
             | empty

    '''
    print(interpret(p[1]))

def p_empty(p):
    'empty :'
    p[0] = None



def p_assign_identifier(p):
    '''
    assign_identifier : IDENTIFIER EQUAL exp
    '''
    p[0] = ('=', p[1], p[3])

def p_exp(p):
    '''
    exp : exp TIMES exp
        | exp DIVIDE exp
        | exp PLUS exp
        | exp MINUS exp
    '''
    p[0] = (p[2], p[1], p[3])

def p_exp_uminus(p):
    'exp : MINUS exp %prec UMINUS'
    p[0] = -p[2]

def p_exp_number(p):
    '''
    exp : NUMBER
    '''
    p[0] = p[1]

def p_exp_identifier(p):
    '''
    exp : IDENTIFIER
    '''
    p[0] = ('var', p[1])

def p_error(p):
    print('Syntax Error found in input!')

env = {}

#Testing
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
        elif p[0] == '=':
            env[p[1]] = interpret(p[2])
            return ''
        elif p[0] == 'var':
            if p[1] not in env:
                return 'undeclared variable found!'
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
