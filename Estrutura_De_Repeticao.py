


#ex 01
def ex01():
    while True:
        nota = float(input("INSIRA UMA NOTA ENTRE ZERO E DEZ: "))
        if 0<=nota<=10:
            print(f"A nota é {nota}")
            break
        else:
            print("VALOR INVALIDO! \n\n")

#ex 02

def ex02():
    while True:
        usuario = str(input("Insira um nome de usuário: "))
        senha = str(input("Insira uma senha: "))

        if usuario == senha:
            print("A SENHA E O USUARIO DEVEM SER DISTINTOS")
        else:
            break

    print(usuario,'\n', senha)

#ex 03

def ex03():
    while True:
        nome = str(input("Insira o nome: "))
        if len(nome) >= 3:
            break
        else:
            print(f"{nome} é um valor invalido")

    while True:
        idade = int(input("Insira a idade: "))
        if 0<idade<150:
            break
        else:
            print(f"{idade} é um valor invalido")

    while True:
        salario = float(input("Insira o salario: "))
        if salario>0:
            break
        else:
            print(f"{salario} é um valor invalido")

    generos = ('f', 'm', 'i', 'o')  # tupla =(feminino, masculino, intersex, outros)
    while True:
        genero = str(input("Insira o genero: "))
        if genero in generos:
            break
        else:
            print(f"{genero} é um valor invalido")

    ecivil = ('s', 'c', 'v', 'd')  # tupla = (solteiro, casado, viuvo, divorciado)
    while True:
        estado_civil = str(input("Insira o estado civil: "))
        if estado_civil in ecivil:
            break
        else:
            print(f"{estado_civil} é um valor invalido")

    return print("""Informações inseridas e validadas:
    NOME: {}
    IDADE: {}
    SALARIO: {}
    GENERO: {}
    ESTADO CIVIL: {}
    """.format(nome,idade,salario,genero,estado_civil))

#ex 04:
def ex04():
    a, ta = 8000, 0.03
    b, tb = 20000, 0.015

    anos = 0
    while not a>=b:
        anos += 1
        a += a*ta
        b += b*tb

    return print(f"{anos} anos são necessários para que A ultrapasse ou iguale a B em população")

#ex 05:
def ex05():
    def ex04():
        while True:
            a, ta = int(input("Insira a população da cidade A: ")), float(input("Insira a taxa de crescimento de A em %: "))
            b, tb = int(input("Insira a população da cidade B: ")), float(input("Insira a taxa de crescimento de B em %: "))
            ta,tb = ta/100, tb/100

            anos = 0
            while not a >= b:
                anos += 1
                a += a * ta
                b += b * tb

            print(f"{anos} anos são necessários para que A ultrapasse ou iguale a B em população\n")

            if (input("Digite [0] para sair da repetição: ")) == '0':
                break
        return


#ex 06:
def ex06():
    for i in range(1,21):
        print(i, end=' ')
        #utilizando o end= é possivel difinil o que estará no final da linha de impressao
        #quando end = está vazia o python3 ja interpretará como end='\n'

#ex 07:
def ex07():
    lista =[]
    for i in range(5):
        x = float(input())
        lista.append(x)

    return print("O maior numero é: {}".format(max(lista)))

#ex 08:
def ex08():
    soma = 0.0
    for i in range(5):
        soma += float(input())
    media = soma/5
    return print("SOMA = {}\nMEDIA = {}".format(soma,media))

#ex 09:
def ex09():
    lista = []
    for i in range(1,51):
        if i % 2 !=0:
            lista.append(i)

    for n in lista:
        print(n, end=' ')
    return

#ex 10:
def ex10():
    a = int(input("A: "))
    b = int(input("B: "))
    lista = []
    if a>b:
        for i in range(a,(b+1)):
            print(i, end=' ')
    elif b>a:
        for i in range(b, (a+1)):
            print(i, end=' ')
    else:
        print("A e B são identicos, não há algum número compreendido entre eles")

#ex 11:
def ex11():
    a = int(input("A: "))
    b = int(input("B: "))
    soma = 0
    if a > b:
        for i in range(a, (b + 1)):
            print(i, end=' ')
            soma += i
    elif b > a:
        for i in range(b, (a + 1)):
            print(i, end=' ')
            soma += i
    else:
        print("A e B são identicos, não há algum número compreendido entre eles")

    print("A SOMA É: {}".format(soma))

#ex 12:
def ex12():
    pass

#ex 13:
def ex13():
    pass

#ex 14:
def ex14():
    pass

#ex 15:
def ex15():
    pass

#ex 16:
def ex16():
    pass

#ex 17:
def ex17():
    pass

#ex 18:
def ex18():
    pass

#ex 19:
def ex19():
    pass

#ex 20:
def ex20():
    pass

#ex 21:
def ex21():
    pass

#ex 22:
def ex22():
    pass

#ex 23:
def ex23():
    pass

#ex 24:
def ex24():
    pass

#ex 25:
def ex25():
    pass

#ex 26:
def ex27():
    pass

#ex 28:
def ex28():
    pass

#ex 29:
def ex29():
    pass

#ex 30:
def ex30():
    pass

#ex 31:
def ex31():
    pass

#ex 32:
def ex32():
    pass

#ex 33:
def ex33():
    pass

#ex 34:
def ex34():
    pass

#ex 35:
def ex35():
    pass

#ex 36:
def ex37():
    pass

#ex 38:
def ex38():
    pass

#ex 39:
def ex39():
    pass

#ex 40:
def ex40():
    pass

#ex 41:
def ex41():
    pass

#ex 42:
def ex42():
    pass

#ex 43:
def ex43():
    pass

#ex 44:
def ex44():
    pass

#ex 45:
def ex45():
    pass

#ex 46:
def ex46():
    pass

#ex 47:
def ex47():
    pass

#ex 48:
def ex48():
    pass

#ex 49:
def ex49():
    pass

#ex 50:
def ex50():
    pass

#ex 51:
def ex51():
    pass
