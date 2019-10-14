while True:
	ex = input('Введите выражение: ')
	if ex == 'выйти':
		exit()
	parsed = ex.split(' ')
	a = int(parsed[0])
	op = parsed[1]
	b = int(parsed[2])
	if op == '+':
		print(a + b)
	elif op == '*':
		print(a * b)
	elif op == '/':
		print(a / b)
	else:
		print('Ошибка')
	