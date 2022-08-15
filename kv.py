import random
import math
import time

### SETTINGS ###
mode = 1
			  # Режимы работы
	 		  # 0 - автоматическая генерация
			  # 1 - ввести коэф. уравнения
			  # 2 - создать уравнение по корням
			  # 3 - разложить уравнение (ax + n)²
			  # 4 - [засекречено]

count = 0   # Счетчик запусков (стоит на '0')


### DEF RANDOM START ###
def rnd():
	predel_max = 5 # Можно менять. Предел коэффициентов
	predel_min = -predel_max
	global a
	global b
	global c
	a = random.randint(predel_min, predel_max)
	b = random.randint(predel_min, predel_max)
	c = random.randint(predel_min, predel_max)

### DEF RANDOM END ###


### DEF OSNOVNOE YRAVN START ###

def yravnenie(a, b, c):
	if int(a) == a:
		a = int(a)
	if int(b) == b:
		b = int(b)
	if int(c) == c:
		c = int(c)
	if a == 1:
		if b < 0 and c < 0:
			print('x² - ' + str(abs(b))+'x - ' + str(abs(c)))
		elif b < 0:
			print('x² - ' + str(abs(b))+'x + ' + str(c))
		elif c < 0:
			print('x² + ' + str(b)+'x - ' + str(abs(c)))
		else:
			print('x² + ' + str(b)+'x + ' + str(c))
	elif a == -1:
		if b < 0 and c < 0:
			print('-x² - ' + str(abs(b))+'x - ' + str(abs(c)))
		elif b < 0:
			print('-x² - ' + str(abs(b))+'x + ' + str(c))
		elif c < 0:
			print('-x² + ' + str(b)+'x - ' + str(abs(c)))
		else:
			print('-x² + ' + str(b)+'x + ' + str(c))
	else:
		if b < 0 and c < 0:
			print(str(a)+'x² - ' + str(abs(b))+'x - ' + str(abs(c)))
		elif b < 0:
			print(str(a)+'x² - ' + str(abs(b))+'x + ' + str(c))
		elif c < 0:
			print(str(a)+'x² + ' + str(b)+'x - ' + str(abs(c)))
		else:
			print(str(a)+'x² + ' + str(b)+'x + ' + str(c))

### DEF OSNOVNOE YRAVN END ###


### DEF PRIVED. YRAVN START ###

def yravnenie_dop(a, b, c):
	if int(a) == a:
		a = int(a)
	if int(b) == b:
		b = int(b)
	if int(c) == c:
		c = int(c)

	if b % a == 0 and c % a == 0:
		if a > 0:
			ba = b//a
			if int(ba) == ba:
				ba = int(ba)
			ca = c//a
			if int(ca) == ca:
				ca = int(ca)
			if b < 0 and c < 0:
				print('x² - ' + str(abs(ba))+'x - ' + str(abs(ca)))
			elif b < 0:
				print('x² - ' + str(abs(ba))+'x + ' + str(ca))
			elif c < 0:
				print('x² + ' + str(ba)+'x - ' + str(abs(ca)))
			else:
				print('x² + ' + str(ba)+'x + ' + str(ca))
		else:
			ba = b//a
			if int(ba) == ba:
				ba = int(ba)
			ca = c//a
			if int(ca) == ca:
				ca = int(ca)
			if b < 0 and c < 0:
				print('x² + ' + str(abs(ba))+'x + ' + str(abs(ca)))
			elif b < 0:
				print('x² + ' + str(abs(ba))+'x - ' + str(abs(ca)))
			elif c < 0:
				print('x² - ' + str(abs(ba))+'x + ' + str(abs(ca)))
			else:
				print('x² - ' + str(abs(ba))+'x - ' + str(abs(ca)))

### DEF PRIVED. YRAVN END ###


### DEF FIND ANSWERS START ###

def korni(a, b, c):

	if int(a) == a:
		a = int(a)
	if int(b) == b:
		b = int(b)
	if int(c) == c:
		c = int(c)

	D = b**2 - 4*a*c
	sD = float(math.sqrt(D))

	if int(sD) == sD:
		sD = int(sD)
	print('Корни:')

	ch1 = round(-b + sD, 7)
	ch2 = round(-b - sD, 7)
	zn1 = round(2*a, 7)
	zn2 = round(2*a, 7)
	if int(sD) == sD:
		k1 = math.gcd(ch1, zn1)
		k2 = math.gcd(ch2, zn2)
	else:
		if round(sD, 4) != sD:
			print('Ответ примерный!')	
		print('D = ' + str(D))
		k1 = 1
		k2 = 1

	x1 = ((ch1/k1)/(zn1/k1))
	x2 = ((ch2/k2)/(zn2/k2))

	if ch1 < 0 and zn1 < 0:
		ch1 = -ch1
		zn1 = -zn1
	if ch2 < 0 and zn2 < 0:
		ch2 = -ch2
		zn2 = -zn2

	if len(str(x1)) < 7 and len(str(x2)) < 7:
		if x1 == x2 or D == 0:
			if int(x1) == x1:
				print('x =', int(x1))
			else:
				print('x =', x1)
		else:
			if int(x1) == x1 and int(x2) == x2:
				print('x₁ =', int(x1))
				print('x₂ =', int(x2))
			else:
				if int(x1) == x1:
					print('x₁ =', int(x1))
				else:
					print('x₁ =', x1)
				if int(x2) == x2:
					print('x₂ =', int(x2))
				else:
					print('x₂ =', x2)
	else:
		zn1k1 = zn1/k1
		if int(zn1k1) == zn1k1:
			zn1k1 = int(zn1k1)
		zn2k2 = zn2/k2
		if int(zn2k2) == zn2k2:
			zn2k2 = int(zn2k2)
		ch1k1 = ch1/k1
		if int(ch1k1) == ch1k1:
			ch1k1 = int(ch1k1)
		ch2k2 = ch2/k2
		if int(ch2k2) == ch2k2:
			ch2k2 = int(ch2k2)

		if D == 0 or (ch1k1 == ch2k2 and zn1k1 == zn2k2):
			print('x =', str(round((ch1k1), 4)) + '/' + str(round((zn1k1), 4)))
		else:
			if len(str(x1)) >= 6 and len(str(x2)) >= 6:
				print('x₁ =', str(round((ch1k1), 4)) + '/' + str(round((zn1k1), 4)))
				print('x₂ =', str(round((ch2k2), 4)) + '/' + str(round((zn2k2), 4)))
			elif len(str(x1)) >= 6:
				print('x₁ =', str(round((ch1k1), 4)) + '/' + str(round((zn1k1), 4)))
				if x2 == int(x2):
					print('x₂ =', int(x2))
				else:
					print('x₂ =', x2)
			elif len(str(x2)) >= 6:
				if x1 == int(x1):
					print('x₁ =', int(x1))
				else:
					print('x₁ =', x1)
				print('x₂ =', str(round((ch2k2), 4)) + '/' + str(round((zn2k2), 4)))

### DEF FIND ANSWERS END ###


### MODE 0 START ###
# Random Y

if mode == 0:
	print('Случайное уравнение: ')
	rnd()
	while True:
		D = D = b**2 - 4*a*c
		count += 1

		if D < 0 or (a == 0 or b == 0 or c == 0):
			rnd()

		else:
			sD = math.sqrt(D)
			if int(sD) == sD:

				if str(int(sD)).isnumeric() == True:
					yravnenie(a, b, c)
					yravnenie_dop(a, b, c)
					print('')
					korni(a, b, c)
					print('')
					print('D = ' + str(D), 'C = ' + str(count))
					break
			else:
				rnd()

### MODE 0 END ###


### MODE 1 START ###
# non-Random Y

if mode == 1:
	print('Введите коэффициенты уравнения: ')
	sp = list(map(float, input('a = ').split()))
	if len(sp) == 1:
		a = sp[0]
		b = float(input('b = '))
		c = float(input('c = '))
	elif len(sp) == 2:
		a = sp[0]
		b = sp[1]
		c = float(input('c = '))
	else:
		a = sp[0]
		b = sp[1]
		c = sp[2]
	print('')
	if a != 1:
		yravnenie(a, b, c)
		yravnenie_dop(a, b, c)
	else:
		yravnenie_dop(a, b, c)
	print('')
	D = b**2 - 4*a*c
	if D < 0:
		D = round(D, 7)
		if int(D) == D:
			D = int(D)
		print('Дискриминант меньше нуля, решений нет', '(D =', str(D) + ')')
	else:
		korni(a, b, c)

### MODE 1 END ###


### MODE 2 START ###
# Find Y
if mode == 2:
	print('Введите уравнение с желаемыми корнями:')
	sp = list(map(float, input('x₁ = ').split()))
	if len(sp) == 1:
		x1 = sp[0]
		x2 = float(input('x₂ = '))
	elif len(sp) == 2:
		x1 = sp[0]
		x2 = sp[1]

	b = (x1 + x2) *(-1)
	c = x1 * x2
	a = 1

	print('')
	print('Вот варианты уравнений: ')
	print('---')

	yravnenie(a, b, c)
	
	rndm1 = random.randint(2, 4)
	rndm2 = round(random.random(), 1)
	if rndm2 == 0:
		rndm2 = 0.1
	print('---')
	yravnenie(a*rndm1, b*rndm1, c*rndm1)
	print('---')

	if round(b*rndm2, 5) == int(round(b*rndm2, 5)) and round(c*rndm2, 5) == int(round(c*rndm2, 5)):
		yravnenie(a*rndm2, int(round(b*rndm2, 5)), int(round(c*rndm2, 5)))

	elif round(b*rndm2, 5) == int(round(b*rndm2, 5)):
		yravnenie(a*rndm2, round(b*rndm2, 5), round(c*rndm2, 5))

	elif round(c*rndm2, 5) == int(round(c*rndm2, 5)):
		yravnenie(a*rndm2, round(b*rndm2, 5), int(round(c*rndm2, 5)))

	else:
		yravnenie(a*rndm2, round(b*rndm2, 5), round(c*rndm2, 5))

### MODE 2 END ###



### MODE 3 START ###

if mode == 3:
	print('Введите a и  n, чтобы раскрыть (ax + n)²:')
	sp = list(map(float, input('a = ').split()))
	if len(sp) == 1:
		ax = sp[0]
		n = float(input('n = '))
	elif len(sp) == 2:
		ax = sp[0]
		n = sp[1]

	a = ax**2
	b = 2*ax*n
	c = n**2
	print('')

	if int(ax) == ax:
		ax = int(ax)
	if int(n) == n:
		n = int(n)
	if a == 1 or a == -1:
		if ax < 0 and n < 0:
			print('(-' + 'x - ' + str(abs(n)) + ')²')
		elif ax < 0:
			print('(-'+  'x + ' + str(abs(n)) + ')²')
		elif n < 0:
			print('(' + 'x - ' + str(abs(n)) + ')²')
		else:
			print('(' + 'x + ' + str(abs(n)) + ')²')
	else:
		if ax < 0 and n < 0:
			print('(-' + str(abs(ax)) + 'x - ' + str(abs(n)) + ')²')
		elif ax < 0:
			print('(-' + str(abs(ax)) + 'x + ' + str(abs(n)) + ')²')
		elif n < 0:
			print('(' + str(ax) + 'x - ' + str(abs(n)) + ')²')
		else:
			print('(' + str(ax) + 'x + ' + str(abs(n)) + ')²')
	print('')

	if a != 1:
		yravnenie(a, b, c)
		yravnenie_dop(a, b, c)
	else:
		yravnenie_dop(a, b, c)
	korni(a, b, c)

### MODE 3 END ###



### MODE 4 START ###
if mode == 4:
	print('Запрещенная секция!')
	time.sleep(1)
	print('Пожалуйста, покиньте зону!')
	time.sleep(1)
	print('Уйти? (Да/Нет)')
	answer = input()
	if answer == 'Да' or answer == 'lf' or answer == 'да':
		print('Спасибо за понимание')
		time.sleep(1)
		print('Хорошего дня!')
	else:
		time.sleep(1)
		print('Ладно, тогда проходите')
		time.sleep(2)
		print('░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░')
		time.sleep(0.05)
		print('░░░░█░░░░░░░░░░░░░█░░░░')
		time.sleep(0.05)
		print('░░░█░░░░░░░░░░▄▄▄░░█░░░')
		time.sleep(0.05)
		print('░░░█░░▄▄▄░░▄░░███░░█░░░')
		time.sleep(0.05)
		print('░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░')
		time.sleep(0.05)
		print('░░░█░░▀█▀█▀█▀█▀█▀░░█░░░')
		time.sleep(0.05)
		print('░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░')
		time.sleep(0.05)
		print('░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░')
		time.sleep(0.05)
		print('▄▀░▄▄▀▄▄▀▀▀▄▀▀▀▄▄▀▄▄░▀▄')
		time.sleep(0.05)
		print('█░░░░▀▄░█▄░░░▄█░▄▀░░░░█')
		time.sleep(0.05)
		print('░▀▄▄░█░░█▄▄▄▄▄█░░█░▄▄▀░')
		time.sleep(0.05)
		print('░░░▀██▄▄███████▄▄██▀░░░')
		time.sleep(0.05)
		print('░░░████████▀████████░░░')
		time.sleep(0.05)
		print('░░▄▄█▀▀▀▀█░░░█▀▀▀▀█▄▄░░')
		time.sleep(0.05)
		print('░░▀▄▄▄▄▄▀▀░░░▀▀▄▄▄▄▄▀░░')
		time.sleep(0.1)
		time.sleep(2)
		print('Сыграем в игру?')
		time.sleep(1)
		print('Согласиться? (Да/Нет)')
		answer = input()
		if answer == 'Да' or answer == 'lf' or answer == 'да':
			print('Хо-хо-хо!')
			time.sleep(1)
			print('Значит так, игра простая:')
			time.sleep(1)
			print('Кидаем монету!')
			time.sleep(1)
			print('Играем на кристаллы')
			time.sleep(1)
			print('Держи 5 кристаллов')
			time.sleep(2)
			bal = 5
			streak = 0
			streak_n = 0
			while True:

				print('')
				print('Баланс:', bal)
				time.sleep(0.7)
				print('Выбирай: Луна или Солнце?')
				print('Луна - 0, Солнце - 1')
				mon = random.randint(0, 1)
				answer = int(input())
				time.sleep(2)
				if mon == 0:

					print('___________00_____________________7_______________')
					print('________0000_____________________777______________')
					print('______0000______________________77777_____________')
					print('____00000______________________7777777____________')
					print('___00000______________________777777777___________')
					print('__000000____________77777777777777777777777777777')
					print('_0000000______________7777777777777777777777777___')
					print('_0000000_______________7777777777777777777777_____')
					print('_0000__00_________________77777777777777777_______')
					print('_0000__00000000__________777777777_777777777______')
					print('_000000000000___________7777777_______7777777_____')
					print('__0000000000___________77777_____________77777____')
					print('___0000_000000________777___________________777___')
					print('____00000_______0___________0000__________________')
					print('______000000__00000______000000___________________')
					print('________000000000000000000000_____________________')
					print('__________00000000000000000_______________________')
					print('______________000000000___________________________')

				else:
					print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡿⠁⠄⣾⣿⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠻⠃⠄⠄⠻⠁⠄⣿⡿⠛⣽⣿⣿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣷⡉⠙⠻⢆⣠⣴⡶⠶⠶⣶⣦⣅⠄⢰⣿⣿⠿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣿⣿⡄⣠⣿⠛⠁⠄⠄⠄⠄⠉⠻⣷⡍⠄⢀⣾⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣦⣄⠄⢰⣿⠁⣊⣭⡙⣦⠄⣠⣤⣀⠘⣿⡀⠉⠉⠛⢿⣿⣿⣿⣿')
					print('⣿⣶⣤⡀⠉⠙⠋⠁⢸⡇⠄⠙⠛⠉⣿⠄⠙⠛⠉⠄⣿⡇⣀⣤⣀⡀⠉⠻⠿⣿')
					print('⣿⣿⣿⣿⣶⣄⣀⡀⠸⣿⡀⠄⠄⠐⠿⠄⠄⠄⠄⢠⣿⠁⠈⠙⠿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⠟⠁⠄⡙⣿⣤⡀⠐⠓⠓⠂⣀⣴⡿⠃⠻⣿⣿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣷⣶⣿⣿⠁⠈⡙⠻⠷⠶⠶⠿⠟⠋⢰⣤⣄⡙⢿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣿⣿⣇⣴⣾⡇⠄⣠⡆⠄⠄⢰⣄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣰⣿⡇⠄⢠⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠄⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
					print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
				if answer == mon and streak < 3:
					print('Ха! Ты выиграл! Держи кристалл')
					time.sleep(2)
					bal += 1
					streak += 1
				elif answer != mon:
					print('Есть! Выиграл Я. Давай 2 кристалла')
					time.sleep(2)
					bal -= 2
					streak_n += 1

				if bal < 0:
					print('')
					print('Кажется, у тебя закончились кристаллы!')
					time.sleep(2)
					print('Приходи, когда будешь побогаче!')
					break
					time.sleep(2)

				if streak == 3:
					print('')
					print('Да ты жульничаешь!')
					time.sleep(2)
					print('Нельзя выиграть 3 раза подряд!')
					time.sleep(2)
					print('Приходи, когда будешь играть честно!')
					break
					time.sleep(2)

				if streak_n == 3:
					print('')
					print('Ха-ха-ха! Ладно')
					time.sleep(2)
					print('Признаюсь честно, я жульничаю')
					time.sleep(2.3)
					print('...')
					time.sleep(1)
					print('Но ведь игра моя!')
					print('Эм...')
					time.sleep(2.5)
					print('Ладно, хорошего дня. До свидания!')
					break

		else:
			print('Ну что ж')
			time.sleep(1)
			print('Не смею Вас задерживать!')
			time.sleep(1)
			print('Хорошего дня!')
			time.sleep(1)
		print('...')
		time.sleep(3)

### MODE 4 END ###