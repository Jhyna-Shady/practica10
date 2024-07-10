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

class Hiperboloide(Superficie3D):
    def __init__(self, x_range, y_range, a, b, c):
        super().__init__(x_range, y_range)
        self.a = a
        self.b = b
        self.c = c

    def calcular_z(self):
        return (self.x**2 / self.a**2 - self.y**2 / self.b**2) * self.c

class Esfera(Superficie3D):
    def __init__(self, x_range, y_range, radio):
        super().__init__(x_range, y_range)
        self.radio = radio

    def calcular_z(self):
        z_pos = np.sqrt(np.maximum(0, self.radio**2 - self.x**2 - self.y**2))
        return z_pos  # Solo devuelve la parte positiva de la esfera
