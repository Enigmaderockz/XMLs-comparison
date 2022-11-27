import re
from datetime import datetime

filename = "show_data_paris_20211123456868.dat"


regex = re.compile(r'\d+')
x = regex.findall(filename)[0]
y = x[:8]
print('-'.join([y[:4], y[4:6], y[6:]]))
