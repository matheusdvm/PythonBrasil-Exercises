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
