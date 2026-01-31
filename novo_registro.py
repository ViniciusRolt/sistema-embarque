import datetime

class Embarque:
    def __init__(self, referencia, tipo_operacao, cliente_nome, transporte, data_registro, ref_cliente):
        self.referencia = referencia
        self.tipo_operacao = tipo_operacao
        self.cliente_nome = cliente_nome
        self.transporte = transporte
        self.data_registro = data_registro
        self.ref_cliente = ref_cliente

    def __str__(self):
        return f"{self.referencia} | {self.cliente_nome} ({self.transporte})"

class SistemaGerenciador:
    def __init__(self):
        self.embarques = {}
        self.contador = 0
        self.ano_atual = "25"
        self.clientes = {
            "1": "Signode",
            "2": "Starrett",
            "3": "Interbrilho",
            "4": "Radio Holland"
        }
    
    def get_cliente_nome(self, id_cliente):
        return self.clientes.get(id_cliente)

    def listar_clientes(self):
        return self.clientes.items()

    def gerar_referencia(self, tipo_operacao, tipo_transporte):
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
        
        self.contador += 1
        return f"{prefixo}-{self.contador:04d}/{self.ano_atual}"

    def criar_embarque(self, tipo_operacao, cliente_nome, transporte, data_registro, ref_cliente):
        ref = self.gerar_referencia(tipo_operacao, transporte)
        
        novo_embarque = Embarque(
            referencia=ref,
            tipo_operacao=tipo_operacao,
            cliente_nome=cliente_nome,
            transporte=transporte,
            data_registro=data_registro,
            ref_cliente=ref_cliente
        )
        
        self.embarques[ref] = novo_embarque
        return novo_embarque

    def buscar_embarque(self, referencia):
        return self.embarques.get(referencia)

    def obter_todos_embarques(self):
        lista = list(self.embarques.values())
        lista.sort(key=lambda x: x.data_registro)
        return lista

    def editar_ref_cliente(self, referencia, nova_ref):
        if referencia in self.embarques:
            self.embarques[referencia].ref_cliente = nova_ref
            return True
        return False

    def excluir_embarque(self, referencia):
        if referencia in self.embarques:
            del self.embarques[referencia]
            return True
        return False

class InterfaceConsole:
    """Gerencia a interação com o usuário (Inputs e Prints)."""
    def __init__(self):
        self.sistema = SistemaGerenciador()

    def _ler_data(self):
        while True:
            data_str = input("Informe a data de registro (DD/MM/AAAA): ")
            try:
                return datetime.datetime.strptime(data_str, "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                print("⚠️ Formato inválido. Use DD/MM/AAAA.")

    def _selecionar_cliente(self):
        while True:
            print("\n--- Seleção de Cliente ---")
            for k, v in self.sistema.listar_clientes():
                print(f"{k} - {v}")
            print("0 - Voltar")
            
            escolha = input("Digite o número do cliente: ")
            if escolha == "0": return None
            
            nome = self.sistema.get_cliente_nome(escolha)
            if nome: return nome
            print("⚠️ Cliente inválido.")

    def _selecionar_transporte(self, tipo_operacao):
        opcoes = {
            "1": "Aéreo",
            "2": "Marítimo"
        }
        if tipo_operacao == "Exportação":
            opcoes["3"] = "Rodoviário"

        while True:
            print(f"\n--- Transporte ({tipo_operacao}) ---")
            for k, v in opcoes.items():
                print(f"{k} - {v}")
            print("0 - Voltar")
            
            escolha = input("Opção: ")
            if escolha == "0": return None
            if escolha in opcoes: return opcoes[escolha]
            print("⚠️ Opção inválida.")

    def menu_novo_registro(self, tipo_operacao):
        cliente = self._selecionar_cliente()
        if not cliente: return

        transporte = self._selecionar_transporte(tipo_operacao)
        if not transporte: return

        data = self._ler_data()
        ref_cliente = input("Informe a referência do cliente (ou 0 para N/A): ")
        if ref_cliente == "0": ref_cliente = "N/A"

        try:
            emb = self.sistema.criar_embarque(tipo_operacao, cliente, transporte, data, ref_cliente)
            print(f"\n Embarque Registrado com Sucesso: {emb.referencia}")
        except ValueError as e:
            print(f"Erro: {e}")

    def menu_exibir(self):
        embarques = self.sistema.obter_todos_embarques()
        if not embarques:
            print("\n Nenhum embarque registrado.")
            return

        print("\n" + "="*85)
        print(f"{'Referência':<15} | {'Data':<12} | {'Cliente':<15} | {'Tipo':<10} | {'Ref. Cli':<15}")
        print("-" * 85)
        
        for e in embarques:
            data_fmt = datetime.datetime.strptime(e.data_registro, "%Y-%m-%d").strftime("%d/%m/%Y")
            tipo_abrev = e.tipo_operacao[0] + e.transporte[0]
            print(f"{e.referencia:<15} | {data_fmt:<12} | {e.cliente_nome:<15} | {tipo_abrev:<10} | {e.ref_cliente:<15}")
        print("="*85 + "\n")

    def menu_gerenciar(self):
        self.menu_exibir()
        ref = input("Digite a Referência para gerenciar (ou 0 para sair): ").upper()
        if ref == "0": return

        emb = self.sistema.buscar_embarque(ref)
        if not emb:
            print("❌ Referência não encontrada.")
            return

        print(f"\nSelecionado: {emb}")
        print("1 - Editar Ref. Cliente\n2 - Excluir\n0 - Cancelar")
        op = input("Opção: ")

        if op == "1":
            nova = input("Nova Referência do Cliente: ")
            self.sistema.editar_ref_cliente(ref, nova)
            print("✅ Atualizado.")
        elif op == "2":
            conf = input(f"Tem certeza que deseja excluir {ref}? (S/N): ").upper()
            if conf == "S":
                self.sistema.excluir_embarque(ref)
                print("🗑️ Embarque excluído.")

    def executar(self):
        while True:
            print("\n=== 🚢 SISTEMA DE EMBARQUES (POO) ===")
            print("1 - Nova Importação")
            print("2 - Nova Exportação")
            print("3 - Exibir Tudo")
            print("4 - Gerenciar (Editar/Excluir)")
            print("0 - Sair")
            
            opcao = input("Opção: ")
            
            if opcao == "1": self.menu_novo_registro("Importação")
            elif opcao == "2": self.menu_novo_registro("Exportação")
            elif opcao == "3": self.menu_exibir()
            elif opcao == "4": self.menu_gerenciar()
            elif opcao == "0": 
                print("Saindo... 👋")
                break
            else:
                print("Opção inválida.")

# --- Execução ---
if __name__ == "__main__":
    app = InterfaceConsole()
    app.executar()
