from db.habitaciones_db import HabitacionesInDB
from db.habitaciones_db import get_habitacion,update_habitacion,delete_habitacion,save_habitacion

from models.habitaciones_models import HabitacionInf,HabitacionReserva

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()


@api.get("/info/habitacion/consulta")#llamado habitacion info
async def get_habi_info(id: int):

    habi_in_db = get_habitacion(id)#validacion de existencia
    if habi_in_db == None:
        raise HTTPException(status_code=404, detail="la habitacion no existe")

    habi_inf = HabitacionInf(**habi_in_db)#si existe muestre la  info de la habitacion
    return habi_inf#retorne la habitacion info

@api.get("/info/habitacion/llamado")#llamado habitacion reserva
async def get_habi_func(id: int):

    habi_in_db = get_habitacion(id)#validacion de existencia
    if habi_in_db == None:
        raise HTTPException(status_code=404, detail="la habitacion no existe")

    habi_fun = HabitacionReserva(**habi_in_db)#si existe muestre la  reserva de la habitacion
    return habi_fun#retorne la habitacion reserva

@api.put("/ingreso/habitacion")#actualizacion base de datos
async def make_habi(habitacion : HabitacionInf):

    #validacion de existencia
    habi_in_db = get_habitacion(habitacion.id_habitacion)
    if habi_in_db == None:
        raise HTTPException(status_code=404, detail="la habitacion no existe")

    update_habitacion(habitacion.dict())
    upd_habitacion = HabitacionInf(**habitacion.dict())
    return upd_habitacion

@api.delete("/borrar/habitacion")
async def borrar_habi(id: int):

    #validacion de existencia
    habi_in_db = get_habitacion(id)
    if habi_in_db == None:
        raise HTTPException(status_code=404, detail="la habitacion no existe")

    delete_habitacion(id)
    return True

@api.post("/crear/habitacion")
async def create_habi(habitacion: HabitacionInf):
    habi_in_db = get_habitacion(habitacion.id_habitacion)
    if habi_in_db == None:
        save_habitacion(habitacion)
        new_habitacion = HabitacionInf(**habitacion.dict())
        return new_habitacion
    return None



