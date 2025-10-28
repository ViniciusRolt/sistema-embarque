import datetime

embarques = {}
contador = 0
ano = "25"

clientes = {
    "1": "Signode",
    "2": "Starrett",
    "3": "Interbrilho",
    "4": "Radio Holland"
}

def gerar_referencia(tipo_operacao, tipo_transporte, contador_atual):
    """Gera a referência única do embarque."""
    global contador
    contador = contador_atual + 1
    
    prefixos = {
        ("Importação", "Aéreo"): "IA",
        ("Importação", "Marítimo"): "IM",
        ("Exportação", "Aéreo"): "EA",
        ("Exportação", "Marítimo"): "EM",
        ("Exportação", "Rodoviário"): "ER",
    }
    
    prefixo = prefixos.get((tipo_operacao, tipo_transporte))
    if not prefixo:
        raise ValueError("Combinação de operação e transporte inválida.")
        
    return f"{prefixo}-{contador:04d}/{ano}", contador

def registrar_embarque(tipo_operacao, cliente_id, transporte_nome):
    """Função para registrar um novo embarque com as novas informações."""
    global contador
    global embarques

    cliente_nome = clientes[cliente_id]
    
    while True:
        data_str = input("Informe a data de registro (DD/MM/AAAA): ")
        try:
            data_registro = datetime.datetime.strptime(data_str, "%d/%m/%Y").strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Formato de data inválido. Use DD/MM/AAAA.")

    ref_cliente = input("Informe a referência do cliente (ou 0 se não houver): ")
    if ref_cliente == "0":
        ref_cliente = "N/A"
    
    try:
        ref, contador = gerar_referencia(tipo_operacao, transporte_nome, contador)
    except ValueError as e:
        print(f"Erro ao gerar referência: {e}")
        return

    embarques[ref] = {
        "tipo": tipo_operacao,
        "cliente": cliente_nome,
        "transporte": transporte_nome,
        "data_registro": data_registro,
        "ref_cliente": ref_cliente
    }
    
    print(f"\n--- Embarque Registrado ---")
    print(f"Referência Gerada: {ref}")
    print(f"Cliente: {cliente_nome}")
    print(f"Tipo: {tipo_operacao} ({transporte_nome})")
    print(f"Data de Registro: {data_str}")
    print(f"Referência do Cliente: {ref_cliente}")
    print("---------------------------\n")

def exibir_embarques():
    """Exibe todas as referências abertas (registradas) e quando foram abertas."""
    if not embarques:
        print("\nNenhum embarque registrado ainda.")
        return

    print("\n===============================================================")
    print("===================== Embarques Registrados ===================")
    print("===============================================================")
    
    embarques_ordenados = sorted(embarques.items(), key=lambda item: item[1]["data_registro"])
    
    print(f"{"Referência":<15} | {"Data de Registro":<18} | {"Cliente":<15} | {"Tipo":<10} | {"Ref. Cliente":<15}")
    print("-" * 85)
    
    for ref, dados in embarques_ordenados:
        data_formatada = datetime.datetime.strptime(dados["data_registro"], "%Y-%m-%d").strftime("%d/%m/%Y")
        tipo_abreviado = dados["tipo"][0] + dados["transporte"][0]
        print(f"{ref:<15} | {data_formatada:<18} | {dados["cliente"]:<15} | {tipo_abreviado:<10} | {dados["ref_cliente"]:<15}")
        
    print("===============================================================\n")

def gerenciar_embarque():
    """Permite editar ou excluir um embarque existente."""
    exibir_embarques()
    if not embarques:
        return

    ref_alvo = input("Digite a Referência do embarque para gerenciar (ou 0 para voltar): ").upper()
    if ref_alvo == "0":
        return

    if ref_alvo not in embarques:
        print(f"Referência \'{ref_alvo}\' não encontrada.")
        return

    dados = embarques[ref_alvo]
    print(f"\nEmbarque selecionado: {ref_alvo} - Cliente: {dados["cliente"]}")
    print("O que deseja fazer?")
    print("1 - Editar Referência do Cliente")
    print("2 - Excluir Embarque")
    print("0 - Voltar")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        nova_ref_cliente = input(f"Nova Referência do Cliente (atual: {dados["ref_cliente"]}, ou 0 para N/A): ")
        if nova_ref_cliente == "0":
            nova_ref_cliente = "N/A"
        
        embarques[ref_alvo]["ref_cliente"] = nova_ref_cliente
        print(f"Referência do Cliente para {ref_alvo} atualizada para: {nova_ref_cliente}")

    elif opcao == "2":
        confirmacao = input(f"Tem certeza que deseja EXCLUIR o embarque {ref_alvo}? (S/N): ").upper()
        if confirmacao == "S":
            del embarques[ref_alvo]
            print(f"Embarque {ref_alvo} excluído com sucesso.")
        else:
            print("Exclusão cancelada.")
    
    elif opcao == "0":
        return
    else:
        print("Opção inválida.")

while True:
    print("\n===============================================================")
    print("==================== Sistema de Embarques =====================")
    print("===============================================================")
    print("Escolha uma das opções abaixo:")
    print("1 - Novo Registro (Importação)")
    print("2 - Novo Registro (Exportação)")
    print("3 - Exibir Referências Abertas")
    print("4 - Gerenciar Embarque (Editar/Excluir)")
    print("0 - Sair")

    opcao = input("Digite o número da opção: ")
    print("===============================================================")

    if opcao == "1":
        tipo_operacao = "Importação"
        while True:
            print("Escolha o cliente: ")
            for k, v in clientes.items():
                print(f"{k} - {v}")
            print("0 - Voltar")

            cliente = input("Digite o número do cliente: ")
            print("===============================================================")

            if cliente == "0":
                break

            if cliente not in clientes:
                print("Cliente inválido. Tente novamente.")
                continue

            print(f"{tipo_operacao} para {clientes[cliente]} selecionada.")

            while True:
                print("Informe o tipo de transporte:")
                print("1 - Aéreo")
                print("2 - Marítimo")
                print("0 - Voltar")
                modelo = input("Digite o número do modelo: ")
                print("===============================================================")

                if modelo == "0":
                    break
                
                if modelo == "1":
                    transporte_nome = "Aéreo"
                elif modelo == "2":
                    transporte_nome = "Marítimo"
                else:
                    print("Opção inválida. Tente novamente.")
                    continue
                
                registrar_embarque(tipo_operacao, cliente, transporte_nome)
                break
            
            break

    elif opcao == "2":
        tipo_operacao = "Exportação"
        while True:
            print("Escolha o cliente: ")
            for k, v in clientes.items():
                print(f"{k} - {v}")
            print("0 - Voltar")

            cliente = input("Digite o número do cliente: ")
            print("===============================================================")

            if cliente == "0":
                break

            if cliente not in clientes:
                print("Cliente inválido. Tente novamente.")
                continue

            print(f"{tipo_operacao} para {clientes[cliente]} selecionada.")

            while True:
                print("Informe o tipo de transporte:")
                print("1 - Aéreo")
                print("2 - Marítimo")
                print("3 - Rodoviário")
                print("0 - Voltar")
                modelo = input("Digite o número do modelo: ")
                print("===============================================================")

                if modelo == "0":
                    break
                
                if modelo == "1":
                    transporte_nome = "Aéreo"
                elif modelo == "2":
                    transporte_nome = "Marítimo"
                elif modelo == "3":
                    transporte_nome = "Rodoviário"
                else:
                    print("Opção inválida. Tente novamente.")
                    continue
                
                registrar_embarque(tipo_operacao, cliente, transporte_nome)
                break
            
            break

    elif opcao == "3":
        exibir_embarques()

    elif opcao == "4":
        gerenciar_embarque()

    elif opcao == "0":
        print("Saindo do sistema... 👋")
        break

    else:
        print("Opção inválida. Tente novamente.")
        print("===============================================================")
        continue
