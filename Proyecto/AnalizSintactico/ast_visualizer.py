"""
Visualizador del Árbol de Sintaxis Abstracta (AST)
"""

from ast_nodes import *


class ASTVisualizer:
    """Genera una representación visual del AST"""
    
    def __init__(self):
        self.indent_level = 0
        self.output = []
    
    def visualize(self, node, show_details=True):
        """Genera la representación visual del AST"""
        self.output = []
        self.indent_level = 0
        self._visit(node, show_details)
        return '\n'.join(self.output)
    
    def _indent(self):
        """Retorna la indentación actual"""
        return "  " * self.indent_level
    
    def _add_line(self, text):
        """Añade una línea al output"""
        self.output.append(self._indent() + text)
    
    def _visit(self, node, show_details):
        """Visita un nodo del AST"""
        if node is None:
            return
        
        if isinstance(node, Program):
            self._visit_program(node, show_details)
        elif isinstance(node, FunctionDecl):
            self._visit_function_decl(node, show_details)
        elif isinstance(node, VarDecl):
            self._visit_var_decl(node, show_details)
        elif isinstance(node, CompoundStatement):
            self._visit_compound_statement(node, show_details)
        elif isinstance(node, IfStatement):
            self._visit_if_statement(node, show_details)
        elif isinstance(node, WhileStatement):
            self._visit_while_statement(node, show_details)
        elif isinstance(node, ForStatement):
            self._visit_for_statement(node, show_details)
        elif isinstance(node, ReturnStatement):
            self._visit_return_statement(node, show_details)
        elif isinstance(node, BreakStatement):
            self._add_line("├─ BREAK")
        elif isinstance(node, ContinueStatement):
            self._add_line("├─ CONTINUE")
        elif isinstance(node, ExpressionStatement):
            self._visit_expression_statement(node, show_details)
        elif isinstance(node, BinaryOp):
            self._visit_binary_op(node, show_details)
        elif isinstance(node, UnaryOp):
            self._visit_unary_op(node, show_details)
        elif isinstance(node, Assignment):
            self._visit_assignment(node, show_details)
        elif isinstance(node, FunctionCall):
            self._visit_function_call(node, show_details)
        elif isinstance(node, ArrayAccess):
            self._visit_array_access(node, show_details)
        elif isinstance(node, Identifier):
            self._add_line(f"├─ ID: {node.name}")
        elif isinstance(node, IntLiteral):
            self._add_line(f"├─ INT: {node.value}")
        elif isinstance(node, FloatLiteral):
            self._add_line(f"├─ FLOAT: {node.value}")
        elif isinstance(node, StringLiteral):
            self._add_line(f"├─ STRING: {node.value}")
        elif isinstance(node, CharLiteral):
            self._add_line(f"├─ CHAR: {node.value}")
        elif isinstance(node, ParamDecl):
            self._add_line(f"├─ PARAM: {node.param_type} {node.name}")
    
    def _visit_program(self, node, show_details):
        """Visita el programa"""
        self._add_line("┌─ PROGRAMA")
        self.indent_level += 1
        
        for i, decl in enumerate(node.declarations):
            if i == len(node.declarations) - 1:
                self._add_line("└─ DECLARACIÓN")
            else:
                self._add_line("├─ DECLARACIÓN")
            
            self.indent_level += 1
            self._visit(decl, show_details)
            self.indent_level -= 1
        
        self.indent_level -= 1
    
    def _visit_function_decl(self, node, show_details):
        """Visita una declaración de función"""
        self._add_line(f"├─ FUNCIÓN: {node.name} () -> {node.return_type}")
        self.indent_level += 1
        
        if node.params:
            self._add_line("├─ PARÁMETROS:")
            self.indent_level += 1
            for i, param in enumerate(node.params):
                if i == len(node.params) - 1:
                    self._add_line(f"└─ {param.param_type} {param.name}")
                else:
                    self._add_line(f"├─ {param.param_type} {param.name}")
            self.indent_level -= 1
        
        self._add_line("├─ CUERPO:")
        self.indent_level += 1
        self._visit(node.body, show_details)
        self.indent_level -= 1
        
        self.indent_level -= 1
    
    def _visit_var_decl(self, node, show_details):
        """Visita una declaración de variable"""
        if node.init_value:
            self._add_line(f"├─ VAR: {node.var_type} {node.name} =")
            self.indent_level += 1
            self._visit(node.init_value, show_details)
            self.indent_level -= 1
        else:
            self._add_line(f"├─ VAR: {node.var_type} {node.name}")
    
    def _visit_compound_statement(self, node, show_details):
        """Visita un bloque de sentencias"""
        self._add_line("├─ BLOQUE {}")
        self.indent_level += 1
        
        for i, stmt in enumerate(node.statements):
            if i == len(node.statements) - 1:
                self._add_line("└─ SENTENCIA")
            else:
                self._add_line("├─ SENTENCIA")
            
            self.indent_level += 1
            self._visit(stmt, show_details)
            self.indent_level -= 1
        
        self.indent_level -= 1
    
    def _visit_if_statement(self, node, show_details):
        """Visita una sentencia if"""
        self._add_line("├─ IF")
        self.indent_level += 1
        
        self._add_line("├─ CONDICIÓN:")
        self.indent_level += 1
        self._visit(node.condition, show_details)
        self.indent_level -= 1
        
        self._add_line("├─ ENTONCES:")
        self.indent_level += 1
        self._visit(node.then_stmt, show_details)
        self.indent_level -= 1
        
        if node.else_stmt:
            self._add_line("├─ SINO:")
            self.indent_level += 1
            self._visit(node.else_stmt, show_details)
            self.indent_level -= 1
        
        self.indent_level -= 1
    
    def _visit_while_statement(self, node, show_details):
        """Visita una sentencia while"""
        self._add_line("├─ WHILE")
        self.indent_level += 1
        
        self._add_line("├─ CONDICIÓN:")
        self.indent_level += 1
        self._visit(node.condition, show_details)
        self.indent_level -= 1
        
        self._add_line("├─ CUERPO:")
        self.indent_level += 1
        self._visit(node.body, show_details)
        self.indent_level -= 1
        
        self.indent_level -= 1
    
    def _visit_for_statement(self, node, show_details):
        """Visita una sentencia for"""
        self._add_line("├─ FOR")
        self.indent_level += 1
        
        if node.init:
            self._add_line("├─ INICIALIZACIÓN:")
            self.indent_level += 1
            self._visit(node.init, show_details)
            self.indent_level -= 1
        
        if node.condition:
            self._add_line("├─ CONDICIÓN:")
            self.indent_level += 1
            self._visit(node.condition, show_details)
            self.indent_level -= 1
        
        if node.increment:
            self._add_line("├─ INCREMENTO:")
            self.indent_level += 1
            self._visit(node.increment, show_details)
            self.indent_level -= 1
        
        self._add_line("├─ CUERPO:")
        self.indent_level += 1
        self._visit(node.body, show_details)
        self.indent_level -= 1
        
        self.indent_level -= 1
    
    def _visit_return_statement(self, node, show_details):
        """Visita una sentencia return"""
        if node.expr:
            self._add_line("├─ RETURN:")
            self.indent_level += 1
            self._visit(node.expr, show_details)
            self.indent_level -= 1
        else:
            self._add_line("├─ RETURN")
    
    def _visit_expression_statement(self, node, show_details):
        """Visita una sentencia expresión"""
        self._add_line("├─ EXPRESIÓN:")
        self.indent_level += 1
        self._visit(node.expr, show_details)
        self.indent_level -= 1
    
    def _visit_binary_op(self, node, show_details):
        """Visita una operación binaria"""
        self._add_line(f"├─ OP: '{node.op}'")
        self.indent_level += 1
        
        self._add_line("├─ IZQUIERDA:")
        self.indent_level += 1
        self._visit(node.left, show_details)
        self.indent_level -= 1
        
        self._add_line("├─ DERECHA:")
        self.indent_level += 1
        self._visit(node.right, show_details)
        self.indent_level -= 1
        
        self.indent_level -= 1
    
    def _visit_unary_op(self, node, show_details):
        """Visita una operación unaria"""
        prefix_postfix = "PREFIJO" if node.is_prefix else "POSTFIJO"
        self._add_line(f"├─ UNARIA ({prefix_postfix}): '{node.op}'")
        self.indent_level += 1
        self._visit(node.operand, show_details)
        self.indent_level -= 1
    
    def _visit_assignment(self, node, show_details):
        """Visita una asignación"""
        self._add_line(f"├─ ASIGNACIÓN: '{node.op}'")
        self.indent_level += 1
        
        self._add_line("├─ OBJETIVO:")
        self.indent_level += 1
        self._visit(node.target, show_details)
        self.indent_level -= 1
        
        self._add_line("├─ VALOR:")
        self.indent_level += 1
        self._visit(node.value, show_details)
        self.indent_level -= 1
        
        self.indent_level -= 1
    
    def _visit_function_call(self, node, show_details):
        """Visita una llamada a función"""
        self._add_line(f"├─ LLAMADA: {node.name}()")
        self.indent_level += 1
        
        if node.args:
            self._add_line("├─ ARGUMENTOS:")
            self.indent_level += 1
            for i, arg in enumerate(node.args):
                if i == len(node.args) - 1:
                    self._add_line("└─ ARG:")
                else:
                    self._add_line("├─ ARG:")
                
                self.indent_level += 1
                self._visit(arg, show_details)
                self.indent_level -= 1
            self.indent_level -= 1
        
        self.indent_level -= 1
    
    def _visit_array_access(self, node, show_details):
        """Visita un acceso a array"""
        self._add_line("├─ ARRAY_ACCESS[]")
        self.indent_level += 1
        
        self._add_line("├─ ARRAY:")
        self.indent_level += 1
        self._visit(node.array, show_details)
        self.indent_level -= 1
        
        self._add_line("├─ ÍNDICE:")
        self.indent_level += 1
        self._visit(node.index, show_details)
        self.indent_level -= 1
        
        self.indent_level -= 1


class ASTStatistics:
    """Calcula estadísticas del AST"""
    
    def __init__(self):
        self.node_count = 0
        self.node_types = {}
        self.depth = 0
        self.max_depth = 0
    
    def analyze(self, node):
        """Analiza el AST"""
        self.node_count = 0
        self.node_types = {}
        self.depth = 0
        self.max_depth = 0
        self._count_nodes(node)
        return self
    
    def _count_nodes(self, node):
        """Cuenta nodos recursivamente"""
        if node is None:
            return
        
        self.depth += 1
        self.max_depth = max(self.max_depth, self.depth)
        
        node_type = type(node).__name__
        self.node_types[node_type] = self.node_types.get(node_type, 0) + 1
        self.node_count += 1
        
        # Contar nodos secundarios
        if isinstance(node, Program):
            for decl in node.declarations:
                self._count_nodes(decl)
        elif isinstance(node, FunctionDecl):
            for param in node.params:
                self._count_nodes(param)
            self._count_nodes(node.body)
        elif isinstance(node, VarDecl):
            self._count_nodes(node.init_value)
        elif isinstance(node, CompoundStatement):
            for stmt in node.statements:
                self._count_nodes(stmt)
        elif isinstance(node, IfStatement):
            self._count_nodes(node.condition)
            self._count_nodes(node.then_stmt)
            self._count_nodes(node.else_stmt)
        elif isinstance(node, WhileStatement):
            self._count_nodes(node.condition)
            self._count_nodes(node.body)
        elif isinstance(node, ForStatement):
            self._count_nodes(node.init)
            self._count_nodes(node.condition)
            self._count_nodes(node.increment)
            self._count_nodes(node.body)
        elif isinstance(node, ReturnStatement):
            self._count_nodes(node.expr)
        elif isinstance(node, ExpressionStatement):
            self._count_nodes(node.expr)
        elif isinstance(node, BinaryOp):
            self._count_nodes(node.left)
            self._count_nodes(node.right)
        elif isinstance(node, UnaryOp):
            self._count_nodes(node.operand)
        elif isinstance(node, Assignment):
            self._count_nodes(node.target)
            self._count_nodes(node.value)
        elif isinstance(node, FunctionCall):
            for arg in node.args:
                self._count_nodes(arg)
        elif isinstance(node, ArrayAccess):
            self._count_nodes(node.array)
            self._count_nodes(node.index)
        
        self.depth -= 1
    
    def get_report(self):
        """Retorna un reporte de estadísticas"""
        report = []
        report.append("\n" + "="*60)
        report.append("ESTADÍSTICAS DEL AST")
        report.append("="*60)
        report.append(f"Total de nodos: {self.node_count}")
        report.append(f"Profundidad máxima: {self.max_depth}")
        report.append(f"\nTipos de nodos:")
        
        for node_type in sorted(self.node_types.keys()):
            count = self.node_types[node_type]
            report.append(f"  {node_type}: {count}")
        
        report.append("="*60)
        
        return '\n'.join(report)
