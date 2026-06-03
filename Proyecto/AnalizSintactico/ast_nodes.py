"""
Nodos del Árbol de Sintaxis Abstracta (AST)
"""

class ASTNode:
    """Clase base para todos los nodos del AST"""
    pass


class Program(ASTNode):
    """Raíz del programa"""
    def __init__(self, declarations):
        self.declarations = declarations  # Lista de funciones y variables globales


class FunctionDecl(ASTNode):
    """Declaración de función"""
    def __init__(self, return_type, name, params, body):
        self.return_type = return_type
        self.name = name
        self.params = params  # Lista de ParamDecl
        self.body = body  # CompoundStatement


class ParamDecl(ASTNode):
    """Declaración de parámetro"""
    def __init__(self, param_type, name):
        self.param_type = param_type
        self.name = name


class VarDecl(ASTNode):
    """Declaración de variable"""
    def __init__(self, var_type, name, init_value=None):
        self.var_type = var_type
        self.name = name
        self.init_value = init_value  # Puede ser None


class CompoundStatement(ASTNode):
    """Bloque de código { ... }"""
    def __init__(self, statements):
        self.statements = statements  # Lista de statements


class IfStatement(ASTNode):
    """Sentencia if/else"""
    def __init__(self, condition, then_stmt, else_stmt=None):
        self.condition = condition
        self.then_stmt = then_stmt
        self.else_stmt = else_stmt


class WhileStatement(ASTNode):
    """Sentencia while"""
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class ForStatement(ASTNode):
    """Sentencia for"""
    def __init__(self, init, condition, increment, body):
        self.init = init
        self.condition = condition
        self.increment = increment
        self.body = body


class ReturnStatement(ASTNode):
    """Sentencia return"""
    def __init__(self, expr=None):
        self.expr = expr  # Puede ser None


class BreakStatement(ASTNode):
    """Sentencia break"""
    pass


class ContinueStatement(ASTNode):
    """Sentencia continue"""
    pass


class ExpressionStatement(ASTNode):
    """Expresión como sentencia"""
    def __init__(self, expr):
        self.expr = expr


class BinaryOp(ASTNode):
    """Operación binaria (a + b, a < b, etc)"""
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class UnaryOp(ASTNode):
    """Operación unaria (!a, -b, ++c, etc)"""
    def __init__(self, op, operand, is_prefix=True):
        self.op = op
        self.operand = operand
        self.is_prefix = is_prefix


class Assignment(ASTNode):
    """Asignación (a = 5, a += 3, etc)"""
    def __init__(self, target, op, value):
        self.target = target  # Identificador
        self.op = op  # =, +=, -=, etc
        self.value = value  # Expresión


class FunctionCall(ASTNode):
    """Llamada a función"""
    def __init__(self, name, args):
        self.name = name
        self.args = args  # Lista de expresiones


class ArrayAccess(ASTNode):
    """Acceso a elemento de array"""
    def __init__(self, array, index):
        self.array = array
        self.index = index


class PointerDeref(ASTNode):
    """Desreferencia de puntero (*ptr)"""
    def __init__(self, expr):
        self.expr = expr


class AddressOf(ASTNode):
    """Dirección de (&var)"""
    def __init__(self, expr):
        self.expr = expr


class Identifier(ASTNode):
    """Identificador (nombre de variable/función)"""
    def __init__(self, name):
        self.name = name


class IntLiteral(ASTNode):
    """Literal entero"""
    def __init__(self, value):
        self.value = int(value)


class FloatLiteral(ASTNode):
    """Literal flotante"""
    def __init__(self, value):
        self.value = float(value)


class StringLiteral(ASTNode):
    """Literal de cadena"""
    def __init__(self, value):
        self.value = value


class CharLiteral(ASTNode):
    """Literal de carácter"""
    def __init__(self, value):
        self.value = value
