from nameko.rpc import rpc
import db
from db import WaterTemperature
from psycopg2 import OperationalError


class WaterTemperatureServer():
    name = "water_temperature_server"

    @rpc
    def receive_water_temperature(self, waterTemperature):
        waterTemperature = round(waterTemperature, 1)
        wt = WaterTemperature()
        wt.value = waterTemperature
        wt.unit = ('C')
        try:
            db.session.add(wt)
            db.session.commit()
        except OperationalError:
            db.session.rollback()
        return waterTemperature
