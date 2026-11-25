from central import CentralReciclagem
from materiais import TIPOS, criar_material
from participantes import Morador, PontoColeta, CooperativaDestino


def ler_numero(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        if texto.replace(".", "", 1).isdigit() and float(texto) > 0:
            return float(texto)
        print("Valor inválido, digite um número maior que zero.")


def ler_sim_nao(mensagem):
    resposta = input(mensagem + " (s/n): ").strip().lower()
    return resposta == "s"


def escolher(lista, titulo):
    if len(lista) == 0:
        print("Nada cadastrado ainda.")
        return None
    print(titulo)
    for i in range(len(lista)):
        print(f"  {i + 1} - {lista[i]}")
    escolha = input("Número: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(lista):
        return lista[int(escolha) - 1]
    print("Opção inválida.")
    return None


def montar_central():
    central = CentralReciclagem("Central PontoVerde", 500)
    central.pontos.append(PontoColeta("Ecoponto Praça do Diário", "Santo Antônio"))
    central.pontos.append(PontoColeta("Escola Municipal Várzea", "Várzea"))
    central.cooperativas.append(CooperativaDestino("Coopagres"))
    central.cooperativas.append(CooperativaDestino("Recicla Eletro PE", aceita_eletronicos=True))
    central.cadastrar_morador(Morador("Dona Lúcia", "Rua do Sol, 120"))
    central.cadastrar_morador(Morador("Seu Raimundo", "Av. Caxangá, 45"))
    return central


def cadastrar_morador(central):
    nome = input("Nome: ").strip()
    endereco = input("Endereço: ").strip()
    if nome == "":
        print("O nome não pode ficar vazio.")
        return
    if central.cadastrar_morador(Morador(nome, endereco)):
        print(f"{nome} cadastrado(a).")
    else:
        print("Já existe um morador com esse nome.")


def registrar_entrega(central):
    morador = escolher(central.moradores, "Quem está entregando?")
    if morador is None:
        return
    ponto = escolher(central.pontos, "Em qual ponto de coleta?")
    if ponto is None:
        return
    tipo = escolher(TIPOS, "Tipo de material:")
    if tipo is None:
        return

    peso = ler_numero("Peso (kg): ")
    limpo = True
    quebrado = False
    descricao = ""
    if tipo == "eletronicos":
        descricao = input("O que é (ex.: celular, teclado): ").strip()
    else:
        limpo = ler_sim_nao("Está limpo?")
    if tipo == "vidro":
        quebrado = ler_sim_nao("Tem vidro quebrado?")

    material = criar_material(tipo, peso, limpo, quebrado, descricao)
    if central.registrar_entrega(morador, ponto, material):
        print(f"Entrega registrada: {material}")
        print(f"Cuidados: {material.cuidados()}")
        print(f"Volume estimado: {material.volume_estimado():.1f} litros")


def fazer_triagem(central):
    pendentes = central.get_aguardando_triagem()
    if len(pendentes) == 0:
        print("Nada esperando triagem.")
        return
    for material in pendentes:
        print(f"  {material} -> {material.cuidados()}")
    if ler_sim_nao("Marcar tudo como triado?"):
        quantidade = central.fazer_triagem()
        print(f"Itens triados e movidos pro estoque: {quantidade}")


def enviar_lote(central):
    tipo = escolher(TIPOS, "Qual material vai no lote?")
    if tipo is None:
        return
    cooperativa = escolher(central.cooperativas, "Pra qual cooperativa?")
    if cooperativa is None:
        return
    lote = central.enviar_lote(tipo, cooperativa)
    if lote is not None:
        print(f"Lote enviado: {lote}")


def historico_morador(central):
    morador = escolher(central.moradores, "Qual morador?")
    if morador is None:
        return
    entregas = morador.get_entregas()
    if len(entregas) == 0:
        print(f"{morador.nome} ainda não fez nenhuma entrega.")
        return
    for entrega in entregas:
        print(f"  {entrega}")
    print(f"Total: {morador.total_entregue_kg():.2f} kg")


def historico_cooperativa(central):
    cooperativa = escolher(central.cooperativas, "Qual cooperativa?")
    if cooperativa is None:
        return
    lotes = cooperativa.get_lotes()
    if len(lotes) == 0:
        print(f"Nenhum lote enviado pra {cooperativa.nome} ainda.")
        return
    for lote in lotes:
        print(f"  {lote}")


def menu():
    print("\n===== PontoVerde =====")
    print("1 - Cadastrar morador")
    print("2 - Registrar entrega")
    print("3 - Triagem")
    print("4 - Enviar lote")
    print("5 - Ver estoque")
    print("6 - Relatório")
    print("7 - Histórico de morador")
    print("8 - Lotes por cooperativa")
    print("0 - Sair")
    return input("Opção: ").strip()


def main():
    central = montar_central()
    while True:
        opcao = menu()
        match opcao:
            case "1":
                cadastrar_morador(central)
            case "2":
                registrar_entrega(central)
            case "3":
                fazer_triagem(central)
            case "4":
                enviar_lote(central)
            case "5":
                central.mostrar_estoque()
            case "6":
                central.relatorio()
            case "7":
                historico_morador(central)
            case "8":
                historico_cooperativa(central)
            case "0":
                print("Até mais!")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
