from sqlalchemy.orm import Session
from conexion import engine
from modelos import Sala
from modelos import Reserva

def registrar_reserva(estudiante, sala_id, fecha):
    if not estudiante.strip() or not fecha.strip():
        print("Error: Datos inválidos.")
        return

    with Session(engine) as session:
        with session.begin():
            sala = session.get(Sala, sala_id)
            
            if sala is None:
                print(f"Error: La sala con id {sala_id} no existe.")
                return
            
            if not sala.disponible:
                print(f"Error: La sala '{sala.nombre}' no esta reservable")
                return

            nueva_reserva = Reserva(estudiante=estudiante, sala_id=sala_id, fecha=fecha)
            sala.disponible = False 
            
            session.add(nueva_reserva)
            
    print(f"Reserva para '{estudiante}' registrada con éxito.")

def insertar_sala(nombre, capacidad):
    if not nombre.strip() or capacidad <= 0:
        print("Error: inserto el nombre o la capacidad de manera incorrecta")
        return
    
    with Session(engine) as session:
        with session.begin():
            nueva_sala = Sala(nombre=nombre, capacidad=capacidad)
            session.add(nueva_sala)
    print(f"Sala '{nombre}' registrada de manera correcta")