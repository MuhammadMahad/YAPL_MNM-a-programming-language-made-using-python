#YAPL_MNM
import ply.lex as lex



tokens = (

        # MY LANG STUFF
        # 'SUPPOSE',      # var -> suppose
        # 'MAYBE',        # maybe => if
        # 'OR',           # else => or #else if => or maybe
        # 'TIL',          # for -> til
        # 'UNTIL',        # while -> until
        # 'WORK',         # do -> work
        # 'MACHINE',      # function -> machine
        # 'FIRE',         # return -> fire
        # 'COMPLEX',      # struct -> complex
        # 'SNAKE',        # list -> snake
        # 'KEYWORD',      #

        # BASIC LANG STUFF
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   #### Not used in this problem.
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       #### Not used in this problem.
        'TIMES',        # *
        'TRUE',         # true

)







reserved = {


'suppose' : 'SUPPOSE',
'maybe' : 'MAYBE',
'or' : 'OR',
'til' : 'TIL',
'until' : 'UNTIL',
'work' : 'WORK',
'machine' : 'MACHINE',
'fire' : 'FIRE',
'complex' : 'COMPLEX',
'snake' : 'SNAKE'


}

# tokens = ['ANDAND','COMMA', 'DIVIDE','EQUAL','EQUALEQUAL','FALSE','GE','GT','IDENTIFIER','LBRACE','LE','LPAREN','LT',
# 'MINUS',
# 'NOT',
# 'NUMBER',
# 'OROR',
# 'PLUS',
# 'RBRACE',
# 'RPAREN',
# 'SEMICOLON',
# 'STRING',
# 'TIMES',
# 'TRUE'] + list(reserved.values())

tokens = list(tokens) + list(reserved.values())
# MY LANG STUFF TOKENS

# t_SUPPOSE = r'suppose'
# t_MAYBE =  r'maybe'
# t_OR =  r'or'
# t_TIL = r'til'
# t_UNTIL = r'until'
# t_WORK = r'work'
# t_MACHINE = r'machine'
# t_FIRE = r'fire'
# t_COMPLEX = r'complex'
# t_SNAKE = r'snake'

# BASIC LANG STUFF TOKENS

states = (('YAPLMNMeolcomment', 'exclusive'), ('YAPLMNMdelimitedcomment', 'exclusive'),)


def t_YAPLMNMeolcomment(t):
    r'//'
    t.lexer.begin('YAPL_MNM_eolcomment')


def t_YAPLMNMeolcomment_end(t):
    r'\n'
    t.lexer.begin('INITIAL')


def t_YAPLMNMdelimitedcomment(t):
    r'/\*'
    t.lexer.begin('YAPL_MNM_delimitedcomment')


def t_YAPLMNMdelimitedcomment_end(t):
    r'\*/'
    t.lexer.begin('INITIAL')


t_YAPLMNMdelimitedcomment_ignore = r'.'
t_YAPLMNMeolcomment_ignore = r'.'


def t_YAPLMNMeolcomment_error(t):
    t.lexer.skip(1)


def t_YAPLMNMdelimitedcomment_error(t):
    t.lexer.skip(1)


t_ignore = ' \t\v\r' # shortcut for whitespace

t_ANDAND =  r'&&'
t_COMMA =  r','
t_DIVIDE =  r'/'
t_EQUALEQUAL = r'=='
t_EQUAL = r'='
t_FALSE =  r'false'
t_GE =  r'>='
t_GT =   r'>'
t_LBRACE = r'\{'
t_LE =  r'<='
t_LPAREN =   r'\('
t_LT = r'<'
t_MINUS = r'-'
t_NOT = r'!'
t_OROR = r'\|\|'
t_PLUS = r'\+'
t_RBRACE =  r'\}'
t_RPAREN =  r'\)'
t_SEMICOLON =   r';'
t_TIMES = r'\*'
t_TRUE =  r'true'







# def t_KEYWORD(token):
#     r'suppose | maybe | or | til | until | work | machine | fire | complex | snake'
#     return token

def t_IDENTIFIER(token):

    r'[a-zA-Z_][a-zA-Z_0-9]*'
    token.type = reserved.get(token.value, 'IDENTIFIER')
    return token
    # if 'suppose' or 'maybe' or 'or' or 'til' or 'until' or 'work' or 'machine' or 'fire' or 'complex' or 'snake' in token.value:
    #     return t_KEYWORD(token)
    # else:
    #     return token

def t_NUMBER(token):
    r'-?[0-9]+(?:\.[0-9]*)?'
    token.value = float(token.value)
    return token

def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1


def t_error(t):
    print("YAPL_MNM Lexer: Illegal character " + t.value[0])
    t.lexer.skip(1)


# def t_WHITESPACE(token):
#     r' '
#     pass
#
# def t_YAPL_MNM_eolcomment(token):
#     pass



#testing

lexer = lex.lex()

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result


input_string = input('Enter string for lexical analysis:\n')

print(test_lexer(input_string))