def show_menu():
    print("1. Citire lista")
    print("2. Det cea mai lunga secv cu prop ca sunt palindroame")
    print("3. Det cea mai lunga subsecv cu prop ca au acelasi nr de div")
    print("4. Exit")

def read_list():
    lst = []
    lst_str = input ("Introduceti numerele prin spatiu:")
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(float(num_str))
    return lst

def main():
    lst=[]
    while True:
        show_menu()
        opt=int(input("Introduceti optiunea: "))
        if opt == 1:
            lst = read_list()
        elif opt == 2:
            pass
        elif opt == 3:
            pass
        elif opt == 4:
            break
        else:
            print("optiune invalida")

if __name__ == '__main__':
    main()

