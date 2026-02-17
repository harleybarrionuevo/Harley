"""
Juego de Piedra, Papel o Tijera
Un juego clásico entre el usuario y la computadora
"""

import random
from typing import Tuple

class JuegoPPT:
    """Gestiona el juego de Piedra, Papel o Tijera"""
    
    OPCIONES = ['piedra', 'papel', 'tijera']
    REGLAS = {
        'piedra': 'tijera',
        'papel': 'piedra',
        'tijera': 'papel'
    }
    
    def __init__(self):
        self.puntos_usuario = 0
        self.puntos_computadora = 0
        self.rondas = 0
    
    def obtener_entrada(self) -> str:
        """Obtiene y valida la entrada del usuario"""
        while True:
            try:
                opcion = input("\nTu opción (1-4): ").strip()
                if opcion in ['1', '2', '3', '4']:
                    return opcion
                print("❌ Ingresa un número entre 1 y 4")
            except KeyboardInterrupt:
                return '4'
    
    def determinar_ganador(self, usuario: str, computadora: str) -> Tuple[str, int]:
        """Determina el ganador de una ronda. Retorna (resultado, puntos_usuario)"""
        if usuario == computadora:
            return "Empate 🤝", 0
        elif self.REGLAS[usuario] == computadora:
            return "¡Ganaste! ✅", 1
        else:
            return "Perdiste ❌", 0
    
    def mostrar_interfaz(self):
        """Muestra el menú del juego"""
        print(f"\n{'='*50}")
        print("🎮 PIEDRA, PAPEL O TIJERA")
        print(f"{'='*50}")
        print(f"Puntuación - Tú: {self.puntos_usuario} | Computadora: {self.puntos_computadora}")
        print(f"Rondas jugadas: {self.rondas}")
        print("\nOpciones:")
        print("1. 🪨 Piedra")
        print("2. 📄 Papel")
        print("3. ✂️  Tijera")
        print("4. 🚪 Salir")
    
    def jugar_ronda(self):
        """Juega una ronda del juego"""
        self.mostrar_interfaz()
        opcion = self.obtener_entrada()
        
        if opcion == '4':
            return False
        
        eleccion_usuario = self.OPCIONES[int(opcion) - 1]
        eleccion_computadora = random.choice(self.OPCIONES)
        
        print(f"\n🎮 Elegiste: {eleccion_usuario.upper()}")
        print(f"💻 Computadora eligió: {eleccion_computadora.upper()}")
        
        resultado, puntos = self.determinar_ganador(eleccion_usuario, eleccion_computadora)
        print(f"\n{resultado}")
        
        self.puntos_usuario += puntos
        self.puntos_computadora += 1 - puntos if puntos == 0 and resultado != "Empate 🤝" else 0
        self.rondas += 1
        
        return True
    
    def mostrar_resultado_final(self):
        """Muestra el resultado final del juego"""
        print(f"\n{'='*50}")
        print("🏁 RESULTADO FINAL")
        print(f"{'='*50}")
        print(f"Rondas jugadas: {self.rondas}")
        print(f"Tu puntuación: {self.puntos_usuario}")
        print(f"Puntuación computadora: {self.puntos_computadora}")
        
        if self.puntos_usuario > self.puntos_computadora:
            print("\n🎉 ¡GANASTE EL JUEGO!")
        elif self.puntos_usuario < self.puntos_computadora:
            print("\n😔 Perdiste el juego")
        else:
            print("\n🤝 ¡Es un empate!")
        print(f"{'='*50}\n")
    
    def iniciar(self):
        """Inicia el bucle principal del juego"""
        print("\n¡Bienvenido a Piedra, Papel o Tijera!")
        
        while self.jugar_ronda():
            pass
        
        self.mostrar_resultado_final()

def main():
    """Función principal"""
    juego = JuegoPPT()
    juego.iniciar()

if __name__ == "__main__":
    main()
