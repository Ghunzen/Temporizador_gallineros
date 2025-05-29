def calcular_tiempo_recoleccion(jaulas_restantes: int, frecuencia_hz: int = 50, segundos_base_por_jaula: int = 17) -> str:
    """
    Calcula el tiempo estimado restante para la recolección de huevos basándose en el conteo de jaulas y la frecuencia de la máquina.

    Args:
        jaulas_restantes (int): El número de jaulas pendientes de vaciar.
        frecuencia_hz (int): La frecuencia de operación de la máquina en Hertz (valor predeterminado: 50 Hz).
        segundos_base_por_jaula (int): El tiempo base por jaula a una frecuencia de 50 Hz (valor predeterminado: 17 segundos).

    Returns:
        str: El tiempo estimado en formato HH:MM:SS. Retorna un mensaje de error si la entrada es inválida.
    """
    if not isinstance(jaulas_restantes, int) or jaulas_restantes < 0:
        return "Cantidad de jaulas inválida. Debe ser un número entero no negativo."
    if not isinstance(frecuencia_hz, int) or frecuencia_hz <= 0:
        return "Frecuencia inválida. Debe ser un número entero positivo."
    if not isinstance(segundos_base_por_jaula, (int, float)) or segundos_base_por_jaula <= 0:
        return "Segundos base por jaula inválidos. Debe ser un número positivo."

    # Ajusta los segundos por jaula basándose en la frecuencia de operación real respecto a la frecuencia base (50 Hz).
    # Si la frecuencia es, por ejemplo, 25 Hz (la mitad de 50), el factor será 50/25 = 2, duplicando el tiempo por jaula.
    # Si la frecuencia es 100 Hz (el doble de 50), el factor será 50/100 = 0.5, reduciendo el tiempo a la mitad.
    factor_ajuste_frecuencia = 50 / frecuencia_hz
    segundos_por_jaula_ajustado = segundos_base_por_jaula * factor_ajuste_frecuencia

    tiempo_total_segundos = jaulas_restantes * segundos_por_jaula_ajustado

    horas = int(tiempo_total_segundos // 3600)
    minutos = int((tiempo_total_segundos % 3600) // 60)
    segundos = int(tiempo_total_segundos % 60)

    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

def ejecutar_temporizador_gallineros():
    """
    Ejecuta la aplicación de temporizador para la recolección de huevos,
    solicitando la entrada del usuario y mostrando los tiempos calculados.
    """
    print("--- Temporizador de Recolección de Huevos en Gallineros ---")

    while True:
        entrada_usuario = input("Ingrese jaulas restantes (ej: '150'), 'largo'/'corto' para galpones estándar, o 'salir': ").strip().lower()

        if entrada_usuario == 'salir':
            print("Saliendo de la aplicación. ¡Hasta pronto!")
            break

        jaulas = 0
        descripcion = ""

        if entrada_usuario == 'largo':
            jaulas = 181  # Estándar para galpones largos (Nº 1, 2, 3, 4)
            descripcion = "Galpón Largo (181 jaulas)"
        elif entrada_usuario == 'corto':
            jaulas = 131  # Estándar para galpones cortos (Nº 5, 6, 7, 8, 9, 10)
            descripcion = "Galpón Corto (131 jaulas)"
        else:
            try:
                jaulas = int(entrada_usuario)
                descripcion = f"{jaulas} Jaulas"
                if jaulas < 0:
                    print(calcular_tiempo_recoleccion(jaulas))  # Maneja el error de entrada negativa
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número, 'largo', 'corto' o 'salir'.")
                continue

        entrada_frecuencia = input(f"Ingrese la frecuencia de la máquina en Hz (ej: '25', '50', '60', '100') [Predeterminado: 50]: ").strip()
        frecuencia_hz = 50  # Valor predeterminado

        if entrada_frecuencia:
            try:
                frecuencia_hz = int(entrada_frecuencia)
                if frecuencia_hz <= 0:
                    print("La frecuencia debe ser un número entero positivo. Se usará 50 Hz por defecto.")
                    frecuencia_hz = 50
            except ValueError:
                print("Entrada de frecuencia inválida. Se usará 50 Hz por defecto.")

        tiempo_estimado = calcular_tiempo_recoleccion(jaulas, frecuencia_hz)
        print(f"Tiempo estimado para {descripcion} a {frecuencia_hz} Hz: {tiempo_estimado}\n")

# Punto de entrada principal para la ejecución de la aplicación
if __name__ == "__main__":
    ejecutar_temporizador_gallineros()
