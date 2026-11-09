from sqlalchemy.orm import Session
from conexion import engine
from modelos import Reserva

def cancelar_reserva(id_reserva):
    with Session(engine) as session:
        with session.begin():
            reserva = session.get(Reserva, id_reserva)
            
            if reserva is None:
                print(f"Error: La reserva con ID {id_reserva} no existe.")
                return
            
            sala = reserva.sala
            sala.disponible = True
            
            session.delete(reserva)
            
    print("Reserva cancelada y sala liberada correctamente.")