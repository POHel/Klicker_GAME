import colorama
from colorama import Fore
colorama.init()
data = open('all.dat', 'r')
data_line = data.read().splitlines()
data.close()

def data():
	print(f'''
{Fore.GREEN}Всего заработано: {Fore.YELLOW}{data_line[0]}$
{Fore.GREEN}Всего потрачено: {Fore.YELLOW}{data_line[1]}$
{Fore.GREEN}Всего машин: {Fore.YELLOW}{data_line[2]} шт
{Fore.GREEN}Всего самолётов: {Fore.YELLOW}{data_line[3]} шт
	''')