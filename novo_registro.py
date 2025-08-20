contador = 0
ano = "25" 

clientes = {
    "1": "Signode",
    "2": "Starrett",
    "3": "Interbrilho",
    "4": "Radio Holland"
}

while True:
    print('===============================================================')
    print('======================== Novo Registro ========================')
    print('===============================================================')
    print("Escolha uma das opções abaixo:")
    print("1 - Importação")
    print("2 - Exportação")
    print("0 - Sair")

    opcao = input("Digite o número da opção: ")
    print('===============================================================')

    # ---- IMPORTAÇÃO ----
    if opcao == '1':
        while True:
            print('Escolha o cliente: ')
            for k, v in clientes.items():
                print(f"{k} - {v}")
            print("0 - Voltar")

            cliente = input('Digite o número do cliente: ')
            print('===============================================================')

            if cliente == '0':
                break  # Volta para o menu principal

            if cliente not in clientes:
                print("Cliente inválido. Tente novamente.")
                continue

            print(f"Importação para {clientes[cliente]} selecionada.")

            while True:
                print("Informe o tipo de transporte:")
                print("1 - Aéreo")
                print("2 - Marítimo")
                print("0 - Voltar")
                modelo = input("Digite o número do modelo: ")
                print('===============================================================')

                if modelo == '0':
                    break  

                elif modelo == '1':
                    contador += 1
                    ref = f"IA-{contador:04d}/{ano}"
                    print(f"Importação Aérea para {clientes[cliente]} selecionada.")
                    print(f"Referência gerada: {ref}")
                    break

                elif modelo == '2':
                    contador += 1
                    ref = f"IM-{contador:04d}/{ano}"
                    print(f"Importação Marítima para {clientes[cliente]} selecionada.")
                    print(f"Referência gerada: {ref}")
                    break

                else:
                    print("Opção inválida. Tente novamente.")

            break  # sai do loop do cliente após gerar a ref

    # ---- EXPORTAÇÃO ----
    elif opcao == '2':
        while True:
            print('Escolha o cliente: ')
            for k, v in clientes.items():
                print(f"{k} - {v}")
            print("0 - Voltar")

            cliente = input('Digite o número do cliente: ')
            print('===============================================================')

            if cliente == '0':
                break  # volta pro menu principal

            if cliente not in clientes:
                print("Cliente inválido. Tente novamente.")
                continue

            print(f"Exportação para {clientes[cliente]} selecionada.")

            while True:
                print("Informe o tipo de transporte:")
                print("1 - Aéreo")
                print("2 - Marítimo")
                print("3 - Rodoviário")
                print("0 - Voltar")
                modelo = input("Digite o número do modelo: ")
                print('===============================================================')

                if modelo == '0':
                    break  

                elif modelo == '1':
                    contador += 1
                    ref = f"EA-{contador:04d}/{ano}"
                    print(f"Exportação Aérea para {clientes[cliente]} selecionada.")
                    print(f"Referência gerada: {ref}")
                    break

                elif modelo == '2':
                    contador += 1
                    ref = f"EM-{contador:04d}/{ano}"
                    print(f"Exportação Marítima para {clientes[cliente]} selecionada.")
                    print(f"Referência gerada: {ref}")
                    break

                elif modelo == '3':
                    contador += 1
                    ref = f"ER-{contador:04d}/{ano}"
                    print(f"Exportação Rodoviária para {clientes[cliente]} selecionada.")
                    print(f"Referência gerada: {ref}")
                    break

                else:
                    print("Opção inválida. Tente novamente.")

            break  

    elif opcao == '0':
        print("Saindo do sistema... 👋")
        break

    else:
        print("Opção inválida. Tente novamente.")
        print('===============================================================')
        continue      