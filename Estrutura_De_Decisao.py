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