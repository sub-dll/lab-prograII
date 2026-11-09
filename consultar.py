from sqlalchemy import select
from sqlalchemy.orm import Session
from conexion import engine
from modelos import Sala
from modelos import Reserva

def consultar_salas():
    with Session(engine) as session:
        salas = session.scalars(select(Sala)).all()
        if not salas:
            print("no hay salas registradas")
            return
            
        print("\n--- Listado de Salas ---")
        for sala in salas:
            estado = "Disponible" if sala.disponible else "No disponible"
            print(f"ID: {sala.id} | {sala.nombre} | Cap: {sala.capacidad} | {estado}")


def consultar_reservas():
    with Session(engine) as session:
        reservas = session.scalars(select(Reserva)).all()
        
        if not reservas:
            print("No hay reservas registradas.")
            return
            
        print("\n--- Listado de Reservas ---")
        for r in reservas:
            print(f"ID: {r.id} | Estudiante: {r.estudiante} | Sala: {r.sala.nombre} | Fecha: {r.fecha}")