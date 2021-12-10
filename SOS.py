b='Programmerimine'
b_l=list(b)
print(b,b_l)
while True:
	print()
	print("1-len")
	print("2-isdigit")
	print("3-isalpha")
	print("4-upper")
	print("5-lower")
	print("6-join")
	print("7-swapcase")
	print("8-title")
	print("9-isalnum")
	print("10-isspace")
	valik = int(input(""))
	print()
	if valik == 1:
		print("Всего ",len(b_l)," симболов") #Длина строки
	elif valik == 2:
		if b.isdigit()==True: #Состоит ли строка из цифр
			print("Есть цифры")
		else:
			print("Нету цифер")
	elif valik == 3:
		if b.isalpha()==True: #Состоит ли строка из букв
			print("Есть буквы")
		else:
			print("Нету букв")
	elif valik == 4:
		print(b.upper()) #Заглавные буквы
	elif valik == 5:
		print(b.lower()) #Маленькие буквы
	elif valik == 6:
		print(", ".join(b_l))#склейвание 
	elif valik == 7:
		print(b.swapcase())# Переводит символы нижнего регистра в верхний, а верхнего – в нижний
	elif valik == 8:
		print(b.title())# Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
	elif valik == 9:
		if b.isalnum()==True: # Состоит ли строка из цифр или букв
			print("Состоит из букв")
		else:
			print("Состоит из букв и цифр")
	elif valik == 10:
		if b.isspace()==True: #Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'), "новая строка" ('\n'), "перевод каретки"('\r'), "горизонтальная табуляция" ('\t') и "вертикальная табуляция"('\v'))
			print("В этом списке есть хотя бы одно место")
		else:
			print("В этом списке нет пробелов")
	else:
		print("Ошибка!")