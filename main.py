def show_menu():
    print("1. Citire lista")
    print("2. Afisarea partii intregi a fiecarui numar din lista")
    print("3. Afisarea numerelor care apartin unui interval citit de la tastura")
    print("4. Afisarea nr a caror partea intreaga este div pt partea lor fractionara")
    print("5. Inlocuire nr cu un sir de string-uri care le descriu")
    print("6. Iesire meniu")


def read_list():
    floats = []
    float_as_str = input ("Introduceti numerele prin spatiu:")
    float_as_str_split = float_as_str.split(' ')
    for num_str in float_as_str_split:
        floats.append(float(num_str))
    return floats

def get_integers(lst):
    """
    Afiseaza partea intreaga a nr din lista
    param intrare: lista de float-uri
    return: lista de intregi
    """
    result=[]
    for elem in lst:
        result.append(int(elem))
    return result

def test_get_integers():
    assert get_integers([1.2, 3.89, 1.0, 7.7]) == [1, 3, 1, 7]
    assert get_integers([]) == []
    assert get_integers([15.9, 28.7, 13.2]) == [15, 28, 13]

def get_elem_interval(lst, first , second):
    """
    Determina nr care apartin intervalului deschis (first, second)
    param intrare: lista floatu-uri, first capatul inferior al intervalului, iar second capatul superior
    return: lista elem care respecta conditia
    """
    result=[]
    for i in lst:
        if i > first and i < second:
            result.append(i)
    return result

def test_get_elem_interval():
    assert get_elem_interval([1.3, 2.7, 28], 1, 10) == [1.3, 2.7]
    assert get_elem_interval([5.3, 7.9, 11.6], 4, 6) == [5.3]
    assert get_elem_interval([2, 6.90, 10], 3, 4) == []


def div_intreg_fract(lst):
    """
    Determina nr a caror parte intreaga este divizor al partii fractionare
    param intrare: lista floaturi
    return:lista cu elem care respecta proprietatea
    """
    result=[]
    for elem in lst:
        elem_integer=int(elem)
        elem_str=str(elem)
        elem_str_fract=elem_str.split('.')[1]
        elem_int_fract=int(elem_str_fract)
        if elem_int_fract % elem_integer == 0:
            result.append(elem)
    return result

def test_div_intreg_fract():
    assert div_intreg_fract([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3]
    assert div_intreg_fract([]) == []
    assert div_intreg_fract([2.8, 9, 3.7]) ==[2.8]


def main():
    lst=[]
    while True:
        show_menu()
        opt=int(input("Introductei optiunea: "))
        if opt == 1:
            lst=read_list()
        elif opt == 2:
            result=get_integers(lst)
            print(f'Lista de intregi obtinuta din lista initiala este {result}')
        elif opt == 3:
            first=int(input("Introduceti marginea inferioara a intervalului: "))
            second=int(input("Introduceti marginea superioara a intervalului: "))
            result=get_elem_interval(lst, first, second)
            print(f'Numerele incluse in intervalul cerut sunt {result}')
        elif opt == 4:
            result=div_intreg_fract(lst)
            print(f'Numerele listei a caror parte intreaga divide partea fract sunt {result}')
        elif opt == 5:
            pass
        elif opt == 6:
            break
        else: 
            print("Optiune invalida")
    
if __name__ == '__main__':
    test_get_integers()
    test_get_elem_interval()
    test_div_intreg_fract()
    main()