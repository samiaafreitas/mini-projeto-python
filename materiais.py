class Material:
    def __init__(self, tipo, peso):
        self.tipo = tipo
        self._peso = peso

    def get_peso(self):
        return self._peso

    def cuidados(self):
        return "nenhum"

    def __str__(self):
        return f"{self.tipo} - {self._peso} kg"


class Papel(Material):
    def __init__(self, peso):
        super().__init__("papel", peso)

    def cuidados(self):
        return "guardar em lugar seco"


class Plastico(Material):
    def __init__(self, peso):
        super().__init__("plastico", peso)

    def cuidados(self):
        return "lavar antes de entregar"


class Vidro(Material):
    def __init__(self, peso):
        super().__init__("vidro", peso)

    def cuidados(self):
        return "levar em caixa fechada pra nao quebrar"
