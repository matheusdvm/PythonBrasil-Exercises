from math import sqrt

#EX 01
def ex1():
    a,b = (float(x) for x in input().split())
    if a>b:
        return print(a)
    elif b>a:
        return print(b)
    else:
        return print("equal")

#EX 02

def ex2():
    x = float(input())
    if x >=0:
        return print("POSITIVE")
    elif x<0:
        return print("NEGATIVE")

#EX 03

def ex3():
    fm = str(input()).lower()
    if fm == "f":
        return print("F - Feminino")
    elif fm == "m":
        return print("M - Masculino")
    else:
        return print("Sexo Inválido")

#EX 04
def ex4():
    vc = str(input()).lower()
    vogais, consoantes = "aeiou", "bcdfghjklmnpqrstvwxyz"
    if vc in vogais:
        return print("VOGAL")
    elif vc in consoantes:
        return print("CONSOANTES")
    else:
        return print("OUTROS")

#ex 05
def ex5():
    n1,n2 = (float(x) for x in input().split())
    media = (n1+n2)/2
    if media==10:
        return print("aprovado com distinção".capitalize())
    elif media < 7:
        return print("Reprovado")
    elif media >= 7:
        return print("Aprovado")
    else:
        return print("Input inválido")

#ex 06  ajustar para if e elif até ex 08
def ex6():
    a,b,c = (float(x) for x in input().split())
    lista = [a,b,c]
    return print(max(lista))

#ex 07
def ex7():
    a,b,c = (float(x) for x in input().split())
    lista = [a,b,c]
    return print("MAIOR: {:.2f}\nMENOR: {:.2f}\n".format(max(lista), min(lista)))

#ex 08
def ex8():
    a,b,c = (float(x) for x in input().split())
    lista = [a,b,c]
    return print("O produto mais barato é o de valor {:.2f}".format(min(lista)))

#ex 09
def ex9():
    a,b,c = (float(x) for x in input().split())
    lista = [a,b,c]
    lista.sort(reverse=True)
    return print(lista)

#ex 10
def ex10():
    print("""Em qual turno você estuda?
M - matutino
V - vespertino
N - noturno""")
    t = str(input()).lower()
    if t == 'm':
        print("BOM DIA!")
    elif t == 'v':
        print("BOA TARDE!")
    elif t == 'n':
        print("BOA NOITE!")
    else:
        print("Valor Inválido".upper())

#ex 11
def ex11():
    salario = float(input())
    salario_anterior = salario


    #aumento
    if salario <= 280.0:
        salario += salario*0.2
        p = '20%'
    elif 280.0 < salario <= 700.0:
        salario += salario*0.15
        p = '15%'
    elif 700.0 < salario <= 1500.0:
        salario += salario*0.1
        p = '10%'
    elif salario > 1500.0:
        salario += salario*0.05
        p = '5%'
    else:
        p = '0%'

    v = salario - salario_anterior

    return print("""
    SALÁRIO ANTERIOR: {:.2f}
    COM AJUSTE SALARIAL DE {}
    VALOR DO AUMENTO: {:.2f}
    
    NOVO SALARIO: {:.2f}
    """.format(salario_anterior, p, v, salario))

#ex 12
def ex12():
    valor = float(input("Qual valor por hora?"))
    horas = int(input("Quantas horas trabalhadas?"))
    bruto = valor*horas
    sindicato = 0.03 * bruto
    fgts = 0.11 * bruto
    inss = 0.1*bruto
    if bruto <= 900:
        ir = 0.0
    elif bruto <= 1500:
        ir = bruto * 0.05
    elif bruto <= 2500:
        ir = bruto * 0.1
    elif bruto > 2500:
        ir = bruto * 0.2
    else:
        ir = 0.0

    totaldesc = (sindicato+inss + ir)
    liquido = (bruto - totaldesc)


    p_ir = int((bruto / ir) * 100)
    print("""(+) SALARIO BRUTO: ({:.2f} * {}) = {:.2f}
    (-) IR ({}%) : {:.2f}
    (-) INSS (10%) : {:.2f}
    (-) SINDICATO (3%) : {:.2f}
    (-) FGTS (10%) : {:.2f}
    (=) Total de descontos : {:.2f}
    -------------------------------
    SALÁRIO LÍQUIDO: {:.2f}""".format(valor, horas, bruto, p_ir, ir, inss, sindicato,fgts,totaldesc,liquido))


#ex 13
def ex13():
    dia = int(input())
    if dia == 1:
        return print("Domingo")
    elif dia == 2:
        return print("Segunda")
    elif dia == 3:
        return print("Terca")
    elif dia == 4:
        return print("Quarta")
    elif dia == 5:
        return print("Quinta")
    elif dia == 6:
        return print("Sexta")
    elif dia == 7:
        return print("Sabado")
    else:
        return print("VALOR INVALIDO")

#ex 14
def ex14():
    n1 = float(input("Primeira Nota Parcial: "))
    n2 = float(input("Segunda Nota Parcial: "))
    media = (n1 + n2) / 2
    if 0 <= media < 4:
        conceito = 'E'
    elif 4 <= media < 6:
        conceito = 'D'
    elif 6 <= media < 7.5:
        conceito = 'C'
    elif 7.5 <= media < 9:
        conceito = 'B'
    elif 9 <= media <= 10:
        conceito = 'A'
    else:
        conceito = -1

    if conceito in 'ABC':
        return print("APROVADO com conceito {}!\nNota 01: {:.2f}\nNota 02:{:.2f}\nMedia: {:.2f}\n".format(conceito, n1, n2, media))
    elif conceito in 'DE':
        return print("REPROVADO com conceito {}!\nNota 01: {:.2f}\nNota 02:{:.2f}\nMedia: {:.2f}\n".format(conceito, n1, n2, media))
    else:
        return print("NOTAS INVALIDAS")


#ex15
def ex15():
    l1, l2, l3 = (float(x) for x in input("Adicione os tres lados do triangulo:\n").split())
    if (l1+l2) > l3 and (l2+l3) > l1 and (l1+l3)>l2:
        #triangulo existe
        if l1==l2==l3:
            return print("O TRIANGULO É EQUILATERO")
        elif l1==l2 or l1==l3 or l2==l3:
            return print("O TRIANGULO É ISOSCELES")
        elif l1!=l2!=l3:
            return print("O TRIANGULO É ESCALENO")
    else:
        return print("OS LADOS NÃO SATISFAZEM A CONDIÇÃO DE EXISTENCIA DO TRIANGULO")

#ex16
def ex16():
    a = float(input("Adicione a variavel A da equação de 2o grau Ax2 + Bx + C\n"))
    if a == 0:
        return print("Se A = 0 a equação não é do segundo grau")

    b = float(input("Adicione a variavel B da equação: "))
    c = float(input("Adicione a variavel C na equação: "))

    delta = b**2 - 4 * a * c
    r1 = (sqrt(delta) - b) / (2 * a)
    r2 = (-sqrt(delta) - b) / (2 * a)

    if delta<0:
        return print("Delta < 0: a equação não possui valores reais")
    elif delta == 0:
        return print("Delta = 0: a equação possui apenas uma raiz\nRAIZ: {:.2f}".format(r1))
    else:
        return print("Delta > 0: a equação possui duas raizes,\n RAIZ 1: {:.2f}\nRAIZ 2: {:.2f}".format(r1,r2))

#ex17
def ex17():
    ano = int(input("Insira um ano: "))
    print("\nVerificando se é bissexto!\n\n")

    if ano%4 == 0 and ano%100 !=0:
        if ano%400 == 0:
            return print("É BISSEXTO")
        elif ano<400:
            return print("É BISSEXTO")
        else:
            return print("NÃO É BISSEXTO")
    else:
        return print("NÃO É BISSEXTO")

#OUTRA MANEIRA DE RESOLVER O EXERCICIO UTILIZANDO CALENDAR(ISLEAP)
def ex172():
    from calendar import isleap
    ano = int(input("INSIRA UM ANO: "))

    if isleap(ano):
        return print("É BISSEXTO")
    else:
        return print("NÃO É BISSEXTO")

#ex18
def ex18():
    data = str(input("insira uma data no formato DD/MM/AAAA\n"))
    dia,mes,ano = (data.split('/'))
    lista = [31,28,31,30,31,30,31,31,30,31,30,31]
    if len(dia) == 2 and len(mes) == 2 and len(ano)==4:
        dia_int,mes_int,ano_int = int(dia), int(mes), int(ano)
        if 1<=mes_int<=12 and ano_int!=0 and 1<=dia_int<=lista[mes_int-1]:
                return print("{} é uma data valida".format(data))
        else:
            return print("{} NÃO é uma data valida".format(data))
    else:
        return print("{} NÃO é uma data valida".format(data))

#ex19
def ex19():
    while True:
        x = int(input("Insira um numero menor que 1000\n"))
        if 0<=x<1000:
            break

    c,d,u = 0,0,0
    c = x//100
    d = (x%100)//10
    u = int(str(x)[-1])
    return print("{} = {} centenas, {} dezenas, {} unidades.".format(x,c,d,u))

#ex20
def ex20():
    n1,n2,n3 = (float(x) for x in input("Insira as três notas parciais separadas por espaço\n").split())
    media = (n1+n2+n3)/3
    if media == 10.0:
        return print("APROVADO COM DISTINÇÃO")
    elif media < 7.0:
        return print("REPROVADO")
    elif 7 <= media < 10:
        return print("APROVADO")

#ex21
def ex21():
    while True:
        saque = int(input("Caro usuario, digite abaixo o valor a ser sacado:\n"))
        if 10<=saque<=600:
            break
        else:
            print("Por Favor, Digite um valor entre 10 e 600 reais.")

    nota100, saque2 = saque//100, saque%100
    nota50, saque2 = saque2//50, saque2%50
    nota10, saque2 = saque2//10, saque2%10
    nota5, saque2 = saque2//5, saque2%5
    nota1, saque2 = saque2//1, saque2%1
    print("""PARA SACAR O VALOR DE R${:.2f} SÃO NECESSÁRIAS AS SEGUINTES QUANTIAS DE CEDULAS\n
    {} notas de 1 real
    {} notas de 5 reais
    {} notas de 10 reais
    {} notas de 50 reais
    {} notas de 100 reais""".format(saque, nota1, nota5, nota10, nota50, nota100))

#ex22
def ex22():
    x = int(input("Insira um numero inteiro: "))
    if x%2==0:
        return print("{} É PAR".format(x))
    else:
        return print("{} É IMPAR".format(x))

#ex23
def ex23():
    n = float(input("Insira um numero: "))
    if n == round(n):
        return print("{} É INTEIRO".format(n))
    else:
        return print("{} É DECIMAL".format(n))

#ex24
def ex24():
    a,b = (float(x) for x in input("Informe dois numeros: ").split())
    while True:
        escolha = str(input("Qual operação deseja realizar?\n[a]-Impar ou Par\n[b] - Positivo ou Negativo\n[c] - Inteiro ou Decimal")).lower()
        if escolha == 'a':
            if a%2==0:
                print("{} é par".format(a))
            else:
                print("{} é impar".format(a))

            if b%2 == 0:
                print("{} é par".format(b))
            else:
                print("{} é impar".format(b))

        elif escolha == 'b':
            if a>=0:
                print("{} é positivo".format(a))
            else:
                print("{} é negativo".format(a))

            if b>=0:
                print("{} é positivo".format(b))
            else:
                print("{} é negativo".format(b))

        elif escolha == 'c':
            if a == round(a):
                print("{} É INTEIRO".format(a))
            else:
                print("{} É DECIMAL".format(a))

            if b == round(b):
                print("{} É INTEIRO".format(b))
            else:
                print("{} É DECIMAL".format(b))

        else:
            break
    return None

#ex25
def ex25():

    print("RESPONDA AS PERGUNTAS ABAIXO\n[1] = SIM\n[2] = NÃO")
    a = int(input("Telefonou para a vítima? "))
    b = int(input("Esteve no local do crime? " ))
    c = int(input("Mora perto da vitima? "))
    d = int(input("Devia para a vitima? "))
    e = int(input("Já trabalhou com a vitima? "))

    soma = a + b + c + d + e
    if soma == 2:
        return print("A PESSOA É SUSPEITA")
    elif 3<=soma<=4:
        return print("A PESSOA É CÚMPLICE")
    elif soma == 5:
        return print("A PESSOA É ASSASSINO")
    else:
        return print("A PESSOA É INOCENTE")

#ex26
def ex26():
    combustivel = str(input("[A] - Alcool $1,90 \n [G] - Gasolina $2,50\nDigite o código correspondente do combustivel desejado:  ")).lower()
    quantia = float(input("Qual é a quantidade de litros de combustivel?\n"))

    if combustivel == 'a':
        combustivel = "Alcool"
        total = quantia * 1.90
        if 0<quantia<=20:
            total -= total*0.03  #3% de desconto
        elif quantia>20:
            total -= total*0.05
        else:
            total = 0.0

    elif combustivel =="g":
        combustivel = "Gasolina"
        total = quantia * 2.50
        if 0 < quantia <= 20:
            total -= total*0.04
        elif quantia > 20:
            total -= total * 0.06
        else:
            total = 0.0

    else:
        total = 0.0  #adicionando o total como 0.0 para evitar erros no terminal

    print("{} litros de {} custam ${:.2f} com desconto".format(quantia, combustivel, total))

#ex27
def ex27():
    print("""
    Até 5kg:
    Morango ---> $2,50
    Maça    ---> $1,80
    
    Acima de 5kg:
    Morango ---> $2,20
    Maça    ---> $1,50
    """)

    morango = float(input("Insira o peso de MORANGO desejado: "))
    maca = float(input("Insira o peso de MAÇA desejado: "))
    print("\n")

    if morango>5:
        p_morango = 2.2
    elif 0<=morango<=5:
        p_morango = 2.5
    else:
        p_morango = 0

    if maca>5:
        p_maca = 1.5
    elif 0<maca<=5:
        p_maca = 1.8
    else:
        p_maca = 0

    v_morango = morango * p_morango
    v_maca = maca * p_maca
    valor_total = v_morango + v_maca

    peso_total = maca + morango

    if peso_total > 8.0 or valor_total > 25.00:
        valor_total -= valor_total*0.1

    print("""CESTA DE COMPRAS:
    {:.2f} KGs de maçã    -----> ${:.2f}
    {:.2f} KGs de morango -----> ${:.2f}
    |-----------------------------------|
    VALOR TOTAL  --------------> ${:.2f}
    """.format(maca, v_maca, morango, v_morango, valor_total))

#ex28
def ex28():
    print("""PROMOÇÃO CARNE BARATINHA*
    
    Até 5kg:
    [F] File Duplo  ---> $4,90
    [A] Alcatra:    ---> $5,90
    [P] Picanha:    ---> $6,90
    
    Acima de 5kg:
    [F] File Duplo: ---> $5,80
    [A] Alcatra:    ---> $6,80
    [P] Picanha:    ---> $7,80
    
    *é permitida a retirada de apenas um tipo de carne devido à procura da promoção
    """)

    tipo = input("Digite o codigo correspondente ao tipo de carne desejada\n").lower()
    quantia = float(input("Quantos kilogramas deseja adquirir? "))

    if tipo == 'f':
        tipo = 'Filé Duplo'
        if quantia > 5:
            preco = 5.8
        elif 0<quantia<=5:
            preco = 4.9
        else:
            preco = 0.0
    elif tipo == 'a':
        tipo = "Alcatra"
        if quantia > 5:
            preco = 6.8
        elif 0<=quantia<=5:
            preco = 5.9
        else:
            preco = 0.0
    elif tipo == 'p':
        tipo = "Picanha"
        if quantia > 5:
            preco = 7.8
        elif 0 <= quantia <= 5:
            preco = 6.9
        else:
            preco = 0.0
    else:
        preco = 0.0
        tipo = "Invalido"

    cartao = int(input("A compra será realizada no Cartão Tabajara que concede 5% de desconto?\n[1] - SIM ou [2] NÃO  : "))

    total = quantia * preco
    if cartao == 1:
        desconto = total*0.05
        pgmt = 'CARTÃO TABAJARA'
    else:
        desconto = 0.0
        while True:
            p = int(input("""
            Então, como será realizado o pagamento? 
            __________________________________________
            [1] = DINHEIRO
            [2] = CARTAO DE CREDITO
            [3] = CARTAO DE DEBITO
            [4] = PIX
            __________________________________________
            Por favor digitar o código correspondente: """))
            if p == 1:
                pgmt = "DINHEIRO"
                break
            elif p == 2:
                pgmt = "CARTAO DE CREDITO"
                break
            elif p == 3:
                pgmt = "CARTAO DE DEBITO"
                break
            elif p == 4:
                pgmt = "PIX"
                break
            else:
                print("\nPOR FAVOR DIGITAR O CODIGO CORRESPONDENTE CORRETAMENTE\n\n")

    print("""\n\nCUPOM FISCAL:
    {:.2f} KGs de {}  -----> ${:.2f}
    DESCONTO  -------------> ${:.2f}
    
    VALOR A PAGAR ---------> ${:.2f}
    FORMA DE PAGAMENTO: {}
    """.format(quantia, tipo, total, desconto, (total - desconto), pgmt))