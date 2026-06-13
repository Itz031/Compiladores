# Compiladores - Proyecto de Compilador C en Python

Compilador educativo implementado en **Python** que compila código escrito en **C** a código **MASM** (Microsoft Macro Assembler).

## 📋 Descripción

Este proyecto implementa las tres fases principales de un compilador:

1. **Análisis Léxico** - Tokenización del código fuente
2. **Análisis Sintáctico** - Validación de la estructura gramatical
3. **Generación de Código** - Traducción a MASM (x86-64)

## 🗂️ Estructura del Proyecto

```
Compiladores/
├── Proyecto/
│   ├── AnalizLexico/
│   │   ├── lexer.py           # Analizador léxico
│   │   ├── tokens.py          # Definición de tipos de tokens
│   │   └── ejemplos/
│   │       └── codigo_ejemplo.c
│   │
│   ├── AnalizSintactico/
│   │   ├── parser.py          # Analizador sintáctico
│   │   ├── ast_nodes.py       # Nodos del árbol de sintaxis
│   │   └── tabla_simbolos.py  # Tabla de símbolos
│   │
│   └── GeneradorCodigo/
│       ├── code_generator.py  # Generador de código MASM
│       └── main.py            # Punto de entrada
│
├── Ensamblador/
│   ├── compilar.bat           # Script para compilar MASM
│   └── ejemplos/
│       ├── hola/
│       │   └── hola.asm
│       └── ciclo/
│           └── ciclo.asm
│
├── README.md
└── .gitignore
```

## 🚀 Uso

### Compilar un archivo C:

```bash
python Proyecto/GeneradorCodigo/main.py archivo.c
```

### Compilar el MASM generado:

```bash
Ensamblador/compilar.bat nombre_programa
```

## 📝 Flujo de Compilación

```
Código C (.c)
    ↓
[Análisis Léxico]  → Tokenización
    ↓
[Análisis Sintáctico] → Validación + AST
    ↓
[Generador de Código] → MASM (.asm)
    ↓
[MASM Compiler] → Objeto (.obj)
    ↓
[Linker] → Ejecutable (.exe)
```

## 🔧 Requisitos

- Python 3.8+
- MASM (Microsoft Macro Assembler)
- Microsoft Visual C++ Build Tools (para link.exe)

## ✨ Características

- ✅ Análisis léxico con expresiones regulares
- ✅ Parser recursivo descendente
- ✅ Detección de errores sintácticos y semánticos
- ✅ Generación de código MASM optimizado
- ✅ Tabla de símbolos con gestión de variables
- ✅ Soporte para control de flujo (if, else, for, while)

## 📚 Ejemplos

Ver carpetas `Proyecto/AnalizLexico/ejemplos/` y `Ensamblador/ejemplos/` para ejemplos de código C y MASM generado.