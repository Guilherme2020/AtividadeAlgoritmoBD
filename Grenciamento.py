import veiculosBD
import montadoraBD

def main():
    while True:
        print("Banco de dados:\n1 - Veiculos:\n2 - Montadoras:\n0 - Sair ")
        bd = input("Opcao >> ")

        if bd == "1":
            veiculosBD.main()
        elif bd == "2":
            montadoraBD.main()
        else:
            break
    

    
if __name__ == "__main__":
    main()
