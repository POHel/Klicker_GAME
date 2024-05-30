import os
import sys
def plane_up():
	data = open('all.dat', 'r')
	data_line = data.read().splitlines()
	data.close()
	data_plane = int(data_line[2])
	data_plane += 1
	data = open('all.dat', 'w')
	data.write(f'{data_line[0]}\n{data_line[1]}\n{data_line[2]}\n{data_plane}')
	data.close()
