from embarque import Embarque

class SistemaGerenciador:
    def __init__(self):
        self.embarques = {}
        self.contador = 0
        self.ano_atual = "26"
        self.clientes = {
            "1": "Signode",
            "2": "Starrett",
            "3": "Interbrilho",
            "4": "Radio Holland",
            "5": "Starrett MG",
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
