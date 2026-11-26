from materiais import Papel, Plastico, Vidro


class Central:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.estoque = []

    def peso_total(self):
        total = 0
        for material in self.estoque:
            total += material.get_peso()
        return total

    def receber(self):
        tipo = input("Tipo (papel, plastico ou vidro): ").lower()
        peso = float(input("Peso em kg: "))

        if tipo == "papel":
            material = Papel(peso)
        elif tipo == "plastico":
            material = Plastico(peso)
        elif tipo == "vidro":
            material = Vidro(peso)
        else:
            print("Tipo inválido")
            return

        if self.peso_total() + peso > self.capacidade:
            print("A central está cheia!")
            return

        self.estoque.append(material)
        print("Material recebido!")
        print("Cuidados:", material.cuidados())

    def mostrar_estoque(self):
        if len(self.estoque) == 0:
            print("Estoque vazio")
        for material in self.estoque:
            print(material)
        print(f"Total: {self.peso_total()} de {self.capacidade} kg")

    def enviar_lote(self):
        print(f"Enviando {self.peso_total()} kg pra cooperativa...")
        self.estoque = []
