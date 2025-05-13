def reiniciar(resultado, _=0):
    """Reinicia la calculadora mostrando el resultado final"""
    print(f"\n🔹 Resultado final: {resultado}\n")
    return 0

def salir(resultado, _=0):
    """Termina el programa mostrando el resultado final"""
    print(f"\n🔹 Resultado final: {resultado}\n")
    exit()
    
def resto (p1,p2):
    return p1 % p2

# Diccionario de operaciones con lambdas y manejo de errores
operaciones = {
                "+": lambda p1, p2: p1 + p2,
                "-": lambda p1, p2: p1 - p2,
                "*": lambda p1, p2: p1 * p2,
                "/": lambda p1, p2: p1 / p2 if p2 != 0 else (print("❌ Error: División por cero ignorada") or p1),
                "=": reiniciar,
                "%": resto,
                "S": salir,
                "?": lambda _, __: (print("\n📝 Ayuda: Operadores disponibles: +, -, *, /, = (reiniciar), S (salir)") or 0)
            }
def obtener_numero():
    """Obtiene un número válido del usuario con manejo de errores"""
    while True:
        entrada = input("Ingrese un número (o '?' para ayuda): ").strip()
        if entrada == "?":
            operaciones["?"](0, 0)
            continue
        try:
            return float(entrada)
        except ValueError:
            print("⚠️ Entrada inválida. Intente nuevamente o ingrese '?' para ayuda")
def main():
    resultado = 0
    primera_operacion = True
    
    print("\n🧮 Calculadora Avanzada (ingrese '?' para ayuda)\n")
    
    while True:
        # Obtener operador
        operador = "+" if primera_operacion else ""
        while operador not in operaciones:
            operador = input(f"Ingrese operador {list(operaciones.keys())}: ").strip().upper()
        
        primera_operacion = False
        
        # Obtener número
        valor = obtener_numero()
        
        # Ejecutar operación
        resultado_anterior = resultado
        resultado = operaciones[operador](resultado, valor)
        
        # Mostrar resultado parcial si no es operación especial
        if operador not in ("=", "S", "?"):
            print(f"🔸 {resultado_anterior} {operador} {valor} = {resultado}")

if __name__ == "__main__":
    main()