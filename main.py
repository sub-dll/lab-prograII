from insertar import insertar_sala, registrar_reserva
from consultar import consultar_salas, consultar_reservas
from eliminar import cancelar_reserva

def menu():
    while True:
        print("\n--- Sistema de Reservas ---")
        print("1. Registrar sala")
        print("2. Consultar salas")
        print("3. Registrar reserva")
        print("4. Consultar reservas")
        print("5. Cancelar reserva")
        print("0. Salir")
        
        try:
            opcion = int(input("Seleccione una opciin: "))
        except ValueError:
            print("Error: Por favor, ingrese un número vido.")
            continue

        if opcion == 1:
            nombre = input("Nombre de la sala: ")
            try:
                capacidad = int(input("Capacidad: "))
                insertar_sala(nombre, capacidad)
            except ValueError:
                print("Error: La capacidad debe ser un numero.")
        elif opcion == 2:
            consultar_salas()
        elif opcion == 3:
            est = input("Nombre del estudiante: ")
            try:
                s_id = int(input("ID de la sala: "))
                fec = input("Fecha (AAAA-MM-DD): ")
                registrar_reserva(est, s_id, fec)
            except ValueError:
                print("Error: El ID de la sala debe ser un numero.")
        elif opcion == 4:
            consultar_reservas()
        elif opcion == 5:
            try:
                id_res = int(input("ID de la reserva a cancelar: "))
                cancelar_reserva(id_res)
            except ValueError:
                print("Error: El ID debe ser un numero.")
        elif opcion == 0:
            print("Saliendo")
            break
        else:
            print("Reintente.")

if __name__ == "__main__":
    menu()