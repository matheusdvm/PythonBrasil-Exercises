#EX 01
def maior():
    a,b = (float(x) for x in input().split())
    if a>b:
        return print(a)
    elif b>a:
        return print(b)
    else:
        return print("equal")

#EX 02

def neg_or_pos():
    x = float(input())
    if x >=0:
        return print("POSITIVE")
    elif x<0:
        return print("NEGATIVE")

#EX 03

def f_or_m():
    fm = str(input()).lower()
    if fm == "f":
        return print("F - Feminino")
    elif fm == "m":
        return print("M - Masculino")
    else:
        return print("Sexo Inválido")

#EX 04
def v_or_c():
    vc = str(input()).lower()
    vogais, consoantes = "aeiou", "bcdfghjklmnpqrstvwxyz"
    if vc in vogais:
        return print("VOGAL")
    elif vc in consoantes:
        return print("CONSOANTES")
    else:
        return print("OUTROS")

#ex 05
def passou_media():
    n1,n2 = (float(x) for x in input().split())
    media = (n1+n2)/2e
    if media==10:
        return print("aprovado com distinção".capitalize())
    elif media < 7:
        return print("Reprovado")
    elif media >= 7:
        return print("Aprovado")
    else:
        return print("Input inválido")

#ex 06  ajustar para if e elif até ex 08
def maior2():
    a,b,c = (float(x) for x in input().split())
    lista = [a,b,c]
    return print(lista.max())

#ex 07
def maior3():
    a,b,c = (float(x) for x in input().split())
    lista = [a,b,c]
    return print("MAIOR: {}\nMENOR: {}\n".format(lista.max(), lista.min()))

#ex 08
def mais_barato():
    a,b,c = (float(x) for x in input().split())
    lista = [a,b,c]
    return print("O produto mais barato é o de valor {}".format(lista.min()))

#ex 09
def decrescente():
    a,b,c = (float(x) for x in input().split())
    lista = [a,b,c]
    lista.sort(reverse=True)
    return print(lista)

#ex 10
def turno():
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
def tabajara():
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
    SALÁRIO ANTERIOR:{}:.2f
    COM AJUSTE SALARIAL DE {}
    VALOR DO AUMENTO: {}:.2f
    
    NOVO SALARIO: {}:.2f
    """.format(salario_anterior, p, v, salario))

#ex 12
def folha_de_pgmt():
    valor = float(input("Qual valor por hora?"))
    horas = int(input("Quantas horas trabalhadas?"))
    bruto = valor*horas
    sindicato = 0.03 * bruto
    fgts = 0.11 * bruto
    inss = 0.1*bruto
    if bruto <= 900:
        ir = 0
    elif bruto <= 1500:
        ir = bruto * 0.05
    elif bruto <= 2500:
        ir = bruto * 0.1
    elif bruto > 2500:
        ir = bruto * 0.2

    totaldesc, liquido = (sindicato+inss+ir), (bruto - totaldesc)
    p_ir = int((bruto / ir) * 100)
    print("""
    (+) SALARIO BRUTO: ({} * {}) = {}:.2f
    (-) IR ({}%) : {}:.2f
    (-) INSS (10%) : {}:.2f
    (-) SINDICATO (3%) : {}:.2f
    (-) FGTS (10%) : {}:.2f
    (=) Total de descontos : {}:.2f
    -------------------------------
    SALÁRIO LÍQUIDO: {}:.2F""".format(valor, horas, bruto, p_ir, ir, inss, sindicato,fgts,totaldesc,liquido)