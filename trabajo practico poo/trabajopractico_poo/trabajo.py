class Sensor:
    def __init__(self, id, ubicacion):
        self.id = id
        self.humedad = 0.0
        self.ubicacion = ubicacion

    def medirHumedad(self):
        # Simulación de medición de humedad
        import random
        self.humedad = random.uniform(0, 100)

    def obtenerHumedad(self):
        return self.humedad

class InterfazUsuario:
    def __init__(self):
        self.nivelHumedad = 0.0
        self.alertas = []
