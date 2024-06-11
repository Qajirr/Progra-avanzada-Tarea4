"""
hola_mundo.py

Una aplicación simple de "Hola, Mundo!" siguiendo la guía de estilo PEP 8.
"""
import random

def print_hello_world():
    """Función para imprimir 'Hola, Mundo!'."""
    print("Hola, Mundo!")

def play_russian_roulette():
    """Función para jugar a la ruleta rusa."""
    chamber = [0, 0, 0, 0, 0, 1]  # Solo una bala en el tambor de 6
    random.shuffle(chamber)
    
    if chamber[0] == 1:
        print("¡Bang! Has perdido.")
    else:
        print("Clic. Has sobrevivido.")

def main():
    """Función principal para seleccionar y ejecutar funcionalidades."""
    while True:
        print("\nSeleccione una funcionalidad:")
        print("1. Imprimir 'Hola, Mundo!'")
        print("2. Jugar a la ruleta rusa")
        print("3. Salir")

        choice = input("Ingrese el número de su elección: ")

        if choice == "1":
            print_hello_world()
        elif choice == "2":
            play_russian_roulette()
        elif choice == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Elección inválida. Intente de nuevo.")
if __name__ == "__main__":
    main()

