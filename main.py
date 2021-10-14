def show_menu():
    print("1. Citire lista")
    print("2. Afisarea tuturor numerelor intregi")
    print("3. Afisarea celui mai mare numar divizibil de la tastatura")
    print("4. Afisarea float-urilor a caror  parte fractionara este palindrom")
    print("5. Afișarea lst obț din lista inițială în care float-urile cu partea întreagă a radicalului număr prim sunt puse ca string-uri cu caracterele în ordine inversă.")
    print("6. Exit")


def read_list():
    floats = []
    float_as_str = input ("Introduceti numerele prin spatiu:")
    float_as_str_split = float_as_str.split(' ')
    for num_str in float_as_str_split:
        floats.append(float(num_str))
    return floats


def get_integers(lst):
    """
    determina numerele intregi din lista
    param intrare: lista de floaturi
    param iesire: lista de nr care verifica conditia
    """
    lista=[]
    for i in lst:
        if i == int(i):
            lista.append(i)
    return lista


def test_get_integers():
    assert get_integers([12, 4.7, 9.8, 4 ]) == [12, 4]
    assert get_integers([]) == []
    assert get_integers([67, 89.9, 34.5, 23.6, 12.6]) == [67]


def get_max_div(lst, k):
    """
    Determina maximul din lista care se divide la un nr citit de la tastatura
    param intrare: lista de floaturi, nr intreg k
    param iesire: maximul intreg
    """
    result=None
    for i in lst :
        if int(i) == i and i % k ==0 :
            if result is None:
                result = int(i)
            else:
                result=max(result, i)
    return result


def show_max_div(lst):
    k=int(input("introduceti nr pt verificarea divizibilitatii: "))
    result = get_max_div(lst,k)
    print( f'Numarul maxim div cu {k} este {result}')

def test_get_max_div():
    assert get_max_div([12.4, 78.1, 3, 9],3) == 9
    assert get_max_div([15.7, 8.9, 12, 55],11) == 55
    assert get_max_div([19, 45.7, 18.99, 38], 19) == 38


def get_with_decimals_palindromes(lst):
    """
    determina nr ale caror parte fractionara este palindrom
    param intrare:lista de floaturi
    return: lista de nr care respecta conditia
    """
    result = []
    for elem in lst:
        str_elem= str(elem)
        if ('.') in str_elem:
            decimals = str_elem.split('.')[1]
            if decimals == decimals[::-1] :
                result.append(elem)
    return result

    

def test_get_with_decimals_palindromes():
    assert get_with_decimals_palindromes([12.13, 56.77, 12, 9.989 ]) == [56.77, 9.989]
    assert get_with_decimals_palindromes([15.78, 98.9, 12.34]) == [98.9]
    assert get_with_decimals_palindromes([1.57, 89.565, 1.0 ]) == [89.565, 1.0]


def show_with_decimals_palindromes(lst):
    result = get_with_decimals_palindromes(lst)
    print(f'Numerele a caror parte fractionara este palindrom sunt {result}')

def is_primes(x):
    """
    determina daca un nr este prim
    param : nr intreg
    return: True daca este prim sau False daca nu este
    """
    if x <= 1:
        False
    else:
        for i in range(2,x-1):
            if x % i == 0:
                return False
    return True

def test_is_primes():
    assert is_primes(7) ==True
    assert is_primes(18) == False
    assert is_primes(17) == True


def get_processing_nr(lst):
    """
    determina daca float-urile cu partea întreagă a radicalului număr prim 
    sunt puse ca string-uri cu caracterele în ordine inversă
    param: lista de float-uri
    return : lista rezultat
    """
    result =[]
    for elem in lst:
        if elem >= 0:
            int_sqrt = int(elem ** 0.5)
            if is_primes(int_sqrt):
                result.append(str(elem)[::-1])
            else:
                result.append(elem)
    return result



def test_get_processing_nr():
    assert get_processing_nr([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]
    assert get_processing_nr([]) == []


def main():
    lst=[]
    while True:
        show_menu()
        opt=int(input("Introduceti optiunea: "))
        if opt == 1:
            lst = read_list()
        elif opt == 2:
            print("Numerele intregi sunt: ", get_integers(lst))
        elif opt == 3:
            show_max_div(lst)
        elif opt == 4:
           show_with_decimals_palindromes(lst)
        elif opt == 5:
            result = get_processing_nr(lst)
            print(f'Noua lista in urma procesarii este : {result}')
        elif opt == 6 :
            break
        else:
            print("optiune invalida")

if __name__ == '__main__':
    test_get_integers()
    test_get_max_div()
    test_get_with_decimals_palindromes()
    test_is_primes()
    test_get_processing_nr()
    main()

