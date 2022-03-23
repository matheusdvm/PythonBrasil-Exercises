import Estrutura_Sequencial as E

def clean():
	print('\n'*80)

def logo():
	print("""                _  _         _    _         _      _ _ _
               |_)|_  /\/` |_   / \|\ |   |_  /\ |_) | |_|
               |  |_ /""\\_,|_   \_/| \|   |_ /""\| \ | | |
     .-------------------------------------------------------------.
     |    _     .-.                                                |
     |   | `.  /  | ,--.                                .          |
    __   \  |  |_/ /   /                             _.'|          |
 .'   `'. \ /,-'';,'-'`         '.                ,'`   ',    ,    |
  \      \.;'   / |`\,.--.        \             ,'      '|   /|    |
   `-._.-;/    | ,'/\ `.  \        |    .,._ .'          |_,' |,   |
,'```'-.,'     \/ /  \  `-'        .-'`     `'.     _,---'     |   |
`.._____/         ;  |             |`.  o      \ .-'           |   |
    ,-';   /`.    |  /             | |         ,'              |   |
  ,'   /  /  |    '.'             .' ;        /                |   |
 /   ,'| ;   |.-.            _    /  /       .'                '   |
'--'`| | |  /   /.'`.       | `. ;__ .       |                /    |
     | | | /   / |  | .-.   \  | /\_)|       \               '     |
    _|._\|/--'`  |  ' |  \   `.|'    |        `.           ,'\     |
  .'    /`;      | /   \__'_,;-.     :          '-..__.,.-'   `.   |
 /    ,' /\\     |/    _,-|\  \ `.   '                          `'-..__
 '--'`   | \`'-._;_.,-'   | \  '-'    '                                )
     |   |  ;       |\    `._)         \                  ,-'`.       /
     |   ;  |       | \                 `.              ,'    |     ,'
     |    \_/       |  ;                  `-.         ,'      |   ,'
     |              \  |                     `''--''`          `'` |
     |               `-'                  made by:    matheusdvm   |
     '-------------------------------------------------------------'""")


def main():
	while True:
		logo()
		numero_exercicio = qual_exercicio()
		aviso_executando_ex(numero_exercicio)

		if numero_exercicio == 1:
			l = E.qual_linguagem()
			E.hello_world(l)

		elif numero_exercicio == 2:
			n = E.qual_numero()
			E.number_is(n)

		elif numero_exercicio == 3:
			a = E.que_numero_somar()
			b = E.que_numero_somar()
			c = E.sum_numbers(a,b)
			print("{} + {} = {}".format(a,b,c))

		elif numero_exercicio == 4:
			quantia = int(input("Quantas provas foram realizadas no periodo?\n"))
			media = E.grades_average(quantia)
			print("A MEDIA DO PERIODO É DE: {}:.2f PONTOS".format(media))

		elif numero_exercicio == 5:
			m = float(input("Quantos Metros deseja transformar em CM? "))
			c = E.m_to_cm(m)
			print("{}:.2fm = {}:.cm".format(m,c))

		elif numero_exercicio == 6:
			r = float(input("Quantos metros o raio do círculo possui?"))
			a = E.circle_area(r)
			print("\n\n A AREA DO CIRCULO DE RAIO {}:.2f É IGUAL A {}:.2f".format(r,a))

		elif numero_exercicio == 7:
			lado = float(input("Qual é o tamanho do lado do quadrado? "))
			aq = E.square_area(lado,lado)
			da = E.double_area(aq)
			print("O DOBRO DA AREA DO QUADRADO DE {}:.2fm2 É {}:.2fm2\n".format(aq,da))

		elif numero_exercicio == 8:
			print("O Salário é: {}:.2f".format(E.gross_salary()))

		elif numero_exercicio == 9:
			print("WELCOME TO 'ºF TO ºC GENERATOR'")
			print("{}ºC".format(E.fahr_to_celsius()))

		elif numero_exercicio == 10:
			print("WELCOME TO 'ºC TO ºF GENERATOR'")
			print("{}ºF".format(E.celsius_to_fahr()))

		elif numero_exercicio == 11:
			E.calculate_and_show()

		elif numero_exercicio == 12:
			print("WELCOME TO 'MALE PERFECT WEIGHT PROGRAM'")
			good_weight = E.perfect_weight_men()
			print("{}:.2fKG is your perfect weight based on your height".format(good_weight))

		elif numero_exercicio == 13:
			print("WELCOME TO 'UNISSEX PERFECT WEIGHT PROGRAM'")
			good_weight = E.perfect_weight()
			print("Your perfect weight is {}KG".format(good_weight))

		elif numero_exercicio == 14:
			print("PAPO DE PESCADOR: DESCOBRIR O VALOR DA MULTA AMBIENTAL")
			multa = E.papo_de_pescador()
			print("\n${}:.2f É O VALOR QUE DEVERÁ SER PAGO ÀS AUTORIDADES AMBIENTAIS")

		elif numero_exercicio == 15:
			print("WELCOME TO 'WHAT IS MY LIQUID SALARY?' PROGRAM")
			E.liquid_salary()

		elif numero_exercicio == 16:
			E.paint_store_01()

		elif numero_exercicio == 17:
			gallons = E.total_gallons()
			s1 = E.situation_01(gallons)
			s2 = E.situation_02(gallons)
			print("${}:.2f with big ones and ${}:.2f with the small ones".format(s1,s2))
			print("SITUATION 3 HAVE TO BE WORKED")

		elif numero_exercicio == 18:
			seconds = E.download_time()
			minutes = seconds//60
			seconds = int(seconds%60)
			hours = int(minutes//60)
			minutes = int(minutes%60)
			print("{} hours {} minutes {} seconds remaining".format(hours, minutes, seconds))

		clean()

if '__main__' == __name__:
	main()
