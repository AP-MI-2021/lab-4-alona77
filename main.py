def show_menu():
    print("1. Citire lista")
    print("2. Afisarea partii intregi a fiecarui numar din lista")
    print("3. Afisarea numerelor care apartin unui interval citit de la tastura")
    print("4. Afisarea nr a caror partea intreaga este div pt partea lor fractionara")
    print("5. Inlocuire nr cu un sir de string-uri care le descriu")
    print("6. Iesire meniu")

def main():
    lst=[]
    while True:
        show_menu()
        opt=int(input("Introductei optiunea: "))
        if opt == 1:
            pass
        elif opt == 2:
            pass
        elif opt == 3:
            pass
        elif opt == 4:
            pass
        elif opt == 5:
            pass
        elif opt == 6:
            break
        else: 
            print("Optiune invalida")
    
if __name__ == '__main__':
    main()