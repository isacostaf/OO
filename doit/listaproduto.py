from make.produto import Produto

#importamos a definicao de produto
#criamos essa classe para criar uma lista de produtos
#e para agregarmos produtos a ela e imprimirmos ela
class Lista:
    
    #criamos uma lista: listinha
    #vamos armazenar varias coisas nessa lista
    def __init__(self):
        self.listinha = []
        
    #vamos inserir em listinha
    #inserir o que??
    #decidimos isso na main pois passamos como parametro (insereproduto)
    def inserir(self, insereproduto):
        self.listinha.append(insereproduto)
        
    #vamos remover em listinha
    #remover o que??
    #decidimos isso na main pois passamos como parametro (removeproduto)
    def remover(self, removeproduto):
        self.listinha.remove(removeproduto)
        
    #vamos imprimir a lista
    def imprimir(self):
        for p in self.listinha:
            print(p.nome)
            print(p.quantidade)
            print(p.categoria)
            