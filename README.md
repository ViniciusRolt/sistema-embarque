# 🚢 Sistema de Abertura de Embarques

Olá! Este projeto foi pensado e desenvolvido a partir de um problema real.  
Na empresa de logística, é utilizado um **caderno físico** para registrar novas referências de embarques. Sempre que um cliente solicita a abertura de um novo embarque, os colaboradores anotam:  

- Número da nova referência  
- Nome do cliente  
- Modalidade  
- Referência do cliente  
- Data de abertura  

O problema é que, muitas vezes, acabam surgindo **referências duplicadas**, gerando confusão e retrabalho.  

Para resolver essa situação, criei este sistema que **automatiza todo o processo**:  
- O colaborador insere os dados do embarque.  
- O sistema gera uma nova referência automaticamente.  
- O controle garante que **não haja duplicidade**.  

## ⚙️ Tecnologias utilizadas
- **Python** → lógica do sistema  
- **Git/GitHub** → versionamento e colaboração  

## 🚀 Como executar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/ViniciusRolt/Sistema_embarque.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd Sistema_embarque
   ```

3. Execute o programa:
   ```bash
   python3 novo_registro.py
   ```

## 📖 Funcionalidades atuais
- Registro digital de novos embarques  
- Geração automática de referências  
- Garantia de **não duplicação** de referências  
- Armazenamento organizado das informações
- Tela para o colaborador inserir a **data de abertura da referência**  
- Tela para informar a **referência do cliente**   

## 🛠 Funcionalidades em desenvolvimento
- Banco de dados para armazenar referências, permitindo que, ao abrir uma nova referência, sejam exibidas as **últimas 3 referências registradas**  

## 🗺 Roadmap do projeto
| Funcionalidade | Status |
|----------------|--------|
| Registro de novos embarques | ✅ Concluído |
| Geração automática de referências | ✅ Concluído |
| Controle de duplicidade | ✅ Concluído |
| Tela para inserir data de abertura | ✅ Concluído  |
| Tela para informar referência do cliente | ✅ Concluído  |
| Banco de dados para histórico de referências | ⏳ Em desenvolvimento |
| Consulta e reajuste de referência | ✅ Concluído  |

## 🤖 Observação
A Inteligência Artificial foi utilizada **apenas para revisar explicações e textos**, evitando gerar ou alterar o código.  

## 📜 Licença
Este projeto foi desenvolvido para fins de estudo e uso interno.  
Sinta-se livre para adaptar e melhorar conforme necessário.
