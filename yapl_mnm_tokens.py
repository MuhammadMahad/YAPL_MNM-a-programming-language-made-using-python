# YAPL_MNM
import ply.lex as lex

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
    'snake': 'SNAKE'

}

tokens = list(tokens) + list(reserved.values())

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


t_ignore = ' \t\v\r'  # whitespace

t_ANDAND = r'&&'
t_COMMA = r','
t_DIVIDE = r'/'
t_EQUALEQUAL = r'=='
t_EQUAL = r'='
t_FALSE = r'false'
t_GE = r'>='
t_GT = r'>'
t_LBRACE = r'\{'
t_LE = r'<='
t_LPAREN = r'\('
t_LT = r'<'
t_MINUS = r'-'
t_NOT = r'!'
t_OROR = r'\|\|'
t_PLUS = r'\+'
t_RBRACE = r'\}'
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_TIMES = r'\*'
t_TRUE = r'true'


def t_IDENTIFIER(token):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    token.type = reserved.get(token.value, 'IDENTIFIER')
    return token


def t_NUMBER(token):
    r'-?[0-9]+(?:\.[0-9]*)?'
    token.value = float(token.value)
    return token


def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1


def t_error(t):
    print("YAPL_MNM Lexer: Illegal character " + t.value[0])
    t.lexer.skip(1)


# testing

# lexer = lex.lex()
#
#
# def test_lexer(input_string):
#     lexer.input(input_string)
#     result = []
#     while True:
#         tok = lexer.token()
#         if not tok: break
#         result.append(tok)
#     return result
#
# while True:
#     try:
#         input_string = input('Enter string for lexical analysis:\n')
#     except EOFError:
#         break
#     print(test_lexer(input_string))
