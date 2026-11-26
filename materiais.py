TIPOS = ["papel", "plastico", "vidro", "metal", "eletronicos"]


class Material:
    def __init__(self, tipo, peso, limpo=True):
        self.tipo = tipo
        self._peso = peso
        self.limpo = limpo

    def get_peso(self):
        return self._peso

    def precisa_triagem(self):
        return not self.limpo

    def cuidados(self):
        if self.limpo:
            return "nenhum"
        return "lavar antes de guardar"

    def __str__(self):
        texto = f"{self.tipo} - {self._peso} kg"
        if not self.limpo:
            texto += " (sujo)"
        return texto


class Papel(Material):
    def __init__(self, peso, limpo=True):
        super().__init__("papel", peso, limpo)

    def cuidados(self):
        if self.limpo:
            return "guardar em lugar seco"
        return "papel sujo de gordura não recicla, separar"


class Plastico(Material):
    def __init__(self, peso, limpo=True):
        super().__init__("plastico", peso, limpo)


class Metal(Material):
    def __init__(self, peso, limpo=True):
        super().__init__("metal", peso, limpo)


class Vidro(Material):
    def __init__(self, peso, limpo=True):
        super().__init__("vidro", peso, limpo)

    def cuidados(self):
        return super().cuidados() + " e levar em caixa fechada"


class Eletronico(Material):
    def __init__(self, peso):
        super().__init__("eletronicos", peso)

    def precisa_triagem(self):
        return True

    def cuidados(self):
        return "tirar pilhas e baterias"


def criar_material(tipo, peso, limpo):
    if tipo == "papel":
        return Papel(peso, limpo)
    elif tipo == "plastico":
        return Plastico(peso, limpo)
    elif tipo == "vidro":
        return Vidro(peso, limpo)
    elif tipo == "metal":
        return Metal(peso, limpo)
    else:
        return Eletronico(peso)
