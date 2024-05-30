def money():
	money = open('money.wallet', 'r')
	line = money.readline()
	money.close()
	return line
