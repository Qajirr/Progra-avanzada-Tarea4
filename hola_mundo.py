"""
hola_mundo.py

Una aplicación simple de "Hola, Mundo!" siguiendo la guía de estilo PEP 8.
"""
import random

def print_hello_world() -> None:
    """Función para imprimir 'Hola, Mundo!'."""
    print("Hola, Mundo!")

def play_russian_roulette() -> None:
    """Función para jugar a la ruleta rusa."""
    chamber = [0, 0, 0, 0, 0, 1]  # Solo una bala en el tambor de 6
    random.shuffle(chamber)
    
    if chamber[0] == 1:
        print("¡Bang! Has perdido.")
    else:
        print("Clic. Has sobrevivido.")

def play_rock_paper_scissors() -> None:
    """Función para jugar cachipun."""
    options = ['piedra', 'papel', 'tijera']
    print("Cachipun.")
    user_input_str = input("Elige piedra (0), papel (1) o tijeras (2): ")
    if user_input_str not in ('0', '1', '2'):
        print("Opción no válida, por favor escoge una de las tres posibles.")
        return
    user_input = int(user_input_str)
    pc_input = random.randint(0, 2)
    if pc_input == user_input:
        print(f"Empate! Ambos sacan {options[user_input]}")
    elif user_input == 0:
        if pc_input == 1:
            print(f"El pc saca {options[pc_input]}, el pc gana!")
        else:
            print(f"El pc saca {options[pc_input]}, tú ganas!")
    elif user_input == 1:
        if pc_input == 2:
            print(f"El pc saca {options[pc_input]}, el pc gana!")
        else:
            print(f"El pc saca {options[pc_input]}, tú ganas!")
    elif user_input == 2:
        if pc_input == 0:
            print(f"El pc saca {options[pc_input]}, el pc gana!")
        else:
            print(f"El pc saca {options[pc_input]}, tú ganas!")

def main():
    """Función principal para seleccionar y ejecutar funcionalidades."""
    while True:
        print("\nSeleccione una funcionalidad:")
        print("1. Imprimir 'Hola, Mundo!'")
        print("2. Jugar a la ruleta rusa")
        print("3. Jugar Cachipun")
        print("4. Salir")

        choice = input("Ingrese el número de su elección: ")

        if choice == "1":
            print_hello_world()
        elif choice == "2":
            play_russian_roulette()
        elif choice == "3":
            play_rock_paper_scissors()
        elif choice == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Elección inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

