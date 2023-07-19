from make.usuario import Usuario

#vamos criar uma lista de usuarios
class Listauser:
    def __init__(self):
        self.listinhauser = []
        
    def inserir(self, usuario):
        self.listinhauser.append(usuario)
        
    def remover(self, usuario):
        self.listinhauser.remove(usuario)
        
    def imprimir(self):
        for p in self.listinhauser:
            print(p.nome)
            print(p.senha)
            print(p.prioridade)
            
