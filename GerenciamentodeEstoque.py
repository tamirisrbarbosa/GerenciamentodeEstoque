# ==========================
# Estrutura de Dados
# ==========================

# Classe que representa um produto no estoque
class Produto:
    def __init__(self, id_produto, nome, categoria, quantidade, preco, localizacao):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

# Classe que representa uma movimentação de entrada ou saída de um produto
class Movimentacao:
    def __init__(self, id_produto, tipo, quantidade, data):
        self.id_produto = id_produto
        self.tipo = tipo  # Tipo da movimentação: 'entrada' ou 'saida'
        self.quantidade = quantidade
        self.data = data

# ==========================
# Banco de dados em memória
# ==========================

# Lista que armazena todos os produtos cadastrados
produtos = []

# Lista que armazena todas as movimentações registradas
movimentacoes = []

# ==========================
# Funções principais
# ==========================

# Função para cadastrar um novo produto
def cadastrar_produto(id_produto, nome, categoria, quantidade, preco, localizacao):
    produtos.append(Produto(id_produto, nome, categoria, quantidade, preco, localizacao))
    print(f"Produto {nome} cadastrado")

# Função para consultar um produto pelo ID
def consultar_produto(id_produto):
    for produto in produtos:
        if produto.id_produto == id_produto:
            return vars(produto)  # Retorna o dicionário com os atributos do produto
    print("Produto não encontrado.")
    return None

# Função para registrar movimentações de entrada ou saída no estoque
def registrar_movimentacao(id_produto, tipo, quantidade, data):
    produto = next((p for p in produtos if p.id_produto == id_produto), None)
    
    # Verifica se o produto existe
    if not produto:
        print("Produto não encontrado.")
        return
    
    # Verifica se há quantidade suficiente no caso de saída
    if tipo == "saida" and produto.quantidade < quantidade:
        print("Estoque insuficiente.")
        return

    # Registra a movimentação e atualiza a quantidade no estoque
    movimentacoes.append(Movimentacao(id_produto, tipo, quantidade, data))
    produto.quantidade += quantidade if tipo == "entrada" else -quantidade
    print(f"Movimentação de {tipo} registrada para {produto.nome}.")

# Função que gera um relatório simples com os dados dos produtos
def gerar_relatorio():
    return [
        {
            "id": p.id_produto,
            "nome": p.nome,
            "quantidade": p.quantidade,
            "localizacao": p.localizacao
        }
        for p in produtos
    ]

# Função para consultar o histórico de movimentações de um produto específico
def consultar_historico(id_produto):
    historico = [vars(m) for m in movimentacoes if m.id_produto == id_produto]
    if not historico:
        print("Nenhuma movimentação registrada.")
    return historico

# ==========================
# Exemplo de uso
# ==========================

# Cadastro de um produto
cadastrar_produto(1, "Produto A", "Categoria 1", 50, 10.99, "Depósito A")

# Consulta do produto cadastrado
print(consultar_produto(1))

# Registro de movimentações: saída e entrada
registrar_movimentacao(1, "saida", 10, "2025-03-31")
registrar_movimentacao(1, "entrada", 20, "2025-04-01")

# Geração do relatório de produtos
print(gerar_relatorio())

# Consulta do histórico de movimentações do produto
print(consultar_historico(1))
