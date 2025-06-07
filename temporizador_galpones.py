def calcular_tiempo_recoleccion(jaulas_restantes: int, frecuencia_hz: float = 50.0, segundos_base_por_jaula: int = 17) -> str:
    """
    Calcula el tiempo estimado restante para la recolección de huevos basándose en el conteo de jaulas y la frecuencia de la máquina.

    Args:
        jaulas_restantes (int): El número de jaulas pendientes de vaciar.
        frecuencia_hz (float): La frecuencia de operación de la máquina en Hertz (valor predeterminado: 50.0 Hz). Puede ser un número decimal.
        segundos_base_por_jaula (int): El tiempo base por jaula a una frecuencia de 50 Hz (valor predeterminado: 17 segundos).

    Returns:
        str: El tiempo estimado en formato HH:MM:SS. Retorna un mensaje de error si la entrada es inválida.
    """
    if not isinstance(jaulas_restantes, int) or jaulas_restantes < 0:
        return "Cantidad de jaulas inválida. Debe ser un número entero no negativo."
    
    # MODIFICACIÓN: Se acepta int y float para la frecuencia.
    if not isinstance(frecuencia_hz, (int, float)) or frecuencia_hz <= 0:
        return "Frecuencia inválida. Debe ser un número positivo (puede tener decimales)."
        
    if not isinstance(segundos_base_por_jaula, (int, float)) or segundos_base_por_jaula <= 0:
        return "Segundos base por jaula inválidos. Debe ser un número positivo."

    # El cálculo se mantiene, ya que la división funciona perfectamente con decimales.
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
    print("--- Temporizador de Recolección de Huevos ---")

    while True:
        entrada_usuario = input("Ingrese jaulas restantes (ej: '150'), 'largo'/'corto' para galpones estándar, o 'salir': ").strip().lower()

        if entrada_usuario == 'salir':
            print("Saliendo de la aplicación. ¡Hasta pronto!")
            break

        jaulas = 0
        descripcion = ""

        if entrada_usuario == 'largo':
            jaulas = 181
            descripcion = "Galpón Largo (181 jaulas)"
        elif entrada_usuario == 'corto':
            jaulas = 131
            descripcion = "Galpón Corto (131 jaulas)"
        else:
            try:
                jaulas = int(entrada_usuario)
                descripcion = f"{jaulas} Jaulas"
                if jaulas < 0:
                    print(calcular_tiempo_recoleccion(jaulas))
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número, 'largo', 'corto' o 'salir'.")
                continue

        # MODIFICACIÓN: Se actualiza el prompt para indicar que se aceptan decimales.
        entrada_frecuencia = input(f"Ingrese la frecuencia en Hz (ej: '45,5', '50', '60') [Predeterminado: 50]: ").strip()
        frecuencia_hz = 50.0  # Usar float para el predeterminado por consistencia.

        if entrada_frecuencia:
            try:
                # MODIFICACIÓN: Reemplazar la coma por un punto y convertir a float.
                entrada_limpia = entrada_frecuencia.replace(',', '.')
                frecuencia_hz = float(entrada_limpia)
                
                if frecuencia_hz <= 0:
                    print("La frecuencia debe ser un número positivo. Se usará 50 Hz por defecto.")
                    frecuencia_hz = 50.0
            except ValueError:
                print("Entrada de frecuencia inválida. Se usará 50 Hz por defecto.")
                frecuencia_hz = 50.0

        tiempo_estimado = calcular_tiempo_recoleccion(jaulas, frecuencia_hz)
        # Se muestra la frecuencia usada para el cálculo, que ahora puede ser decimal.
        print(f"Tiempo estimado para {descripcion} a {frecuencia_hz} Hz: {tiempo_estimado}\n")

# Punto de entrada principal para la ejecución de la aplicación
if __name__ == "__main__":
    ejecutar_temporizador_gallineros()
