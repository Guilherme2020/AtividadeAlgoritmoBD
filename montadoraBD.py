from os import system
import platform
import veiculosBD

def main(): 
    cadastro = []
    cont_cadastro = 0
    cont = 0
    while True:
        print("***** MONTADORA *****")
        print("1 - Adicionar Montadora\n2 - Listar Montadora\n"
              "3 - Remover Montadora\n4 - Editar Montadora\n"
              "5 - Importar Cadastro\n0 - Sair")
        funcao = input("Opcao >> ")
        if funcao == "1":
            cadastro.append(cadastro_montadora())
        elif funcao == "2":
            listar_montadora(cadastro)
        elif funcao == "3":
            remover_montadora(cadastro)
        elif funcao == "4":
            editar_montadora()
        elif funcao == "5":
            cont = 1
            cadastro += importar_montadora()    	           	    	        
        elif funcao == "0":
            sair(cadastro,cont)
            break
        else:
            print("\nERROR XXXD\n")

def limpar_tela():
    if platform.system() == "Linux":
        system("clear")
    elif platform.system() == "Windows":
        system("cls")

def cadastro_montadora():
    limpar_tela()
    arquivo = open("montadora/importMont.txt", "r")
    
    if arquivo.readlines() == "":
        id_cadastro = cont_cadastro
    else:
        arquivo = open("montadora/importMont.txt", "r")
        id_cadastro = int(eval(arquivo.readline()).get("id")) + 1
    
    nome = input("Nome: ")
    country = input("Country: ")
    return {"id" : str(id_cadastro) , "Nome" : nome ,"Country" : country}

def listar_montadora(cadastro):
    limpar_tela()
    print("\n### Lista de Montadora ###\n1 - Listar todas\n2 - Listar nome\n3 - Listar contry")
    listar = input("opcao >> ")
       
    for i in range(len(cadastro)):
        if listar == "1":
            print("Id: " + cadastro[i].get("id") + "| Nome: " + cadastro[i].get("Nome")+ "| Country: " + cadastro[i].get("Country").upper())
        elif listar == "2":
            nome = input("Digite nome: ")
            for i in range(len(cadastro)):
                if nome == cadastro[i].get("Nome"):
                    print("Id: " + cadastro[i].get("id") + "| Nome: " + cadastro[i].get("Nome")+ "| Country: " + cadastro[i].get("Country").upper())
        elif listar == "3":
            country = input("Digite country: ")
            for i in range(len(cadastro)):
                if country == cadastro[i].get("Country"):
                    print("Id: " + cadastro[i].get("id") + "| Nome: " + cadastro[i].get("Nome")+ "| Country: " + cadastro[i].get("Country").upper())
        else:
            print("Opcao invalida\n")

    print("\n\n")
            
def remover_montadora(cadastro):
    limpar_tela()
    remover = input("Nome da Montadora que deseja remover: ")
    for i in range(len(cadastro)):
        if remover == cadastro[i].get("Nome"):
            item_removido = cadastro.pop(i)
    print("Montadora "+ item_removido.get("Nome")+" removida com sucesso")

def editar_montadora(cadastro):
    limpar_tela()
    editar = input("Nome da Montadora que deseja editar: ")

    for i in range(len(cadastro)):
        if editar == cadastro[i].get("Nome"):
            Id = cadastro[i].get("id")
            cadastro.pop(i)
            cadastro.insert(i, {"id" : str(Id) , "Nome" : input("Novo nome: ") ,"Country" : input("Novo country: ")})

def importar_montadora():
    limpar_tela()
    arquivo = open("montadora/importMont.txt", "r")
    cadastro = []
    
    for i in arquivo.readlines():
        cadastro.append(eval(i))
    
    return cadastro
    

def sair(cadastro,cont):
    limpar_tela()
    if cont != 1:
        cadastro += importar_montadora()
        
    arquivo = open("montadora/Montadoras.txt", "w")
    arquivo_importar = open("montadora/importMont.txt", "w")

    for i in cadastro:
        arquivo.write("id: " + i.get("id") + " Nome: " + i.get("Nome") +
                      " Country: " + i.get("Country") + "\n")
        arquivo_importar.write(str(i)+"\n")
        
    arquivo.close()
    arquivo_importar.close()


    
if __name__ == "__main__":
    main()







    
