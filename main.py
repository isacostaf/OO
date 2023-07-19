from make.produto import Produto
from make.usuario import Usuario
from doit.listauser import Listauser
from doit.listaproduto import Lista
from doit.jlistuser import Criandouser
import json

if __name__ == "__main__":
    # DECLARAMOS O ARQUIVO
    json_file_user = "/Users/isabellecosta/Documents/Bcode/OO/ProjetoFinal/data/user.json"
    
    with open(json_file_user) as usersfile:
        userlist = json.load(usersfile)
        
    createuser = Criandouser(userlist,json_file_user)
    createuser.criar()