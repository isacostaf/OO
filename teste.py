from make.produto import Produto
from make.usuario import Usuario
from doit.listauser import Listauser
from doit.listaproduto import Lista

nomezin = input("nomezin:")
senhazin = input("senha:")

user = Usuario(nomezin, senhazin, 0)

listauser = Listauser()
listauser.inserir(user)
listauser.imprimir()

#inputs produto
name = input("Name:")
quantity = input("Quantity:")
category = input("Category:")

#dizemos que product é um Produto e dizemos seus atributos
product = Produto(name, quantity, category)

#inputs produto
name2 = input("Name:")
quantity2 = input("Quantity:")
category2 = input("Category:")

#dizemos que product2 é um Produto e dizemos seus atributos
product2 = Produto(name2, quantity2, category2)

#dizemos que lista é do tipo classe Lista
#nesse momento é criado uma listinha em branco
lista = Lista()

#adicionamos o product na listinha
lista.inserir(product)

#adicionamos o product2 na listinha
lista.inserir(product2)

#imprimimos lista
lista.imprimir()