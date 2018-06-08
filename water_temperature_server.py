from nameko.rpc import rpc
import db
from db import WaterTemperature


class WaterTemperatureServer():
    name = "water_temperature_server"

    @rpc
    def receive_water_temperature(self, waterTemperature):
        waterTemperature = round(waterTemperature, 1)
        wt = WaterTemperature()
        wt.value = waterTemperature
        wt.unit = ('C')
        db.session.add(t)
        db.session.commit()
        return waterTemperature
