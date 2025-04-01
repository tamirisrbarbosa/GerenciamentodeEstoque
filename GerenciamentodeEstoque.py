# Estrutura de Dados


class Produto:
    def __init__(self, id_produto, nome, categoria, quantidade, preco, localizacao):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

class Movimentacao:
    def __init__(self, id_produto, tipo, quantidade, data):
        self.id_produto = id_produto
        self.tipo = tipo # 'entrada' ou 'saida'
        self.quantidade = quantidade
        self.data = data

# Banco de dados em memória
produto = []
movimentacoes = []

# Cadastro de Produto
def cadastrar_produto(id_produto, nome, categoria, quantidade, preco, localizacao):
    produtos.append(Produto(id_produto, nome, categoria, quantidade, preco, localizacao))
    print(f"Produto {nome} cadastrado")

# Consulta de Produto
def consultar_produto(id_produto):
    for produto in produtos:
        if produto.id_produto == id_produto:
            return vars(produto)
        print("Produto não encontrado.")
        return None
    
# Registrar movimentação
def registrar_movimentação(id_produto, tipo, quantidade, data):
    produto = next((p for p in produtos if p.id_produto == id_produto), None)
    if not produto:
        print("Produto não encontrado.")
        return
    if tipo == "saida" and produto.quantidade < quantidade:
        print("Estoque insuficiente.")
        return
    
    movimentacoes.append(Movimentacao(id_produto, tipo, quantidade, data))
    produto.quantidade += quantidade if tipo == "entrada" else -quantidade
    print(f"Movimentação de {tipo} registrada para {produto.nome}.")

# Geração de Relatório
def gerar_relatorio():
    return [{"id": p.id_produto, "nome" : p.nome, "quantidade" : p.quantidade, "localizacao" : p.localizacao} for p in produtos]

# Histórico de Movimentações
def consultar_histórico(id_produto):
    historico = [vars(m) for m in movimentacoes if m.id_produto == id_produto]
    if not historico:
        print("Nenhuma movimentação registrada.")
    return historico

# Exemplo de uso
cadastrar_produto(1, "Produto A", "Categoria 1", 50, 10.99, "Depósito A")
print(consultar_produto(1))
registrar_movimentação(1, "saida", 10, "2025-03-31")
registrar_movimentação(1, "entrada", 20,"2025-04-01")
print(gerar_relatorio())
print(consultar_histórico(1))
