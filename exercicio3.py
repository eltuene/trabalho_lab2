import json

class listaContatos:
    def __init__(self, file_name):
        self.contatos = {}
        self.file_name = file_name
        self.carregar_contatos()
    
    def add_contato(self, nome, telefone, email):
        self.contatos[nome] = {"telefone": telefone, "email": email}
        
    def remove_contato(self, nome):
        del self.contatos[nome]
        
    def show_contatos(self):
        print(self.contatos)
        
    def buscar_contatos(self):
        nome = input("Digite o nome do contato: ")
        for contato in self.contatos:
            if contato["nome"] == nome:
                print(contato)
                return
        print("Contato não encontrado.")
    
    def salvar_contatos(self):
        with open(self.file_name, "w") as file:
            json.dump(self.contatos, file)
            
    def carregar_contatos(self):
        with open(self.file_name, "r") as file:
            self.contatos = json.load(file)
            
if __name__ == "__main__":
    lista = listaContatos("contatos.json")
    lista.add_contato("João", "912345678", "joao@email.com")
    lista.add_contato("Maria", "987654321", "maria@email.com")
    lista.show_contatos()
    lista.salvar_contatos()
    