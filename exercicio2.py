class ListaCompras:
    def __init__(self):
        self.lista = {}
        
    def add_item(self, item, preco):
        if item in self.lista:
            print("Item já cadastrado.")
            return
        self.lista[item] = preco
    
    def remove_item(self, item):
        if item not in self.lista:
            print("Item não cadastrado.")
            return
        del self.lista[item]
    
    def show_items(self):
        if self.lista == {}:
            print("Nenhum item cadastrado.")
            return
        for item in self.lista:
            print(f"{item}: {self.lista[item]}")
            
    def preco_items(self):
        total = 0
        for item in self.lista:
            total += self.lista[item]
        return total
        
if __name__ == "__main__":
    lista = ListaCompras()
    lista.add_item("ovo", 3)
    lista.add_item("feijao", 10)
    lista.show_items()
    print("Total ",lista.preco_items())

    