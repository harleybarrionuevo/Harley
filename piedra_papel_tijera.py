import random
from typing import Dict, List, Optional, Tuple

# ------------------------------------
# estructuras de datos principales
# ------------------------------------

# opciones posibles (tupla inmutable)
OPCIONES: Tuple[str, ...] = ('piedra', 'papel', 'tijera')

# reglas de victoria: la clave vence al valor (diccionario)
REGLAS_GANADOR: Dict[str, str] = {
    'piedra': 'tijera',
    'papel': 'piedra',
    'tijera': 'papel',
}

# códigos ANSI para dar color a la salida (funcionan en PowerShell moderno)
COLOR_RESET = '\033[0m'
COLOR_VERDE = '\033[32m'
COLOR_ROJO = '\033[31m'
COLOR_AMARILLO = '\033[33m'
COLOR_AZUL = '\033[34m'
COLOR_MAGENTA = '\033[35m'


# ------------------------------------
# utilidades de presentación
# ------------------------------------
def bienvenida() -> None:
    """Muestra un mensaje de bienvenida."""
    print(COLOR_AZUL + "=" * 50 + COLOR_RESET)
    print(COLOR_AZUL + "¡Bienvenido al Juego de Piedra, Papel o Tijera!" + COLOR_RESET)
    print(COLOR_AZUL + "=" * 50 + COLOR_RESET + "\n")


def mostrar_menu() -> None:
    """Imprime el menú de opciones numeradas."""
    print("Elige una opción:")
    for idx, nombre in enumerate(OPCIONES, start=1):
        print(f"  {idx}. {nombre.capitalize()}")
    print("  4. Salir")
    print()


def obtener_eleccion_usuario() -> Optional[str]:
    """Solicita y valida una entrada del usuario.

    Retorna el nombre de la opción seleccionada o `None` si decide salir.
    """
    while True:
        opcion = input("Tu opción (1-4): ").strip()
        if opcion == '4':
            return None
        if opcion in ('1', '2', '3'):
            return OPCIONES[int(opcion) - 1]
        print(COLOR_ROJO + "Opción inválida. Intenta de nuevo." + COLOR_RESET)


def obtener_eleccion_computadora() -> str:
    """Elige un movimiento aleatorio para la computadora."""
    return random.choice(OPCIONES)


def determinar_ganador(usuario: str, computadora: str) -> Tuple[str, str]:
    """Devuelve (resultado, mensaje) según las reglas.

    `resultado` es 'empate', 'usuario' o 'computadora'.
    """
    if usuario == computadora:
        return 'empate', 'Empate'
    if REGLAS_GANADOR[usuario] == computadora:
        return 'usuario', '¡Ganaste esta ronda!'
    return 'computadora', 'Perdiste esta ronda'


def determinar_ganador_final(scores: Dict[str, int]) -> str:
    """Determina quién ganó el juego basado en la puntuación final.
    
    Retorna 'usuario', 'computadora' o 'empate'.
    """
    if scores['usuario'] > scores['computadora']:
        return 'usuario'
    elif scores['computadora'] > scores['usuario']:
        return 'computadora'
    else:
        return 'empate'


def mostrar_ganador_final(scores: Dict[str, int]) -> None:
    """Muestra el ganador del juego."""
    ganador = determinar_ganador_final(scores)
    
    print("\n" + COLOR_MAGENTA + "=" * 50 + COLOR_RESET)
    print(COLOR_MAGENTA + "¡FIN DE LAS 5 RONDAS!" + COLOR_RESET)
    print(COLOR_MAGENTA + "=" * 50 + COLOR_RESET)
    
    if ganador == 'usuario':
        print(COLOR_VERDE + f"\n🎉 ¡FELICIDADES, GANASTE EL JUEGO! 🎉" + COLOR_RESET)
        print(f"Puntuación Final: Tú {scores['usuario']} - Computadora {scores['computadora']}\n")
    elif ganador == 'computadora':
        print(COLOR_ROJO + f"\n😢 La computadora ganó el juego" + COLOR_RESET)
        print(f"Puntuación Final: Tú {scores['usuario']} - Computadora {scores['computadora']}\n")
    else:
        print(COLOR_AMARILLO + f"\n⚖️  ¡EMPATE!" + COLOR_RESET)
        print(f"Puntuación Final: Tú {scores['usuario']} - Computadora {scores['computadora']}\n")


def imprimir_puntuacion(scores: Dict[str, int]) -> None:
    """Muestra la puntuación actual usando un diccionario.

    keys: 'usuario' y 'computadora'.
    """
    print(f"\nPuntuación - Tú: {scores['usuario']}  |  Computadora: {scores['computadora']}\n")


def agregar_historial(hist: List[Dict[str, str]], usuario: str, computadora: str, resultado: str) -> None:
    """Registra una ronda en la lista `hist`."""
    hist.append({'usuario': usuario, 'computadora': computadora, 'resultado': resultado})


def mostrar_historial(hist: List[Dict[str, str]]) -> None:
    """Imprime todas las rondas jugadas hasta el momento."""
    if not hist:
        print("No se ha jugado ninguna ronda aún.")
        return
    print("\nHistorial de rondas:")
    for idx, entrada in enumerate(hist, start=1):
        u = entrada['usuario'].capitalize()
        c = entrada['computadora'].capitalize()
        r = entrada['resultado']
        print(f"  {idx}. {u} vs {c} -> {r}")




def juego_piedra_papel_tijera() -> None:
    """Ciclo principal que orquesta el juego completo de 5 rondas."""
    bienvenida()
    
    while True:
        scores: Dict[str, int] = {'usuario': 0, 'computadora': 0}
        historial: List[Dict[str, str]] = []
        
        # Juego de 5 rondas exactas
        for ronda in range(1, 6):
            print(f"\n{'=' * 50}")
            print(f"RONDA {ronda} de 5")
            print(f"{'=' * 50}")
            
            imprimir_puntuacion(scores)
            mostrar_menu()

            eleccion_usuario = obtener_eleccion_usuario()
            if eleccion_usuario is None:
                print(COLOR_ROJO + "\nJuego cancelado. Volviendo al menú..." + COLOR_RESET)
                return

            eleccion_computadora = obtener_eleccion_computadora()

            print(f"\n🎮 Tú elegiste: {COLOR_VERDE}{eleccion_usuario.upper()}{COLOR_RESET}")
            print(f"💻 Computadora eligió: {COLOR_ROJO}{eleccion_computadora.upper()}{COLOR_RESET}")

            resultado, mensaje = determinar_ganador(eleccion_usuario, eleccion_computadora)
            print(COLOR_AMARILLO + mensaje + COLOR_RESET)

            if resultado == 'usuario':
                scores['usuario'] += 1
            elif resultado == 'computadora':
                scores['computadora'] += 1

            agregar_historial(historial, eleccion_usuario, eleccion_computadora, resultado)
        
        # Mostrar resultado final
        mostrar_ganador_final(scores)
        mostrar_historial(historial)
        
        # Preguntar si quiere jugar de nuevo
        print("¿Quieres jugar otra vez?")
        print("  1. Sí")
        print("  2. No")
        
        while True:
            opcion = input("\nTu opción (1-2): ").strip()
            if opcion == '1':
                break
            elif opcion == '2':
                print(COLOR_VERDE + "\n¡Gracias por jugar! Hasta pronto." + COLOR_RESET)
                return
            else:
                print(COLOR_ROJO + "Opción inválida. Intenta de nuevo." + COLOR_RESET)


def main() -> None:
    juego_piedra_papel_tijera()


if __name__ == "__main__":
    main()
