import random

class Sensor:
    def __init__(self, id, ubicacion):
        self.id = id
        self.humedad = 0.0
        self.ubicacion = ubicacion

    def medirHumedad(self):
        
        self.humedad = random.uniform(0, 100)

    def obtenerHumedad(self):
        return self.humedad


class InterfazUsuario:
    def __init__(self):
        self.nivelHumedad = 0.0
        self.alertas = []

    def mostrarDatos(self, humedad):
        self.nivelHumedad = humedad
        print(f"Nivel Actual de Humedad: {self.nivelHumedad}%")

    def mostrarAlertas(self, alerta):
        self.alertas.append(alerta)
        print(f"Alerta: {alerta}")

    def configurarRiego(self, umbralBajo, umbralAlto):
        print(f"Configuración de Riego: Humedad Baja {umbralBajo}%, Humedad Alta {umbralAlto}%")


class Riego:
    def __init__(self, umbralBajo, umbralAlto):
        self.umbralBajo = umbralBajo
        self.umbralAlto = umbralAlto

    def ajustarRiego(self, humedad):
        if humedad < self.umbralBajo:
            return "Aumentar riego"
        elif humedad > self.umbralAlto:
            return "Reducir riego"
        else:
            return "Riego adecuado"

    def obtenerConfiguracion(self):
        return f"Umbral Bajo: {self.umbralBajo}, Umbral Alto: {self.umbralAlto}"

# Uso
sensor = Sensor(1, "Jardín")
sensor.medirHumedad()
humedad_actual = sensor.obtenerHumedad()

interfaz = InterfazUsuario()
interfaz.mostrarDatos(humedad_actual)

riego = Riego(20.0, 60.0)
recomendacion = riego.ajustarRiego(humedad_actual)
interfaz.mostrarAlertas(recomendacion)

