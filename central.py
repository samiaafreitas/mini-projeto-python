from materiais import TIPOS


class Central:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
        self.estoque = {}
        for tipo in TIPOS:
            self.estoque[tipo] = 0
        self.triagem = []
        self.moradores = []
        self.cooperativas = []
        self.total_recebido = 0
        self.total_enviado = 0

    def peso_total(self):
        total = 0
        for peso in self.estoque.values():
            total += peso
        for material in self.triagem:
            total += material.get_peso()
        return total

    def registrar_entrega(self, morador, material):
        if self.peso_total() + material.get_peso() > self.capacidade:
            print("Não cabe mais na central, precisa mandar um lote antes.")
            return False

        morador.entregas.append(material)
        self.total_recebido += material.get_peso()

        if material.precisa_triagem():
            self.triagem.append(material)
        else:
            self.estoque[material.tipo] += material.get_peso()

        if self.peso_total() >= self.capacidade * 0.8:
            print("Aviso: a central está quase cheia!")
        return True

    def fazer_triagem(self):
        for material in self.triagem:
            material.limpo = True
            self.estoque[material.tipo] += material.get_peso()
        self.triagem = []

    def enviar_lote(self, tipo, cooperativa):
        if not cooperativa.aceita(tipo):
            print(f"A {cooperativa.nome} não recebe {tipo}.")
            return
        if self.estoque[tipo] == 0:
            print(f"Não tem {tipo} no estoque.")
            return

        peso = self.estoque[tipo]
        cooperativa.lotes.append(f"{tipo} - {peso} kg")
        self.total_enviado += peso
        self.estoque[tipo] = 0
        print(f"Lote de {peso} kg de {tipo} enviado pra {cooperativa.nome}.")

    def mostrar_estoque(self):
        print(f"\nEstoque da {self.nome}:")
        for tipo in TIPOS:
            print(f"  {tipo}: {self.estoque[tipo]} kg")
        print(f"  esperando triagem: {len(self.triagem)} itens")
        print(f"Total: {self.peso_total()} de {self.capacidade} kg")

    def relatorio(self):
        print(f"\nRelatório da {self.nome}")
        print(f"Total recebido: {self.total_recebido} kg")
        print(f"Total enviado: {self.total_enviado} kg")

        print("\nEntregas por morador:")
        for morador in self.moradores:
            print(f"  {morador.nome}: {morador.total_entregue()} kg")

        print("\nLotes por cooperativa:")
        for cooperativa in self.cooperativas:
            print(f"  {cooperativa.nome}: {len(cooperativa.lotes)} lotes")
            for lote in cooperativa.lotes:
                print(f"    {lote}")
