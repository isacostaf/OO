from make.usuario import Usuario
import json


class Criandouser:
    def __init__(self, userlist, json_file_user):
        self.userlist = userlist
        self.json_file_user = json_file_user
        
    def updatejson(self):
        with open(self.json_file_user, "w") as updatefile:
            json.dump(self.userlist, updatefile, indent=4)
    
    def criar(self):
        with open(self.json_file_user) as usersfile:
            userlist = json.load(usersfile)

        name = input("nome: ")
        password = input("senha: ")
        priority = input("prioridade: ")
            
        user = Usuario(name, password, priority)
        dicionariouser = vars(user)
        
        userlist.append(dicionariouser)
        
        with open(self.json_file_user, "w") as usersfile:
            json.dump(userlist, usersfile, indent=4)
    
    def remove_user(self, nome):
        
        for user in userlist:
            if user["nome"] == nome:
                userlist.remove(user)
                self.updatejson()
                break
        
    