from central import Central

central = Central(100)
opcao = ""

while opcao != "0":
    print("\n1 - Entregar material\n2 - Ver estoque\n3 - Enviar lote\n0 - Sair")
    opcao = input("Opção: ")
    match opcao:
        case "1":
            central.receber()
        case "2":
            central.mostrar_estoque()
        case "3":
            central.enviar_lote()
