from exercicio2 import ListaCompras

def test_add_item():
    lista = ListaCompras()
    lista.add_item("ovo", 3)
    lista.add_item("feijao", 10)
    assert lista.lista == {'ovo': 3, 'feijao': 10}
    
def test_remove_item():
    lista = ListaCompras()
    lista.add_item("ovo", 3)
    lista.add_item("feijao", 10)
    lista.remove_item("ovo")
    assert lista.lista == {'feijao': 10}
    
def test_preco_items():
    lista = ListaCompras()
    lista.add_item("ovo", 3)
    lista.add_item("feijao", 10)
    assert lista.preco_items() == 13
