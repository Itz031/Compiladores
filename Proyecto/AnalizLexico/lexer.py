"""
Análisis Léxico (Lexer) - Tokenización de código C
"""

import re
from tokens import Token, TokenType, KEYWORDS


class Lexer:
    """Analizador léxico que convierte código fuente en tokens"""
    
    def __init__(self, source_code):
        self.source = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []
    
    def current_char(self):
        """Retorna el carácter actual sin avanzar"""
        if self.position >= len(self.source):
            return None
        return self.source[self.position]
    
    def peek_char(self, offset=1):
        """Retorna el carácter en la posición actual + offset"""
        pos = self.position + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self):
        """Avanza una posición y actualiza línea/columna"""
        if self.position < len(self.source):
            if self.source[self.position] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.position += 1
    
    def skip_whitespace(self):
        """Salta espacios en blanco (excepto newlines que pueden ser importantes)"""
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_single_line_comment(self):
        """Salta comentarios de una línea // """
        if self.current_char() == '/' and self.peek_char() == '/':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
    
    def skip_multi_line_comment(self):
        """Salta comentarios de múltiples líneas /* ... */"""
        if self.current_char() == '/' and self.peek_char() == '*':
            self.advance()  # /
            self.advance()  # *
            while self.current_char():
                if self.current_char() == '*' and self.peek_char() == '/':
                    self.advance()  # *
                    self.advance()  # /
                    return
                self.advance()
    
    def read_string(self):
        """Lee una cadena de caracteres entre comillas"""
        quote_char = self.current_char()
        value = quote_char
        self.advance()
        
        while self.current_char() and self.current_char() != quote_char:
            if self.current_char() == '\\':
                value += self.current_char()
                self.advance()
                if self.current_char():
                    value += self.current_char()
                    self.advance()
            else:
                value += self.current_char()
                self.advance()
        
        if self.current_char() == quote_char:
            value += self.current_char()
            self.advance()
        
        return value
    
    def read_number(self):
        """Lee un número (entero o flotante)"""
        value = ''
        has_dot = False
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            if self.current_char() == '.':
                if has_dot:
                    break
                has_dot = True
            value += self.current_char()
            self.advance()
        
        # Exponente científico (1e5, 2.5e-3)
        if self.current_char() and self.current_char() in 'eE':
            value += self.current_char()
            self.advance()
            if self.current_char() and self.current_char() in '+-':
                value += self.current_char()
                self.advance()
            while self.current_char() and self.current_char().isdigit():
                value += self.current_char()
                self.advance()
        
        return value
    
    def read_identifier(self):
        """Lee un identificador o palabra clave"""
        value = ''
        
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            value += self.current_char()
            self.advance()
        
        return value
    
    def add_token(self, token_type, value):
        """Añade un token a la lista"""
        token = Token(token_type, value, self.line, self.column - len(value))
        self.tokens.append(token)
    
    def tokenize(self):
        """Realiza el análisis léxico completo"""
        
        while self.position < len(self.source):
            self.skip_whitespace()
            
            # Fin del archivo
            if self.position >= len(self.source):
                break
            
            current = self.current_char()
            start_line = self.line
            start_column = self.column
            
            # Comentarios
            if current == '/' and self.peek_char() == '/':
                self.skip_single_line_comment()
                continue
            
            if current == '/' and self.peek_char() == '*':
                self.skip_multi_line_comment()
                continue
            
            # Strings y caracteres
            if current in '"\'':
                value = self.read_string()
                token_type = TokenType.STRING_LITERAL if current == '"' else TokenType.CHAR_LITERAL
                self.add_token(token_type, value)
                continue
            
            # Números
            if current.isdigit():
                value = self.read_number()
                token_type = TokenType.FLOAT_LITERAL if '.' in value or 'e' in value.lower() else TokenType.INT_LITERAL
                self.add_token(token_type, value)
                continue
            
            # Identificadores y palabras clave
            if current.isalpha() or current == '_':
                value = self.read_identifier()
                if value in KEYWORDS:
                    self.add_token(KEYWORDS[value], value)
                else:
                    self.add_token(TokenType.IDENTIFIER, value)
                continue
            
            # Newline
            if current == '\n':
                self.advance()
                continue
            
            # Operadores y delimitadores (dos caracteres)
            two_char = current + (self.peek_char() or '')
            two_char_tokens = {
                '==': TokenType.EQ,
                '!=': TokenType.NE,
                '<=': TokenType.LE,
                '>=': TokenType.GE,
                '&&': TokenType.AND,
                '||': TokenType.OR,
                '++': TokenType.INCREMENT,
                '--': TokenType.DECREMENT,
                '<<': TokenType.LSHIFT,
                '>>': TokenType.RSHIFT,
                '+=': TokenType.PLUS_ASSIGN,
                '-=': TokenType.MINUS_ASSIGN,
                '*=': TokenType.STAR_ASSIGN,
                '/=': TokenType.SLASH_ASSIGN,
                '%=': TokenType.PERCENT_ASSIGN,
                '->': TokenType.ARROW,
            }
            
            if two_char in two_char_tokens:
                self.add_token(two_char_tokens[two_char], two_char)
                self.advance()
                self.advance()
                continue
            
            # Operadores y delimitadores (un carácter)
            one_char_tokens = {
                '+': TokenType.PLUS,
                '-': TokenType.MINUS,
                '*': TokenType.STAR,
                '/': TokenType.SLASH,
                '%': TokenType.PERCENT,
                '=': TokenType.ASSIGN,
                '<': TokenType.LT,
                '>': TokenType.GT,
                '!': TokenType.NOT,
                '&': TokenType.BIT_AND,
                '|': TokenType.BIT_OR,
                '^': TokenType.BIT_XOR,
                '~': TokenType.BIT_NOT,
                '(': TokenType.LPAREN,
                ')': TokenType.RPAREN,
                '{': TokenType.LBRACE,
                '}': TokenType.RBRACE,
                '[': TokenType.LBRACKET,
                ']': TokenType.RBRACKET,
                ';': TokenType.SEMICOLON,
                ',': TokenType.COMMA,
                '.': TokenType.DOT,
                ':': TokenType.COLON,
                '?': TokenType.QUESTION,
            }
            
            if current in one_char_tokens:
                self.add_token(one_char_tokens[current], current)
                self.advance()
                continue
            
            # Carácter desconocido
            self.add_token(TokenType.UNKNOWN, current)
            self.advance()
        
        # Añadir EOF
        self.add_token(TokenType.EOF, 'EOF')
        return self.tokens


def analyze_file(file_path):
    """Analiza un archivo C y retorna los tokens"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file_path}'")
        return None
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        return None
    
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    
    return tokens


def print_tokens(tokens):
    """Imprime los tokens de forma legible"""
    print("\n--- Análisis Léxico Completado ---\n")
    for token in tokens:
        if token.type != TokenType.EOF:
            print(f"Línea {token.line:3d} | {token.type.name:20s} | '{token.value}'")
    print(f"\nTotal de tokens: {len(tokens)}")
