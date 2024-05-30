#energy data
import os
import time
import sys
import datetime
'''
energy = open('energy.wallet', 'r')

energy.close()
'''
from datetime import datetime 
now = datetime.now() 
current_time = now.strftime("%H:%M") 
print("Current Time =", current_time)