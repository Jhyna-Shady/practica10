import numpy as np  # Importa la biblioteca numpy, que es útil para trabajar con arreglos y funciones matemáticas.

# Clase base para superficies 3D
class Superficie3D:
    def __init__(self, x_range, y_range):
        # Inicializa los rangos de x e y y crea una malla de puntos
        self.x_range = x_range  # Guarda el rango de valores para x.
        self.y_range = y_range  # Guarda el rango de valores para y.
        self.x, self.y = np.meshgrid(np.linspace(x_range[0], x_range[1], 100), 
                                     np.linspace(y_range[0], y_range[1], 100))  # Crea una malla de puntos en los rangos especificados para x e y.

    # Método que deben implementar las subclases para calcular z
    def calcular_z(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")  # Define un método abstracto que debe ser implementado por las subclases.

    # Genera los datos de la superficie llamando a calcular_z
    def generar_datos(self):
        self.z = self.calcular_z()  # Llama al método calcular_z para obtener los valores de z.
        return self.x, self.y, self.z  # Retorna los valores de x, y y z.

# Clase para un plano
class Plano(Superficie3D):
    def __init__(self, x_range, y_range, pendiente):
        # Llama al constructor de la clase base
        super().__init__(x_range, y_range)  # Llama al constructor de la clase base Superficie3D.
        self.pendiente = pendiente  # Guarda la pendiente del plano.

    # Implementa el cálculo de z para un plano
    def calcular_z(self):
        return self.pendiente * self.x  # Calcula z como una función lineal de x con la pendiente dada.

# Clase para un paraboloide
class Paraboloide(Superficie3D):
    def __init__(self, x_range, y_range, coef):
        # Llama al constructor de la clase base
        super().__init__(x_range, y_range)  # Llama al constructor de la clase base Superficie3D.
        self.coef = coef  # Guarda el coeficiente del paraboloide.

    # Implementa el cálculo de z para un paraboloide
    def calcular_z(self):
        return self.coef * (self.x**2 + self.y**2)  # Calcula z como una función cuadrática de x e y.

# Clase para una sinusoide
class Sinusoide(Superficie3D):
    def __init__(self, x_range, y_range, frecuencia):
        # Llama al constructor de la clase base
        super().__init__(x_range, y_range)  # Llama al constructor de la clase base Superficie3D.
        self.frecuencia = frecuencia  # Guarda la frecuencia de la sinusoide.

    # Implementa el cálculo de z para una sinusoide
    def calcular_z(self):
        return np.sin(self.frecuencia * np.sqrt(self.x**2 + self.y**2))  # Calcula z como una función sinusoidal de x e y, basada en la frecuencia.

# Clase para un hiperboloide
class Hiperboloide(Superficie3D):
    def __init__(self, x_range, y_range, a, b, c):
        # Llama al constructor de la clase base
        super().__init__(x_range, y_range)  # Llama al constructor de la clase base Superficie3D.
        self.a = a  # Guarda el valor de 'a'.
        self.b = b  # Guarda el valor de 'b'.
        self.c = c  # Guarda el valor de 'c'.

    # Implementa el cálculo de z para un hiperboloide
    def calcular_z(self):
        return (self.x**2 / self.a**2 - self.y**2 / self.b**2) * self.c  # Calcula z como una función racional de x e y, basada en los parámetros a, b y c.

# Clase para una esfera
class Esfera(Superficie3D):
    def __init__(self, x_range, y_range, radio):
        # Llama al constructor de la clase base
        super().__init__(x_range, y_range)  # Llama al constructor de la clase base Superficie3D.
        self.radio = radio  # Guarda el radio de la esfera.

    # Implementa el cálculo de z para una esfera
    def calcular_z(self):
        # Calcula la parte positiva de z para la esfera
        z_pos = np.sqrt(np.maximum(0, self.radio**2 - self.x**2 - self.y**2))  # Calcula z usando la fórmula de la esfera, asegurándose de no tener valores negativos bajo la raíz cuadrada.
        return z_pos  # Retorna la parte positiva de z.
