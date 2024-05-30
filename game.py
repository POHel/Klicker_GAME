import time
import colorama
from colorama import Fore
import sys
import os
import config
colorama.init()
global balance
def balance():
	money = open('money.wallet', 'r')
	line = money.readline()
	money.close()
	balance = int(line)
	return balance


#colors
RES = Fore.RESET
RED = Fore.RED
GR = Fore.GREEN
MAG = Fore.MAGENTA
YE = Fore.YELLOW
WH = Fore.WHITE

#about
print(f'{GR}Tunder SOFT.corp{RES}')
print(f'{MAG}By SKATT{RES}')

#functions
def my_cars():
	cars = open('my_cars.dat', 'r')
	rez = sorted(cars.read().splitlines())
	print('MY CARS:\n')
	for n, item in enumerate(rez):
		print(n+1, item)
	start()


def klic():
	print(f'{GR}Balance: {RES}{balance()}$')
	kl = int(input('1 - начать кликать\n2 - остановить кликер\n-> '))
	if kl == 1:
		try:
			data = open('all.dat', 'r')
			data_line = data.read().splitlines()
			data.close()
			data_money = int(data_line[0])
			money = balance()
			tap = ''
			print('Тапай на клавижу ENTER!')
			while tap != '2':
				tap = input('>')
				print(f'+{config.tap}$')
				money += config.tap
				data_money += config.tap
				print(f'{GR}Balance: {RES}{money}$')
				data = open('all.dat', 'w')
				data.write(f'{data_money}\n{data_line[1]}\n{data_line[2]}\n{data_line[3]}')
				data.close()
				all_money = open('money.wallet', 'w')
				all_money.write(str(money))
			all_money.close()
			os.system('cls')
			start()
		except KeyboardInterrupt:
			all_money.close()
			os.system('cls')

			start()

	elif kl == 2:
		print('Ok!')
	else:
		print('log: error_num')

def bank():
	print()

def business():
	print()

#display
def start():
	print(f'''
{GR}Tunder Game{RED} {config.ver}{RES}
{GR}Баланс: {WH}{balance()}${RES}
{YE}
Меню:
1) Кликер
2) Магазин
{RES}
--3) Банк---{RED}не работает(в разработке){RES}
--4) Бизнесы---{RED}не работает(в разработке){RES}
{YE}
5) Мои Машины
6) Мои Самолёты
7) Сведения
8) Выйти
{RES}
	''')
	num = int(input('-> '))
	if num == 1:
		klic()
	elif num == 2:
		import shop_tool
		shop_tool.shop()
	elif num == 3:
		bank()
	elif num == 4:
		business()
	elif num == 5:
		my_cars()
		
	elif num == 7:
		import all_data
		all_data.data()
		start()
	elif num == 8:
		sys.exit()	
	else:
		print('log: error_num')
	

start()