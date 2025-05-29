def calcular_tiempo_recoleccion(jaulas_restantes, velocidad_hz=50, segundos_base_por_jaula=17):
    """
    Calcula el tiempo restante para la recolección de huevos.

    Args:
        jaulas_restantes (int): Número de jaulas que faltan por vaciar.
        velocidad_hz (int): Frecuencia de operación en Hz (por defecto 50 Hz).
        segundos_base_por_jaula (int): Segundos que tarda cada jaula a 50 Hz (por defecto 17).

    Returns:
        str: El tiempo restante en formato hh:mm:ss.
    """
    if jaulas_restantes < 0:
        return "Cantidad de jaulas inválida. Debe ser un número positivo."

    # Si la velocidad es diferente a 50 Hz, ajustamos los segundos por jaula
    if velocidad_hz != 50:
        # Calculamos la proporción de velocidad.
        # Si es 25 Hz, es el doble de tiempo (50/25 = 2).
        # Si es 100 Hz, es la mitad de tiempo (50/100 = 0.5).
        factor_velocidad = 50 / velocidad_hz
        segundos_por_jaula_ajustado = segundos_base_por_jaula * factor_velocidad
    else:
        segundos_por_jaula_ajustado = segundos_base_por_jaula

    tiempo_total_segundos = jaulas_restantes * segundos_por_jaula_ajustado

    # Convertimos los segundos a horas, minutos y segundos
    horas = int(tiempo_total_segundos // 3600)
    minutos = int((tiempo_total_segundos % 3600) // 60)
    segundos = int(tiempo_total_segundos % 60)

    # Formateamos la salida a hh:mm:ss
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

def temporizador_gallineros():
    """
    Función principal para interactuar con el usuario y calcular el tiempo.
    """
    print("--- Calculador de Tiempo para Recolección de Huevos ---")
    print("¡Acordate que cada jaula tarda 17 segundos a 50 Hz por defecto!")

    while True:
        entrada = input("¿Cuántas jaulas faltan? (o 'largo'/'corto' para gallineros estándar, 'salir' para terminar): ").lower().strip()

        if entrada == 'salir':
            print("¡Nos vemos! ¡A seguirle dando a la envasadora!")
            break
        elif entrada == 'largo':
            jaulas = 181 # Gallineros Nº 1, 2, 3 o 4
            descripcion = "Gallinero largo (181 jaulas)"
        elif entrada == 'corto':
            jaulas = 131 # Gallineros Nº 5, 6, 7, 8, 9 o 10
            descripcion = "Gallinero corto (131 jaulas)"
        else:
            try:
                jaulas = int(entrada)
                descripcion = f"{jaulas} jaulas"
                if jaulas < 0:
                    print(calcular_tiempo_recoleccion(jaulas)) # Maneja el error de número negativo
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, ingresá un número, 'largo', 'corto' o 'salir'.")
                continue

        # Preguntar por la velocidad si es diferente a 50 Hz
        velocidad_input = input("¿A qué frecuencia está la máquina? (ej: 25, 50, 60, 100 Hz) [Por defecto: 50]: ").strip()
        velocidad_hz = 50 # Valor por defecto
        if velocidad_input:
            try:
                velocidad_hz = int(velocidad_input)
                if velocidad_hz <= 0:
                    print("La frecuencia debe ser un número positivo. Usando 50 Hz por defecto.")
                    velocidad_hz = 50
            except ValueError:
                print("Frecuencia inválida. Usando 50 Hz por defecto.")

        tiempo_restante = calcular_tiempo_recoleccion(jaulas, velocidad_hz)
        print(f"Para {descripcion} a {velocidad_hz} Hz: {tiempo_restante}\n")

# Para ejecutar el temporizador, solo tenés que llamar a la función principal:
temporizador_gallineros()
