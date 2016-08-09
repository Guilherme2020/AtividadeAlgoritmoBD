from os import system
import platform
import montadoraBD

def main():
    cadastro = []
    cont_cadastro = 0
    cont = 0
    while True:
        limpar_tela()
        print("***** Veiculos *****")
        print("1 - Adicionar Veiculo\n2 - Listar Veiculos\n"
              "3 - Remover Veiculos\n4 - Editar Veiculos\n"
              "5 - Importar Cadastro\n0 - Sair")
        funcao = input("Opcao >> ")
        if funcao == "1":
            cont_cadastro += 1
            cadastro.append(cadastro_veiculos(cont_cadastro))
        elif funcao == "2":
            listar_veiculos(cadastro)
        elif funcao == "3":
            remover_veiculo(cadastro)
        elif funcao == "4":
            editar_veiculo(cadastro)
        elif funcao == "5":
            cont = 1
            cadastro += importar_veiculo()
       
        elif funcao == "0":
            sair(cadastro, cont)
            break
        else:
            print("\nERROR XXXD\n")

def limpar_tela():
    if platform.system() == "Linux":
        system("clear")
    elif platform.system() == "Windows":
        system("cls")



def cadastro_veiculos(cont_cadastro):
    limpar_tela()
    arquivo = open("veiculo/importVei.txt", "r")
    
    if arquivo.readline() == "":
        id_cadastro = cont_cadastro     
    else:
        arquivo = open("veiculo/importVei.txt", "r")
        id_cadastro = int(eval(arquivo.readline()).get("id")) + 1
    

    nome = input("Nome: ")
    valor = input("Valor: ")
    ano = input("Ano: ")
    print("## Lista de Montadoras ##")
    [print("ID",a.get("id"),"=",a.get("Nome")) for a in montadoraBD.importar_montadora()]
    montadora_id = input("Digite ID referente a sua montadora: ")
    
    for i in montadoraBD.importar_montadora():
        if montadora_id == i.get("id"):
            montadora_nome = i.get("Nome")
    
    return {"id" : str(id_cadastro) , "Nome" : nome , "Valor" : valor,
            "Ano" : ano, "Montadora" : montadora_nome}

def listar_veiculos(cadastro):
    limpar_tela()
    print("\n### Listar de Veiculos ###\n1 - Listar Todos\n2 - Listar por Nome\n3 - Listar por Montadora"
        "\n4 - Listar por Ano\n5 - Listar por Valor")
    listar = input("opcao >> ")
    for i in range(len(cadastro)):
        if listar == "1":
            print("Id: " , cadastro[i].get("id") , "| Nome: " , cadastro[i].get("Nome")+ "| Valor: " , cadastro[i].get("Valor") , "| Ano:",
                   cadastro[i].get("Ano") , "| Montadora: " , cadastro[i].get("Montadora"))
        elif listar == "2":
            nome = input("Digite nome: ")
            for i in range(len(cadastro)):
                if nome == cadastro[i].get("Nome"):
                    print("Id: " , cadastro[i].get("id") , "| Nome: " + cadastro[i].get("Nome"), "| Valor: " , cadastro[i].get("Valor") , "| Ano:",
                           cadastro[i].get("Ano") , "| Montadora" , cadastro[i].get("Montadora"))
        elif listar == "3":
            montadora = input("Digite nome Montadora : ")
            for i in range(len(cadastro)):
                if montadora == cadastro[i].get("Montadora"):
                    print("Id: " , cadastro[i].get("id") , "| Nome: " , cadastro[i].get("Nome"), "| Valor: " , cadastro[i].get("Valor") , "| Ano:",
                           cadastro[i].get("Ano") , "| Montadora: " , cadastro[i].get("Montadora"))
        elif listar == "4":
            ano = int(input("Digite ano: "))
            print("Lista de carros ate o ano de %d:" % ano)
            for i in range(len(cadastro)):
                if ano >= int(cadastro[i].get("Ano")):
                    print("Id: " , cadastro[i].get("id") , "| Nome: " , cadastro[i].get("Nome"), "| Valor: " , cadastro[i].get("Valor") , "| Ano:",
                           cadastro[i].get("Ano") , "| Montadora: " , cadastro[i].get("Montadora"))
        elif listar == "5":
            valor = int(input("Valor: "))
            print("Lista de carros de valores menores iguais a %d:")
            for i in range(len(cadastro)):
                if valor >= int(cadastro[i].get("Valor")):
                    print("Id: " , cadastro[i].get("id") , "| Nome: " , cadastro[i].get("Nome"), "| Valor: " , cadastro[i].get("Valor") , "| Ano:",
                           cadastro[i].get("Ano") , "| Montadora: " , cadastro[i].get("Montadora"))
        else:
            print("Opcao invalida\n")
              
            
    print("\n\n")
            
def remover_veiculo(cadastro):
    limpar_tela()
    remover = input("Nome da Montadora que deseja remover: ")
    for i in range(len(cadastro)):
        if remover == cadastro[i].get("Nome"):
            item_removido = cadastro.pop(i)
    print("Veiculo "+ item_removido.get("Nome")+" removida com sucesso")

def editar_veiculo(cadastro):
    limpar_tela()
    editar = input("Nome da Montadora que deseja editar: ")

    for i in range(len(cadastro)):
        if editar == cadastro[i].get("Nome"):
            Id = cadastro[i].get("id")
            cadastro.pop(i)
            cadastro.insert(i, {"id" : str(Id) , "Nome" : input("Novo nome: ") ,"Valor" : input("Novo valor: "),
                                "Ano" : input("Novo ano: "),"Montadora" : input("Nova montadora: ")})

def importar_veiculo():
    limpar_tela()
    arquivo = open("veiculo/importVei.txt", "r")
    cadastro = []
    
    for i in arquivo.readlines():
        cadastro.append(eval(i))
      
    return cadastro
    

def sair(cadastro, cont):
    limpar_tela()
    if cont != 1:
        cadastro += importar_veiculo()
        
    arquivo = open("veiculo/Veiculo.txt", "w")
    arquivo_importar = open("veiculo/importVei.txt", "w")
       
    
    for i in cadastro:
        print(i) 
        arquivo.write("id: " + i.get("id") + " Nome: " + i.get("Nome") +
                      " Valor: " + i.get("Valor") + " Ano: " + i.get("Ano") + " Montadora: " + i.get("Montadora")+"\n")
        arquivo_importar.write(str(i)+"\n")
        
    arquivo.close()
    arquivo_importar.close()

if __name__ == "__main__":
    main()







    
