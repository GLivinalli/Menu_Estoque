#!/bin/python3

import estoque_caf

def menu_inicial():
    escolha = input(("""
        Estoque da Cafeteria.\n
        (1) Adicionar Produto.
        (2) Verificar Estoque.
        (3) Modificar o Estoque.
    """))
    if escolha == "1":
        estoque_caf.add_prod()
    elif escolha == "2":
        estoque_caf.verificar_estoque()
    elif escolha == "3":
        estoque_caf.modificar_estoque()
    elif escolha != ("1","2","3"):
        print("Saindo...")
        quit

if __name__ == "__main__":
    estoque_caf.cls()
    menu_inicial()
