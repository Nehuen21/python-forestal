from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    def __init__(self, id: int, variedad: str, superficie: float, altura: float = 1.0, agua: float = 0.0):
        super().__init__(id, variedad)
        self._superficie = superficie
        self._altura = altura
        self._agua = agua

    # ===== GETTERS =====
    def get_superficie(self) -> float:
        return self._superficie

    def get_altura(self) -> float:
        return self._altura

    def get_agua(self) -> float:
        return self._agua

    # ===== SETTERS =====
    def set_superficie(self, superficie: float) -> None:
        self._superficie = superficie

    def set_altura(self, altura: float) -> None:
        self._altura = altura

    def set_agua(self, agua: float) -> None:
        self._agua = agua

    # ===== OPERACIONES =====
    def crecer(self, incremento: float):
        self._altura += incremento

    def absorber_agua(self, cantidad: float):
        self._agua += cantidad