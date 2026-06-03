"""
Visor interactivo de AST para el compilador
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Proyecto', 'AnalizLexico'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Proyecto', 'AnalizSintactico'))

from lexer import Lexer
from parser import Parser
from ast_visualizer import ASTVisualizer, ASTStatistics


class ASTInteractiveViewer:
    """Visor interactivo de AST"""
    
    def __init__(self):
        self.ejemplos = {
            '1': self._get_ejemplo_basico(),
            '2': self._get_ejemplo_if(),
            '3': self._get_ejemplo_ciclo(),
            '4': self._get_ejemplo_completo(),
        }
    
    def _get_ejemplo_basico(self):
        return """
int main() {
    int x = 5;
    int y = 10;
    int suma = x + y;
    return suma;
}
"""
    
    def _get_ejemplo_if(self):
        return """
int main() {
    int x = 15;
    
    if (x > 10) {
        x = x + 5;
    } else {
        x = x - 5;
    }
    
    return x;
}
"""
    
    def _get_ejemplo_ciclo(self):
        return """
int main() {
    int suma = 0;
    
    for (int i = 0; i < 5; i++) {
        suma = suma + i;
    }
    
    while (suma < 20) {
        suma = suma + 1;
    }
    
    return suma;
}
"""
    
    def _get_ejemplo_completo(self):
        return """
int suma(int a, int b) {
    return a + b;
}

int main() {
    int x = 5;
    int y = 10;
    int resultado = suma(x, y);
    
    if (resultado > 10) {
        resultado = resultado * 2;
    }
    
    return resultado;
}
"""
    
    def show_menu(self):
        """Muestra el menú principal"""
        print("\n" + "╔" + "="*78 + "╗")
        print("║" + "VISOR INTERACTIVO DE ÁRBOL DE SINTAXIS ABSTRACTA".center(78) + "║")
        print("╚" + "="*78 + "╝\n")
        
        print("Selecciona un ejemplo para visualizar:\n")
        print("  1. Ejemplo básico (Variables y asignación)")
        print("  2. Ejemplo if/else (Control condicional)")
        print("  3. Ejemplo for/while (Ciclos)")
        print("  4. Ejemplo completo (Funciones + todo)")
        print("  5. Escribir código personalizado")
        print("  0. Salir\n")
    
    def run(self):
        """Ejecuta el visor interactivo"""
        while True:
            self.show_menu()
            opcion = input("Elige una opción (0-5): ").strip()
            
            if opcion == '0':
                print("\n[✓] ¡Hasta luego!")
                break
            elif opcion in self.ejemplos:
                codigo = self.ejemplos[opcion]
                self._visualizar_ast(codigo, f"Ejemplo {opcion}")
            elif opcion == '5':
                print("\nEscribe el código C (termina con una línea vacía):")
                lineas = []
                while True:
                    linea = input()
                    if not linea:
                        break
                    lineas.append(linea)
                codigo = '\n'.join(lineas)
                self._visualizar_ast(codigo, "Código personalizado")
            else:
                print("\n[✗] Opción inválida")
                input("Presiona ENTER para continuar...")
    
    def _visualizar_ast(self, codigo, titulo):
        """Visualiza el AST para el código dado"""
        print("\n" + "─"*80)
        print(titulo.center(80))
        print("─"*80 + "\n")
        
        try:
            # Lexer
            print("[1/3] Análisis Léxico...")
            lexer = Lexer(codigo)
            tokens = lexer.tokenize()
            print(f"      ✓ {len(tokens)} tokens generados")
            
            # Parser
            print("[2/3] Análisis Sintáctico...")
            parser = Parser(tokens)
            ast = parser.parse()
            print(f"      ✓ AST generado")
            
            # Visualización
            print("[3/3] Generando visualización...\n")
            
            visualizer = ASTVisualizer()
            ast_visual = visualizer.visualize(ast)
            print(ast_visual)
            
            # Estadísticas
            stats = ASTStatistics()
            stats.analyze(ast)
            print(stats.get_report())
            
            input("\nPresiona ENTER para continuar...")
            
        except SyntaxError as e:
            print(f"\n[✗] Error de sintaxis: {e}\n")
            input("Presiona ENTER para continuar...")
        except Exception as e:
            print(f"\n[✗] Error: {e}\n")
            input("Presiona ENTER para continuar...")


def main():
    viewer = ASTInteractiveViewer()
    try:
        viewer.run()
    except KeyboardInterrupt:
        print("\n\n[!] Programa interrumpido")
        sys.exit(0)


if __name__ == '__main__':
    main()
