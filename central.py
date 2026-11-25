from materiais import TIPOS
from participantes import Entrega, Lote


class CentralReciclagem:
    def __init__(self, nome, capacidade_kg):
        self.nome = nome
        self._capacidade_kg = capacidade_kg
        self._estoque = {}
        for tipo in TIPOS:
            self._estoque[tipo] = []
        self._aguardando_triagem = []
        self._entregas = []
        self._lotes = []
        self.moradores = []
        self.pontos = []
        self.cooperativas = []

    def get_capacidade(self):
        return self._capacidade_kg

    def peso_em_estoque(self, tipo=None):
        total = 0
        if tipo is None:
            for lista in self._estoque.values():
                for material in lista:
                    total += material.get_peso()
            for material in self._aguardando_triagem:
                total += material.get_peso()
        else:
            for material in self._estoque[tipo]:
                total += material.get_peso()
        return total

    def ocupacao(self):
        return self.peso_em_estoque() / self._capacidade_kg * 100

    def buscar_morador(self, nome):
        for morador in self.moradores:
            if morador.nome.lower() == nome.lower():
                return morador
        return None

    def cadastrar_morador(self, morador):
        if self.buscar_morador(morador.nome) is not None:
            return False
        self.moradores.append(morador)
        return True

    def registrar_entrega(self, morador, ponto, material):
        if self.peso_em_estoque() + material.get_peso() > self._capacidade_kg:
            livre = self._capacidade_kg - self.peso_em_estoque()
            print(f"Entrega recusada: só cabem mais {livre:.2f} kg na central.")
            return False

        entrega = Entrega(morador, ponto, material)
        morador.adicionar_entrega(entrega)
        ponto.adicionar_entrega(entrega)
        self._entregas.append(entrega)

        if material.precisa_triagem():
            self._aguardando_triagem.append(material)
        else:
            self._estoque[material.get_tipo()].append(material)

        self.verificar_capacidade()
        return True

    def verificar_capacidade(self):
        ocupacao = self.ocupacao()
        if ocupacao >= 90:
            print(f"ALERTA: central com {ocupacao:.0f}% da capacidade, precisa mandar lote o quanto antes.")
        elif ocupacao >= 75:
            print(f"Aviso: central com {ocupacao:.0f}% da capacidade.")

    def get_aguardando_triagem(self):
        return self._aguardando_triagem

    def fazer_triagem(self):
        quantidade = len(self._aguardando_triagem)
        for material in self._aguardando_triagem:
            material.fazer_triagem()
            self._estoque[material.get_tipo()].append(material)
        self._aguardando_triagem = []
        return quantidade

    def enviar_lote(self, tipo, cooperativa):
        if not cooperativa.aceita(tipo):
            print(f"{cooperativa.nome} não recebe {tipo}.")
            return None
        if len(self._estoque[tipo]) == 0:
            print(f"Não tem {tipo} pronto pra envio.")
            return None

        lote = Lote(tipo, self._estoque[tipo], cooperativa)
        cooperativa.receber_lote(lote)
        self._lotes.append(lote)
        self._estoque[tipo] = []
        return lote

    def mostrar_estoque(self):
        print(f"\nEstoque da {self.nome}")
        for tipo in TIPOS:
            print(f"  {tipo:<12} {self.peso_em_estoque(tipo):>8.2f} kg")
        peso_triagem = 0
        for material in self._aguardando_triagem:
            peso_triagem += material.get_peso()
        print(f"  {'triagem':<12} {peso_triagem:>8.2f} kg ({len(self._aguardando_triagem)} itens)")
        print(f"Ocupação: {self.peso_em_estoque():.2f} de {self._capacidade_kg:.0f} kg ({self.ocupacao():.0f}%)")
