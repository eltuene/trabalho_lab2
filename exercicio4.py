import csv

class Estoque:
    def __init__(self, file_name):
        self.produtos = []
        self.file_name = file_name
        self.carregar_produtos()
    
    def carregar_produtos(self):
        with open(self.file_name, encoding="utf-8") as file:
            produtos_reader = csv.reader(file, delimiter=",", quotechar='"')

            header = next(produtos_reader)
            self.produtos = list(produtos_reader)

    def add_produto(self, nome, preco, quantidade):
        for produto in self.produtos:
            if produto[0] == nome:
                print("Produto já cadastrado.")
                return
        self.produtos.append([nome, preco, quantidade])
    
    def atualizar_produto(self, nome, preco, quantidade):
        for produto in self.produtos:
            if produto[0] == nome:
                produto[1] = preco
                produto[2] = quantidade
                return
        print("Produto não encontrado.")
    
    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto[0] == nome:
                self.produtos.remove(produto)
                return
        print("Produto não encontrado.")
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)
            
    def salvar_produtos(self):
        with open(self.file_name, "w", encoding="utf-8", newline="") as file:
            produtos_writer = csv.writer(file)
            headers = ["Nome", "Preço", "Quantidade"]
            produtos_writer.writerow(headers)
            produtos_writer.writerows(self.produtos)

estoque = Estoque("produtos.csv")
estoque.carregar_produtos()
estoque.add_produto("Ovo", 3.0, 100)
estoque.add_produto("Arroz", 10.0, 100)
estoque.atualizar_produto("Arroz", 9.0, 100)
estoque.remover_produto("Caneta")
estoque.listar_produtos()
estoque.salvar_produtos()