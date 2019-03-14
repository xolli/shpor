from sys import argv

for filename in argv[1:]:
	try:
		fin = open (filename, 'r')
	except:
		print ("файл \"", filename, "\" не найден", sep = '')
		exit()
	filetext = fin.read()
	print ("До:", filetext, sep='\n')
	filetext = filetext.replace('∀', "люб ")
	filetext = filetext.replace('∃', "сущ ")
	filetext = filetext.replace('∅', "Ø")
	filetext = filetext.replace('∉', "¬∈")
	filetext = filetext.replace('∋', "содерж ")
	filetext = filetext.replace('⊂', "подмн-во ")
	filetext = filetext.replace('⊄', "¬подмн-во ")
	filetext = filetext.replace('⊃', "надмн-во ")
	filetext = filetext.replace('⊆', "=подмн-во")
	filetext = filetext.replace('⊇', "=надмн-во")
	filetext = filetext.replace('⊊', "≠подмн-во")
	filetext = filetext.replace('⊋', "≠надмн-во")
	#filetext = filetext.replace('⊗', "")
	filetext = filetext.replace('➙', "->")
	filetext = filetext.replace('➙', "->")
	filetext = filetext.replace('↦', "->")
	filetext = filetext.replace('➔', "->")
	filetext = filetext.replace('⇨', "=>")
	filetext = filetext.replace('⇒', "=>")
	filetext = filetext.replace('⇦', "<=")
	filetext = filetext.replace('⇐', "<=")
	filetext = filetext.replace('⇔', "<=>")
	filetext = filetext.replace('ℕ', "N")
	filetext = filetext.replace('ℤ', "Z")
	filetext = filetext.replace('ℚ', "Q")
	filetext = filetext.replace('ℝ', "R")
	filetext = filetext.replace('ℝ', "R")
	filetext = filetext.replace('ℂ', "C")
	filetext = filetext.replace(', . . . , ', "…")
	filetext = filetext.replace(' , . . .', "…")
	filetext = filetext.replace(' . . . ', "…")
	filetext = filetext.replace('...', "…")
	filetext = filetext.replace('1/4', "¼")
	filetext = filetext.replace('1/3', "⅓")
	filetext = filetext.replace('1/2', "½")
	filetext = filetext.replace('2/3', "⅔")
	filetext = filetext.replace('2/3', "⅔")
	filetext = filetext.replace('3/4', "¾")
	filetext = filetext.replace('^1', "¹")
	filetext = filetext.replace('^2', "²")
	filetext = filetext.replace('^3', "³")
	filetext = filetext.replace('такой, что', "т.ч.")
	filetext = filetext.replace('такой что', "т.ч.")
	filetext = filetext.replace('такое что', "т.ч.")
	filetext = filetext.replace('такое, что', "т.ч.")
	filetext = filetext.replace('такая что', "т.ч.")
	filetext = filetext.replace('такая, что', "т.ч.")
	filetext = filetext.replace('в том числе', "в том ч.")
	filetext = filetext.replace('свойству', "св-ву")
	filetext = filetext.replace('свойство', "св-во")
	filetext = filetext.replace('множество', "мн-во")
	filetext = filetext.replace('множества', "мн-ва")
	filetext = filetext.replace('система', "сист")
	filetext = filetext.replace('предыдущего', "пред")
	filetext = filetext.replace('определения', "опред")
	filetext = filetext.replace('единственное', "ед.")
	filetext = filetext.replace('принадлежит', "∈")
	filetext = filetext.replace('Принадлежит', "∈")
	filetext = filetext.replace('Доказательство', "ДОК-ВО")
	filetext = filetext.replace('доказательство', "ДОК-ВО")
	filetext = filetext.replace('Так как', "Т.к.")
	filetext = filetext.replace('так как', "т.к.")
	filetext = filetext.replace('таким образом', "т.о.")
	filetext = filetext.replace('Таким образом', "Т.о.")
	filetext = filetext.replace('ноль', "0")
	filetext = filetext.replace('нуль', "0")
	filetext = filetext.replace('один', "1")
	filetext = filetext.replace('два', "2")
	filetext = filetext.replace('двух', "2ух")
	filetext = filetext.replace('три ', "3 ")
	filetext = filetext.replace('три\n', "3\n")
	filetext = filetext.replace('четыре', "4")
	filetext = filetext.replace('пять', "5")
	filetext = filetext.replace('шесть', "6")
	filetext = filetext.replace('семь', "7")
	filetext = filetext.replace('восемь', "8")
	filetext = filetext.replace('девять', "9")
	filetext = filetext.replace('Согласно', "Согл")
	filetext = filetext.replace('согласно', "согл")
	filetext = filetext.replace('некоторого', "нек-го")
	filetext = filetext.replace('Некоторого', "Нек-го")
	filetext = filetext.replace('последовательность', "послед.")
	filetext = filetext.replace('Последовательность', "Послед.")
	filetext = filetext.replace('ограничена', "огранич.")
	filetext = filetext.replace('Зафиксируем', "Зафикс.")
	filetext = filetext.replace('зафиксируем', "зафикс.")
	filetext = filetext.replace('фиксированного', "фикс.")
	filetext = filetext.replace('Фиксированного', "Фикс.")
	filetext = filetext.replace('минимум', "мин.")
	filetext = filetext.replace('максимум', "макс.")
	filetext = filetext.replace('является', "явл.")
	filetext = filetext.replace('являются', "явл.")
	filetext = filetext.replace('бесконечно', "беск.")
	filetext = filetext.replace('неубывающая', "неуб.")
	filetext = filetext.replace('невозрастающая', "невозр.")
	filetext = filetext.replace('означет', "знач.")
	filetext = filetext.replace('значит', "знач.")
	filetext = filetext.replace('некоторому', "некот-му.")
	filetext = filetext.replace('выбираем', "выбир.")
	filetext = filetext.replace('натуральный', "натур.")
	filetext = filetext.replace('существует', "сущ.")
	filetext = filetext.replace('наибольший', "наиб.")
	filetext = filetext.replace('наименьший', "наим.")
	filetext = filetext.replace('равносильно', "равносил.")
	filetext = filetext.replace('получаем', "получ.")
	filetext = filetext.replace('вытекает', "вытек.")
	filetext = filetext.replace('Неравенство', "Нер-во.")
	filetext = filetext.replace('неравенство', "нер-во.")
	filetext = filetext.replace('сходится', "сход.")
	filetext = filetext.replace('Функция', "Ф-я")
	filetext = filetext.replace('функция', "ф-я")
	filetext = filetext.replace('Функции', "Ф-ции")
	filetext = filetext.replace('функции', "ф-ции")
	filetext = filetext.replace('называется', "наз-ся")
	filetext = filetext.replace('сгущения', "сгущ.")
	filetext = filetext.replace('содержится', "содерж.")
	filetext = filetext.replace('по крайней мере', "по кр. мере")
	filetext = filetext.replace('отличная', "отл.")
	filetext = filetext.replace('Определение', "Опр.")
	filetext = filetext.replace('определение', "опр.")
	filetext = filetext.replace('lim\nn→∞\nxn', "lim_n→∞(xn)")
	filetext = filetext.replace('lim\nn→∞\nyn', "lim_n→∞(yn)")
	filetext = filetext.replace('lim\nn→∞\nzn', "lim_n→∞(zn)")
	filetext = filetext.replace('lim\nn→∞\nan', "lim_n→∞(an)")
	filetext = filetext.replace('lim\nn→∞\nbn', "lim_n→∞(bn)")
	filetext = filetext.replace('lim\nn→∞\ncn', "lim_n→∞(cn)")

	filetext = filetext.replace('=>\n-', "=>")
	filetext = filetext.replace('=>', "=>\n- ")

	filetext = filetext.replace('  ', " ")
	if "END" not in filetext:
		filetext += "\n--END--\n"

	print ("\nПосле:", filetext, sep='\n')
	print ("\nПринять изменения? (y/N)", end = ' ')
	agree = input().lower()
	if agree == 'y' or agree == 'д' or agree == "yes" or agree == "да":
		fin.close()
		fin = open (filename, 'w')
		fin.write(filetext)
	fin.close()
	print()