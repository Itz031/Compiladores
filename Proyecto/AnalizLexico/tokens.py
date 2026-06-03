"""
Definición de tipos de tokens para el análisis léxico.
"""

from enum import Enum, auto

class TokenType(Enum):
    """Enumeration of all token types"""
    
    # Literales
    INT_LITERAL = auto()
    FLOAT_LITERAL = auto()
    STRING_LITERAL = auto()
    CHAR_LITERAL = auto()
    BOOL_LITERAL = auto()
    
    # Palabras clave
    INT = auto()
    FLOAT = auto()
    CHAR = auto()
    VOID = auto()
    BOOL = auto()
    DOUBLE = auto()
    SHORT = auto()
    LONG = auto()
    UNSIGNED = auto()
    SIGNED = auto()
    
    # Control de flujo
    IF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    DO = auto()
    SWITCH = auto()
    CASE = auto()
    DEFAULT = auto()
    BREAK = auto()
    CONTINUE = auto()
    RETURN = auto()
    
    # Otros keywords
    STRUCT = auto()
    UNION = auto()
    ENUM = auto()
    TYPEDEF = auto()
    STATIC = auto()
    EXTERN = auto()
    CONST = auto()
    VOLATILE = auto()
    SIZEOF = auto()
    
    # Identificadores
    IDENTIFIER = auto()
    
    # Operadores
    PLUS = auto()          # +
    MINUS = auto()         # -
    STAR = auto()          # *
    SLASH = auto()         # /
    PERCENT = auto()       # %
    ASSIGN = auto()        # =
    PLUS_ASSIGN = auto()   # +=
    MINUS_ASSIGN = auto()  # -=
    STAR_ASSIGN = auto()   # *=
    SLASH_ASSIGN = auto()  # /=
    PERCENT_ASSIGN = auto() # %=
    
    # Operadores de comparación
    EQ = auto()            # ==
    NE = auto()            # !=
    LT = auto()            # <
    LE = auto()            # <=
    GT = auto()            # >
    GE = auto()            # >=
    
    # Operadores lógicos
    AND = auto()           # &&
    OR = auto()            # ||
    NOT = auto()           # !
    
    # Operadores bitwise
    BIT_AND = auto()       # &
    BIT_OR = auto()        # |
    BIT_XOR = auto()       # ^
    BIT_NOT = auto()       # ~
    LSHIFT = auto()        # <<
    RSHIFT = auto()        # >>
    
    # Incremento/Decremento
    INCREMENT = auto()     # ++
    DECREMENT = auto()     # --
    
    # Delimitadores
    LPAREN = auto()        # (
    RPAREN = auto()        # )
    LBRACE = auto()        # {
    RBRACE = auto()        # }
    LBRACKET = auto()      # [
    RBRACKET = auto()      # ]
    SEMICOLON = auto()     # ;
    COMMA = auto()         # ,
    DOT = auto()           # .
    ARROW = auto()         # ->
    COLON = auto()         # :
    QUESTION = auto()      # ?
    
    # Especiales
    EOF = auto()
    UNKNOWN = auto()
    NEWLINE = auto()


class Token:
    """Representa un token con su tipo, valor y posición"""
    
    def __init__(self, token_type, value, line, column):
        self.type = token_type
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type.name}, '{self.value}', {self.line}:{self.column})"
    
    def __str__(self):
        return f"<{self.type.name} | {self.value}>"


# Palabras clave reservadas
KEYWORDS = {
    'int': TokenType.INT,
    'float': TokenType.FLOAT,
    'char': TokenType.CHAR,
    'void': TokenType.VOID,
    'bool': TokenType.BOOL,
    'double': TokenType.DOUBLE,
    'short': TokenType.SHORT,
    'long': TokenType.LONG,
    'unsigned': TokenType.UNSIGNED,
    'signed': TokenType.SIGNED,
    'if': TokenType.IF,
    'else': TokenType.ELSE,
    'for': TokenType.FOR,
    'while': TokenType.WHILE,
    'do': TokenType.DO,
    'switch': TokenType.SWITCH,
    'case': TokenType.CASE,
    'default': TokenType.DEFAULT,
    'break': TokenType.BREAK,
    'continue': TokenType.CONTINUE,
    'return': TokenType.RETURN,
    'struct': TokenType.STRUCT,
    'union': TokenType.UNION,
    'enum': TokenType.ENUM,
    'typedef': TokenType.TYPEDEF,
    'static': TokenType.STATIC,
    'extern': TokenType.EXTERN,
    'const': TokenType.CONST,
    'volatile': TokenType.VOLATILE,
    'sizeof': TokenType.SIZEOF,
    'true': TokenType.BOOL_LITERAL,
    'false': TokenType.BOOL_LITERAL,
}