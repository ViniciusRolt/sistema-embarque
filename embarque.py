class Embarque:
    """Representa um registro de embarque individual."""
    def __init__(self, referencia, tipo_operacao, cliente_nome, transporte, data_registro, ref_cliente):
        self.referencia = referencia
        self.tipo_operacao = tipo_operacao
        self.cliente_nome = cliente_nome
        self.transporte = transporte
        self.data_registro = data_registro
        self.ref_cliente = ref_cliente

    def __str__(self):
        return f"{self.referencia} | {self.cliente_nome} ({self.transporte})"
