"""
Script mejorado para demostrar la compilación completa con visualización del AST
"""

import sys
import os

# Añadir rutas
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Proyecto', 'AnalizLexico'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Proyecto', 'AnalizSintactico'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Proyecto', 'GeneradorCodigo'))

from lexer import Lexer, print_tokens
from parser import Parser
from code_generator import CodeGenerator
from ast_visualizer import ASTVisualizer, ASTStatistics


def show_banner():
    """Muestra el banner del compilador"""
    print("\n" + "╔" + "="*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "COMPILADOR C -> MASM | VISUALIZACIÓN DE ÁRBOL DE SINTAXIS ABSTRACTA".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "="*78 + "╝\n")


def compile_with_ast_visualization(code, titulo=""):
    """Compila código C y visualiza el AST"""
    
    if titulo:
        print("\n╔" + "="*78 + "╗")
        print("║" + titulo.center(78) + "║")
        print("╚" + "="*78 + "╝")
    
    print("\n" + "─"*80)
    print("FASE 1: ANÁLISIS LÉXICO")
    print("─"*80)
    
    # Análisis Léxico
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    print(f"\n[✓] {len(tokens)} tokens generados\n")
    print_tokens(tokens)
    
    # Análisis Sintáctico
    print("\n" + "─"*80)
    print("FASE 2: ANÁLISIS SINTÁCTICO")
    print("─"*80 + "\n")
    
    try:
        parser = Parser(tokens)
        ast = parser.parse()
        print("[✓] Análisis sintáctico completado")
        print(f"[✓] Tabla de símbolos: {len(parser.symbol_table.scopes[0])} símbolos globales\n")
    except Exception as e:
        print(f"[✗] Error: {e}")
        return None
    
    # Visualizar AST
    print("\n" + "─"*80)
    print("ÁRBOL DE SINTAXIS ABSTRACTA (AST)")
    print("─"*80 + "\n")
    
    visualizer = ASTVisualizer()
    ast_visual = visualizer.visualize(ast, show_details=True)
    print(ast_visual)
    
    # Estadísticas
    stats = ASTStatistics()
    stats.analyze(ast)
    print(stats.get_report())
    
    # Generación de Código
    print("\n" + "─"*80)
    print("FASE 3: GENERACIÓN DE CÓDIGO MASM")
    print("─"*80 + "\n")
    
    try:
        generator = CodeGenerator()
        masm_code = generator.generate(ast)
        print(f"[✓] {len(masm_code)} líneas de MASM generadas\n")
        
        print("CÓDIGO MASM GENERADO:")
        print("─"*80)
        for i, line in enumerate(masm_code, 1):
            print(f"{i:3d}: {line}")
        print("─"*80)
    except Exception as e:
        print(f"[✗] Error: {e}")
        return None
    
    return masm_code


def main():
    show_banner()
    
    # Ejemplo 1: Suma simple
    codigo_suma = """
int main() {
    int x = 5;
    int y = 10;
    int suma = x + y;
    return suma;
}
"""
    
    compile_with_ast_visualization(codigo_suma, "EJEMPLO 1: SUMA SIMPLE")
    
    # Ejemplo 2: Control de flujo
    codigo_control = """
int main() {
    int x = 15;
    
    if (x > 10) {
        x = x + 5;
    }
    
    for (int i = 0; i < 3; i++) {
        x = x + 1;
    }
    
    return x;
}
"""
    
    input("\n\nPresiona ENTER para ver el siguiente ejemplo...")
    
    compile_with_ast_visualization(codigo_control, "EJEMPLO 2: CONTROL DE FLUJO (IF y FOR)")
    
    # Ejemplo 3: Funciones
    codigo_funcion = """
int doble(int x) {
    return x * 2;
}

int main() {
    int valor = 5;
    int resultado = doble(valor);
    return resultado;
}
"""
    
    input("\n\nPresiona ENTER para ver el siguiente ejemplo...")
    
    compile_with_ast_visualization(codigo_funcion, "EJEMPLO 3: DECLARACIÓN DE FUNCIONES")
    
    print("\n" + "="*80)
    print("[✓] DEMOSTRACIÓN COMPLETADA")
    print("="*80 + "\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Compilación interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n[✗] Error: {e}")
        sys.exit(1)
