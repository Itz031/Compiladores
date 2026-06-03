"""
Script para exportar AST a archivo HTML para visualización en navegador
"""

import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Proyecto', 'AnalizLexico'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Proyecto', 'AnalizSintactico'))

from lexer import Lexer
from parser import Parser
from ast_nodes import *


class ASTHTMLExporter:
    """Exporta el AST a HTML con estilo"""
    
    def __init__(self):
        self.node_count = 0
    
    def export(self, ast, codigo_c, filename='ast_visualization.html'):
        """Exporta el AST a un archivo HTML"""
        html = self._generate_html(ast, codigo_c)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return filename
    
    def _generate_html(self, ast, codigo_c):
        """Genera el contenido HTML"""
        html_parts = []
        
        # Header
        html_parts.append(self._get_header())
        
        # Título
        html_parts.append(f"""
        <div class="container">
            <h1>🌳 Árbol de Sintaxis Abstracta (AST)</h1>
            <p class="timestamp">Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            
            <div class="code-section">
                <h2>Código C Original</h2>
                <pre class="code">{self._escape_html(codigo_c)}</pre>
            </div>
            
            <div class="ast-section">
                <h2>Árbol de Sintaxis</h2>
                <div class="tree">
        """)
        
        # AST
        html_parts.append(self._node_to_html(ast))
        
        # Footer
        html_parts.append("""
                </div>
            </div>
        </div>
        """)
        
        html_parts.append(self._get_footer())
        
        return ''.join(html_parts)
    
    def _get_header(self):
        """Retorna el header HTML"""
        return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualizador de AST - Compilador C</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            padding: 40px;
        }
        
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        
        h2 {
            color: #555;
            margin-top: 30px;
            margin-bottom: 15px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }
        
        .timestamp {
            text-align: center;
            color: #999;
            font-size: 0.9em;
            margin-bottom: 30px;
        }
        
        .code-section {
            background: #f5f5f5;
            border-left: 4px solid #667eea;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
        }
        
        .code {
            background: #282c34;
            color: #abb2bf;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.5;
        }
        
        .ast-section {
            margin-top: 30px;
        }
        
        .tree {
            background: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
            font-family: 'Courier New', monospace;
            line-height: 1.8;
            font-size: 13px;
        }
        
        .node {
            margin-left: 15px;
        }
        
        .node-keyword {
            color: #d73a49;
            font-weight: bold;
        }
        
        .node-type {
            color: #6f42c1;
            font-weight: bold;
        }
        
        .node-value {
            color: #22863a;
        }
        
        .node-operator {
            color: #e36209;
        }
        
        .branch {
            color: #666;
        }
    </style>
</head>
<body>
"""
    
    def _get_footer(self):
        """Retorna el footer HTML"""
        return """
</body>
</html>
"""
    
    def _node_to_html(self, node, depth=0):
        """Convierte un nodo a HTML"""
        if node is None:
            return ""
        
        indent = "▌ " * depth
        html = ""
        
        if isinstance(node, Program):
            html += f'<div class="node"><span class="branch">📦 PROGRAMA</span>\n'
            for decl in node.declarations:
                html += self._node_to_html(decl, depth + 1)
            html += '</div>\n'
        
        elif isinstance(node, FunctionDecl):
            html += f'<div class="node">{indent}<span class="node-keyword">ƒ FUNCIÓN</span> '
            html += f'<span class="node-value">{node.name}</span> () → '
            html += f'<span class="node-type">{node.return_type}</span>\n'
            if node.params:
                html += f'<div class="node">{indent}  <span class="branch">Parámetros:</span>\n'
                for param in node.params:
                    html += f'<div class="node">{indent}    <span class="node-type">{param.param_type}</span> '
                    html += f'<span class="node-value">{param.name}</span>\n</div>'
                html += '</div>\n'
            html += f'<div class="node">{indent}  <span class="branch">Cuerpo:</span>\n'
            html += self._node_to_html(node.body, depth + 2)
            html += '</div></div>\n'
        
        elif isinstance(node, VarDecl):
            html += f'<div class="node">{indent}<span class="node-keyword">var</span> '
            html += f'<span class="node-type">{node.var_type}</span> '
            html += f'<span class="node-value">{node.name}</span>'
            if node.init_value:
                html += f' <span class="node-operator">=</span>\n'
                html += self._node_to_html(node.init_value, depth + 1)
                html += '</div>\n'
            else:
                html += '</div>\n'
        
        elif isinstance(node, CompoundStatement):
            html += f'<div class="node">{indent}<span class="branch">{{ BLOQUE }}</span>\n'
            for stmt in node.statements:
                html += self._node_to_html(stmt, depth + 1)
            html += '</div>\n'
        
        elif isinstance(node, IfStatement):
            html += f'<div class="node">{indent}<span class="node-keyword">if</span>\n'
            html += f'<div class="node">{indent}  <span class="branch">Condición:</span>\n'
            html += self._node_to_html(node.condition, depth + 2)
            html += f'<div class="node">{indent}  <span class="branch">Entonces:</span>\n'
            html += self._node_to_html(node.then_stmt, depth + 2)
            if node.else_stmt:
                html += f'<div class="node">{indent}  <span class="branch">Sino:</span>\n'
                html += self._node_to_html(node.else_stmt, depth + 2)
            html += '</div></div></div>\n'
        
        elif isinstance(node, ForStatement):
            html += f'<div class="node">{indent}<span class="node-keyword">for</span>\n'
            if node.init:
                html += f'<div class="node">{indent}  <span class="branch">Init:</span>\n'
                html += self._node_to_html(node.init, depth + 2)
            if node.condition:
                html += f'<div class="node">{indent}  <span class="branch">Condition:</span>\n'
                html += self._node_to_html(node.condition, depth + 2)
            if node.increment:
                html += f'<div class="node">{indent}  <span class="branch">Increment:</span>\n'
                html += self._node_to_html(node.increment, depth + 2)
            html += f'<div class="node">{indent}  <span class="branch">Body:</span>\n'
            html += self._node_to_html(node.body, depth + 2)
            html += '</div></div>\n'
        
        elif isinstance(node, WhileStatement):
            html += f'<div class="node">{indent}<span class="node-keyword">while</span>\n'
            html += f'<div class="node">{indent}  <span class="branch">Condition:</span>\n'
            html += self._node_to_html(node.condition, depth + 2)
            html += f'<div class="node">{indent}  <span class="branch">Body:</span>\n'
            html += self._node_to_html(node.body, depth + 2)
            html += '</div></div></div>\n'
        
        elif isinstance(node, ReturnStatement):
            html += f'<div class="node">{indent}<span class="node-keyword">return</span>'
            if node.expr:
                html += '\n'
                html += self._node_to_html(node.expr, depth + 1)
            html += '</div>\n'
        
        elif isinstance(node, BinaryOp):
            html += f'<div class="node">{indent}<span class="node-operator">{node.op}</span>\n'
            html += f'<div class="node">{indent}  L:\n'
            html += self._node_to_html(node.left, depth + 2)
            html += f'<div class="node">{indent}  R:\n'
            html += self._node_to_html(node.right, depth + 2)
            html += '</div></div></div>\n'
        
        elif isinstance(node, FunctionCall):
            html += f'<div class="node">{indent}<span class="node-value">➜ {node.name}</span>('
            for arg in node.args:
                html += '\n'
                html += self._node_to_html(arg, depth + 1)
            html += ')</div>\n'
        
        elif isinstance(node, Identifier):
            html += f'<div class="node">{indent}<span class="node-value">id: {node.name}</span></div>\n'
        
        elif isinstance(node, IntLiteral):
            html += f'<div class="node">{indent}<span class="node-value">int: {node.value}</span></div>\n'
        
        elif isinstance(node, FloatLiteral):
            html += f'<div class="node">{indent}<span class="node-value">float: {node.value}</span></div>\n'
        
        elif isinstance(node, ExpressionStatement):
            html += f'<div class="node">{indent}<span class="branch">expr:</span>\n'
            html += self._node_to_html(node.expr, depth + 1)
            html += '</div>\n'
        
        return html
    
    def _escape_html(self, text):
        """Escapa caracteres HTML"""
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))


def main():
    print("\n" + "="*80)
    print("EXPORTADOR DE AST A HTML")
    print("="*80 + "\n")
    
    codigo = """
int doble(int x) {
    return x * 2;
}

int main() {
    int valor = 5;
    int resultado = doble(valor);
    
    if (resultado > 10) {
        resultado = resultado + 5;
    }
    
    return resultado;
}
"""
    
    try:
        # Análisis
        lexer = Lexer(codigo)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Exportar
        exporter = ASTHTMLExporter()
        filename = exporter.export(ast, codigo, 'ast_visualization.html')
        
        print(f"[✓] Archivo generado: {filename}")
        print(f"[✓] Abre el archivo en tu navegador para ver la visualización\n")
        
    except Exception as e:
        print(f"[✗] Error: {e}\n")
        sys.exit(1)


if __name__ == '__main__':
    main()
