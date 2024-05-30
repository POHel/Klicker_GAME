import os
import sys
def cars_up():
	data = open('all.dat', 'r')
	data_line = data.read().splitlines()
	data.close()
	data_cars = int(data_line[2])
	data_cars += 1
	data = open('all.dat', 'w')
	data.write(f'{data_line[0]}\n{data_line[1]}\n{data_cars}\n{data_line[3]}')
	data.close()
