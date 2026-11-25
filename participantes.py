from datetime import date


class Entrega:
    def __init__(self, morador, ponto, material):
        self.morador = morador
        self.ponto = ponto
        self.material = material
        self.data = date.today()

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y')} | {self.material} | {self.morador.nome} em {self.ponto.nome}"


class Lote:
    def __init__(self, tipo, materiais, cooperativa):
        self.tipo = tipo
        self.materiais = materiais
        self.cooperativa = cooperativa
        self.data = date.today()

    def peso_total(self):
        total = 0
        for material in self.materiais:
            total += material.get_peso()
        return total

    def volume_estimado(self):
        total = 0
        for material in self.materiais:
            total += material.volume_estimado()
        return total

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y')} | lote de {self.tipo} | {self.peso_total():.2f} kg | {self.cooperativa.nome}"


class Morador:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self._entregas = []

    def adicionar_entrega(self, entrega):
        self._entregas.append(entrega)

    def get_entregas(self):
        return self._entregas

    def total_entregue_kg(self):
        total = 0
        for entrega in self._entregas:
            total += entrega.material.get_peso()
        return total

    def __str__(self):
        return f"{self.nome} ({self.endereco})"


class PontoColeta:
    def __init__(self, nome, bairro):
        self.nome = nome
        self.bairro = bairro
        self._entregas = []

    def adicionar_entrega(self, entrega):
        self._entregas.append(entrega)

    def get_entregas(self):
        return self._entregas

    def total_recebido_kg(self):
        total = 0
        for entrega in self._entregas:
            total += entrega.material.get_peso()
        return total

    def __str__(self):
        return f"{self.nome} - {self.bairro}"


class CooperativaDestino:
    def __init__(self, nome, aceita_eletronicos=False):
        self.nome = nome
        self.aceita_eletronicos = aceita_eletronicos
        self._lotes = []

    def aceita(self, tipo):
        if tipo == "eletronicos":
            return self.aceita_eletronicos
        return True

    def receber_lote(self, lote):
        self._lotes.append(lote)

    def get_lotes(self):
        return self._lotes

    def total_recebido_kg(self):
        total = 0
        for lote in self._lotes:
            total += lote.peso_total()
        return total

    def __str__(self):
        if self.aceita_eletronicos:
            return f"{self.nome} (aceita eletrônicos)"
        return self.nome
