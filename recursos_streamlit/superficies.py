import numpy as np

class Superficie3D:
    def __init__(self, x_range, y_range):
        self.x_range = x_range
        self.y_range = y_range
        self.x, self.y = np.meshgrid(np.linspace(x_range[0], x_range[1], 100), 
                                     np.linspace(y_range[0], y_range[1], 100))

    def calcular_z(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def generar_datos(self):
        self.z = self.calcular_z()
        return self.x, self.y, self.z

class Plano(Superficie3D):
    def __init__(self, x_range, y_range, pendiente):
        super().__init__(x_range, y_range)
        self.pendiente = pendiente

    def calcular_z(self):
        return self.pendiente * self.x

class Paraboloide(Superficie3D):
    def __init__(self, x_range, y_range, coef):
        super().__init__(x_range, y_range)
        self.coef = coef

    def calcular_z(self):
        return self.coef * (self.x**2 + self.y**2)

class Sinusoide(Superficie3D):
    def __init__(self, x_range, y_range, frecuencia):
        super().__init__(x_range, y_range)
        self.frecuencia = frecuencia

    def calcular_z(self):
        return np.sin(self.frecuencia * np.sqrt(self.x**2 + self.y**2))
