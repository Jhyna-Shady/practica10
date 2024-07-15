import numpy as np

# Clase base para superficies 3D
class Superficie3D:
    def __init__(self, x_range, y_range):
        # Inicializa los rangos de x e y y crea una malla de puntos
        self.x_range = x_range
        self.y_range = y_range
        self.x, self.y = np.meshgrid(np.linspace(x_range[0], x_range[1], 300), 
                                     np.linspace(y_range[0], y_range[1], 300))

    # Método que deben implementar las subclases para calcular z
    def calcular_z(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    # Genera los datos de la superficie llamando a calcular_z
    def generar_datos(self):
        self.z = self.calcular_z()
        return self.x, self.y, self.z

# Clase para un plano
class Plano(Superficie3D):
    def __init__(self, x_range, y_range, pendiente):
        # Llama al constructor de la clase base
        super().__init__(x_range, y_range)
        self.pendiente = pendiente

    # Implementa el cálculo de z para un plano
    def calcular_z(self):
        return self.pendiente * self.x

# Clase para un paraboloide
class Paraboloide(Superficie3D):
    def __init__(self, x_range, y_range, coef):
        # Llama al constructor de la clase base
        super().__init__(x_range, y_range)
        self.coef = coef

    # Implementa el cálculo de z para un paraboloide
    def calcular_z(self):
        return self.coef * (self.x**2 + self.y**2)

# Clase para una sinusoide
class Sinusoide(Superficie3D):
    def __init__(self, x_range, y_range, frecuencia):
        # Llama al constructor de la clase base
        super().__init__(x_range, y_range)
        self.frecuencia = frecuencia

    # Implementa el cálculo de z para una sinusoide
    def calcular_z(self):
        return np.sin(self.frecuencia * np.sqrt(self.x**2 + self.y**2))

# Clase para un hiperboloide
class Hiperboloide(Superficie3D):
    def __init__(self, x_range, y_range, a, b, c):
        # Llama al constructor de la clase base
        super().__init__(x_range, y_range)
        self.a = a
        self.b = b
        self.c = c

    # Implementa el cálculo de z para un hiperboloide
    def calcular_z(self):
        return (self.x**2 / self.a**2 - self.y**2 / self.b**2) * self.c

# Clase para una esfera
class Esfera(Superficie3D):
    def __init__(self, x_range, y_range, radio):
        # Llama al constructor de la clase base
        super().__init__(x_range, y_range)
        self.radio = radio

    # Implementa el cálculo de z para una esfera
    def calcular_z(self):
        # Calcula la parte positiva de z para la esfera
        z_pos = np.sqrt(np.maximum(0, self.radio**2 - self.x**2 - self.y**2))
        return z_pos

