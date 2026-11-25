TIPOS = ["papel", "plastico", "vidro", "metal", "eletronicos"]


class MaterialReciclavel:
    litros_por_kg = 10

    def __init__(self, tipo, peso_kg, limpo=True):
        self._tipo = tipo
        self._peso_kg = peso_kg
        self._limpo = limpo

    def get_tipo(self):
        return self._tipo

    def get_peso(self):
        return self._peso_kg

    def esta_limpo(self):
        return self._limpo

    def precisa_triagem(self):
        return not self._limpo

    def fazer_triagem(self):
        self._limpo = True

    def volume_estimado(self):
        return self._peso_kg * self.litros_por_kg

    def cuidados(self):
        if self._limpo:
            return "sem cuidado especial"
        return "lavar e secar antes de mandar pro lote"

    def __str__(self):
        situacao = "limpo" if self._limpo else "sujo"
        return f"{self._tipo} - {self._peso_kg:.2f} kg ({situacao})"


class Papel(MaterialReciclavel):
    litros_por_kg = 8

    def __init__(self, peso_kg, limpo=True):
        super().__init__("papel", peso_kg, limpo)

    def cuidados(self):
        if self._limpo:
            return "guardar em lugar seco"
        return "separar a parte suja, papel engordurado não recicla"


class Plastico(MaterialReciclavel):
    litros_por_kg = 20

    def __init__(self, peso_kg, limpo=True):
        super().__init__("plastico", peso_kg, limpo)


class Metal(MaterialReciclavel):
    litros_por_kg = 5

    def __init__(self, peso_kg, limpo=True):
        super().__init__("metal", peso_kg, limpo)


class Vidro(MaterialReciclavel):
    litros_por_kg = 2.5

    def __init__(self, peso_kg, limpo=True, quebrado=False):
        super().__init__("vidro", peso_kg, limpo)
        self._quebrado = quebrado

    def esta_quebrado(self):
        return self._quebrado

    def cuidados(self):
        texto = super().cuidados()
        if self._quebrado:
            return texto + "; vidro quebrado, usar luva e guardar em caixa fechada"
        return texto + "; transportar em caixa pra não quebrar"

    def __str__(self):
        texto = super().__str__()
        if self._quebrado:
            texto += " [quebrado]"
        return texto


class Eletronico(MaterialReciclavel):
    litros_por_kg = 4

    def __init__(self, peso_kg, descricao=""):
        super().__init__("eletronicos", peso_kg, True)
        self._descricao = descricao
        self._triado = False

    def precisa_triagem(self):
        return not self._triado

    def fazer_triagem(self):
        self._triado = True

    def cuidados(self):
        return "descarte especial: tirar pilhas e baterias, só vai pra cooperativa habilitada"

    def __str__(self):
        texto = f"eletronicos - {self._peso_kg:.2f} kg"
        if self._descricao:
            texto += f" ({self._descricao})"
        if not self._triado:
            texto += " [aguardando triagem]"
        return texto


def criar_material(tipo, peso_kg, limpo=True, quebrado=False, descricao=""):
    match tipo:
        case "papel":
            return Papel(peso_kg, limpo)
        case "plastico":
            return Plastico(peso_kg, limpo)
        case "metal":
            return Metal(peso_kg, limpo)
        case "vidro":
            return Vidro(peso_kg, limpo, quebrado)
        case "eletronicos":
            return Eletronico(peso_kg, descricao)
        case _:
            return None
