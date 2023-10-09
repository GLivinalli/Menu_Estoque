import estoque_base
import menu
estoque_now = {}
def cls():
    print("\033[H\033[J")

def att_banco(estoque_now=""):
     
        estoque_base.estoque.update(estoque_now)
        
        with open("estoque_base.py", "w") as arquivo:
            novo_conteudo = f'estoque = {estoque_base.estoque}\n'
            arquivo.write(novo_conteudo)

def prod_info(id, prod, valor, quant):
        id = str(id)
        prod = str(prod.lower())
        valor = float(valor)
        quant = int(quant)
        estoque_now[id] = {"Produto": prod, "Valor": valor, "Quantidade": quant}
        att_banco(estoque_now)

def add_prod():
        cls()
        try:
            id = input("ID do Produto: ")
            cls()
            if id in estoque_base.estoque:
                cls()
                print("Já exite esse ID!")
                menu.menu_inicial()
                
            else:
                print("ID:", id)
                prod = str(input("Nome do Produto: "))
                for x, sub_dic in estoque_base.estoque.items():
                    if prod in sub_dic.values():
                        cls()
                        print("Já existe esse nome de produto!")
                        menu.menu_inicial()
                
                    else:
                        cls()
                        print("- ID: {}\n- Produto: {}".format(id, prod))
                        valor = input("Valor: ")

                        cls()
                        print("- ID: {}\n- Produto: {}\n- Valor: {}".format(id, prod, valor))
                        quant = input("Quantidade: ")
                        
                        cls()
                        print("- ID: {}\n- Produto: {}\n- Valor: {}\n- Quantidade: {}".format(id, prod, valor, quant))
                        print(f"Produto {prod} adicionado ao estoque.")

        except ValueError:
            cls()
            print("Voltando...")
            menu.menu_inicial()
        
        prod_info(id, prod, valor, quant)        
        menu.menu_inicial()

def modificar_estoque():
        cls()  
        escolha_prod = str(input("Coloque o ID do produto a ser editado: ")).lower()
        cls()
        if escolha_prod in estoque_base.estoque:
            print("Escolha as opções para editar o produto {}".format(estoque_base.estoque[escolha_prod]["Produto"]))
            editar = input("""
                           
        (1) - Nome.
        (2) - ID.
        (3) - Valor.
        (4) - Quantidade.
        (5) - Apagar Produto.
        (6) - Voltar.
                           
        """)
        
            if editar == "1":
                escolha = input("Novo nome para o Produto: ")

                if escolha in estoque_base.estoque:
                    print("Já existe esse Produto!")


                else:
                    estoque_base.estoque[escolha_prod]["Produto"] = escolha
                    att_banco()
                    menu.menu_inicial()

            elif editar == "2":
                escolha = input(str("Novo ID do Produto: "))
                estoque_base.estoque[escolha] = estoque_base.estoque.pop(escolha_prod) 
                att_banco()
                menu.menu_inicial()    

            elif editar == "3":
                escolha = input("Novo Valor do Produto: ")
                estoque_base.estoque[escolha_prod]["Valor"] = float(escolha)
                att_banco()
                menu.menu_inicial()
                
            elif editar == "4":
                escolha = input("Novo Quantidade do Produto: ")
                estoque_base.estoque[escolha_prod]["Quantidade"] = int(escolha)
                att_banco()
                menu.menu_inicial()


            elif editar == "5":
                del estoque_base.estoque[escolha_prod]
                att_banco()
                menu.menu_inicial()

            elif editar == "6":
                 cls()
                 menu.menu_inicial()
        else:
             cls()
             menu.menu_inicial()


def verificar_estoque():
    cls()
    entrada = input("""
                    
        (1) - Verificar os informações sobre o produto.
        (2) - Listar todos os produtos cadastrados.
        (3) - Voltar.
                    
                    """)
    cls()   
    if entrada == "1":
        cls()

        entrada = input("ID do produto desejado: ")
        print("""
              
        - ID: {}
        - Produto: {}
        - Valor: R$ {} 
        - Quantidade: {}"""
              
        .format(entrada, estoque_base.estoque[entrada]["Produto"], estoque_base.estoque[entrada]["Valor"], estoque_base.estoque[entrada]["Quantidade"]))
        
        menu.menu_inicial()

    elif entrada == "2":
        for x in estoque_base.estoque:
            print("""
                  
        - ID: {}
        - Produto: {}
        - Valor: R$ {} 
        - Quantidade: {}"""
                  
        .format(x, estoque_base.estoque[x]["Produto"], estoque_base.estoque[x]["Valor"], estoque_base.estoque[x]["Quantidade"]))
            
        menu.menu_inicial()

    elif entrada == "3":
        cls()
        menu.menu_inicial()
