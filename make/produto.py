class Produto:
#definimos o que vai ser um produto
    
    #deinimos o que um produto vai ter
    # nome, quantidade, categoria
    def __init__(self, nome, quantidade, categoria):
        self.nome = nome
        self.quantidade = quantidade
        self.categoria = categoria
        