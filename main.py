import requests

link = "https://makarbass.github.io"
sword = requests.get(link).content.decode("utf-8")[:5]
count = 0
istrue= False
first = True

def check_let(sword, uword):
	i = 0;
	set_sword = set(sword)
	checkword = ''
	while (i < 5):
		if (uword[i] == sword[i]):
			checkword = checkword + uword[i].upper()
		elif (uword[i] in set_sword):
			checkword = checkword + uword[i]
		else:
			checkword = checkword + '■'
		i += 1
	if (checkword.lower() == sword):
		print("ВЕРНО! Слово:", sword)
		istrue = True
		return True



while (count < 5 and istrue == False):
	if count == 0:
		print("""Добро пожаловать в игру!
Введите слово из 5 букв.

Если буква на своем месте - А
Если буква не на своем месте - а
Если такой буквы нет в слове - ■
""")
	print("Осталось попыток: ", 5-count)
	uword = input("Введи слово:").strip()
	#print(uword.isalpha())
	if uword.isalpha() == True:
		if len(uword) == 5:
			if check_let(sword, uword) == True:
				break;
		else:
			print("Слово состоит не из 5 букв")
			count -= 1
	else:
		print("Слово содержит не только буквы")
		count -= 1
	count += 1;

if (count == 5):
	print("Ты проиграл!")