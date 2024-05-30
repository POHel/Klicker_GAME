import time
import colorama
from colorama import Fore
import sys
import os
import cars_check
import airplane_check
import config
colorama.init()
global balance
def balance():
	money = open('money.wallet', 'r')
	line = money.readline()
	money.close()
	balance = int(line)
	return balance

RES = Fore.RESET
RED = Fore.RED
GR = Fore.GREEN
MAG = Fore.MAGENTA
YE = Fore.YELLOW
WH = Fore.WHITE

def shop():
	print(f'''{YE}
  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$ 
 /$$__  $$| $$  | $$ /$$__  $$| $$__  $$
| $$  \__/| $$  | $$| $$  \ $$| $$  \ $$
|  $$$$$$ | $$$$$$$$| $$  | $$| $$$$$$$/
 \____  $$| $$__  $$| $$  | $$| $$____/ 
 /$$  \ $$| $$  | $$| $$  | $$| $$      
|  $$$$$$/| $$  | $$|  $$$$$$/| $$      
 \______/ |__/  |__/ \______/ |__/   {RES}   	

{MAG}0 - EXIT{RES}
{YE}---boosts---{GR}
1) заработок за 1 клик +5$ / стоимость: 100$
2) заработок за 1 клик +10$ / стоимость: 500$
3) заработок за 1 клик +50$ / стоимость: 1.000$
4) заработок за 1 клик +100$ / стоимость: 10.000${RES}
{RED}---energy---
{RED}не работает(в разработке){RES}
5) 1.000 en / 1.000$
6) 5.000 en / 10.000$
7) 10.000 en / 20.000$
8) 15.000 en / 50.000$
9) 20.000 en / 100.000$
{YE}---cars---{GR}
10) Subaru Empreso / 1.500.000$
11) Toyota Landcruser / 5.000.000$
12) Lamborgini Huracan / 15.000.000$
13) Bugatti Charon / 1.000.000.000$
14) BMW M5 competition / 10.000.000$
15) Tesla model Y / 10.500.000$
16) Ford Mustang / 20.000.000$
17) Nissan GTR / 15.500.000$
18) Mercedes-Benz AMG S63 / 20.500.000$
19) Mercedes-Benz AMG G63 / 25.000.000$
20) Lada Vesta Cross / 100.000.000${RES}
{RED}---Airplane---
{RED}не работает(в разработке){RES}
21) Embraer Legacy 500 / 140.000.000$
22) Embraer Legacy 650 / 150.000.000$
23) Bombardier BD-700 Global Express / 200.000.000$
24) Bombardier Challenger 850 Learjet / 230.000.000$
25) Gulfstream V / 300.000.000$
26) Trump's Boeing 757 / 450.000.000$
27) Boeing 747 / 500.000.000$
28) Airbus A340 / 650.000.000$
29) Airbus A380 SuperJumbo Jet / 900.000.000$
30) Boeing 767 / 1.000.000.000$
{RED}---miners---
{RED}не работает(в разработке){RES}
{RED}---businnes---
{RED}не работает(в разработке){RES}
	''')
	all_money = balance()
	buy = int(input('-> '))
	if buy == 0:
		import game
#boosts
	elif buy == 1:	
		if all_money <= 100:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 100:
			all_money -= 100
			print('-100$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			config = open('config.wallet', 'w')
			config.write('5')
			config.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 100
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()

	elif buy == 2:	
		if all_money <= 500:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 500:
			all_money -= 500
			print('-500$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			config = open('config.wallet', 'w')
			config.write('10')
			config.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 500
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()

	elif buy == 3:	
		if all_money <= 1000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 1000:
			all_money -= 1000
			print('-1.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			config = open('config.wallet', 'w')
			config.write('50')
			config.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 1000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()

	elif buy == 4:	
		if all_money <= 10000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 10000:
			all_money -= 10000
			print('-10.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			config = open('config.wallet', 'w')
			config.write('100')
			config.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 10000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
#energy

#Cars
	elif buy == 10:	
		if all_money <= 1500000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 1500000:
			all_money -= 1500000
			print('-1.500.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('Subaru Empreso\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 1500000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()

	elif buy == 11:	
		if all_money <= 5000000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 5000000:
			all_money -= 5000000
			print('-5.000.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('Toyota Landcruser\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 5000000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()
	elif buy == 12:	
		if all_money <= 15000000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 15000000:
			all_money -= 15000000
			print('-15.000.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('Lamborgini Huracan\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 15000000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()
	elif buy == 13:	
		if all_money <= 1000000000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 1000000000:
			all_money -= 1000000000
			print('-1.000.000.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('Bugatti Charon\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 1000000000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()
	elif buy == 14:	
		if all_money <= 10000000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 10000000:
			all_money -= 10000000
			print('-10.000.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('BMW M5 competition\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 10000000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()
	elif buy == 15:	
		if all_money <= 10500000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 10500000:
			all_money -= 10500000
			print('-10.500.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('Tesla model Y\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 10500000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()
	elif buy == 16:	
		if all_money <= 20000000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 20000000:
			all_money -= 20000000
			print('-20.000.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('Ford Mustang\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 20000000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()
	elif buy == 17:	
		if all_money <= 15500000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 15500000:
			all_money -= 15500000
			print('-15.500.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('Nissan GTR\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 15500000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()
	elif buy == 18:	
		if all_money <= 20500000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 20500000:
			all_money -= 20500000
			print('-20.500.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('Mercedes-Benz AMG S63\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 20500000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()
	elif buy == 19:	
		if all_money <= 25000000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 25000000:
			all_money -= 25000000
			print('-25.000.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('Mercedes-Benz AMG G63\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 25000000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()
	elif buy == 20:	
		if all_money <= 100000000:
			print(f'{RED}Упс! Недостаточно средств!{RES}')
		elif all_money >= 100000000:
			all_money -= 100000000
			print('-100.000.000$')
			print(f'{GR}Balance: {RES}{all_money}$')
			a_money = open('money.wallet', 'w')
			a_money.write(str(all_money))
			a_money.close()
			car = open('my_cars.dat', 'a+')
			car.write('Lada Vesta Cross\n')
			car.close()
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[1])
			data_money += 100000000
			data = open('all.dat', 'w')
			data.write(f'{data_line[0]}\n{data_money}\n{data_line[2]}\n{data_line[3]}')
			data.close()
			cars_check.cars_up()
#Airplane

		else:
			print('Возникла ошибка!')
	os.system('cls')
	import game
	game.start()