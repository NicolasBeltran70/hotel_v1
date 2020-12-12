from typing import Dict
from pydantic import BaseModel


class HabitacionesInDB(BaseModel):
    id_habitacion: int 
    tipo_habitacion: str
    num_camas_habitacion: int
    precio_habitacion: int
    descrip_habitacion: str


db_habitaciones = [{"id_habitacion": 555,
                    "tipo_habitacion": "simple",
                    "num_camas_habitacion": 1,
                    "precio_habitacion":75000,
                    "descrip_habitacion":"habitacion sencilla"}
                    ]

cont = {"id":100}

#llamado --> GET
def get_habitacion(id : int):

    for habitacion in db_habitaciones:#for por habitacion
        print(habitacion)
        if habitacion["id_habitacion"]== id:
            return habitacion
        

#insertado --> POST
def save_habitacion(habi_in_db: HabitacionesInDB):

    db_habitaciones.append(habi_in_db.dict())
    return habi_in_db

#actualizado --> PUT

def update_habitacion(habitacion: HabitacionesInDB):

    for p_habitacion in range(len(db_habitaciones)):#for por posicion habitacion
        if db_habitaciones[p_habitacion]["id_habitacion"] == habitacion["id_habitacion"]:

            db_habitaciones[p_habitacion] = habitacion

            return habitacion
   

#borrado --> DELETE

def delete_habitacion(id: int):
    contador = 0
    pos = 1000
    for p_habitacion in range(len(db_habitaciones)):
        if db_habitaciones[p_habitacion]["id_habitacion"] == id:
            pos = contador
        else:
            contador = contador+1
    try:
        db_habitaciones.pop(pos)
        return True
    except:
        return None
    

