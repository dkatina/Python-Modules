#import module
import math #Best usecase (not demonstrated) is to import at the top of the page
#https://docs.python.org/3/library/math.html

#square root
root = math.sqrt(30)
print(root)

#round root up
up = math.ceil(root)
print(up)

#round root down
down = math.floor(root)
print(down)


#import module as alias
import datetime as dt

import pytz as tz #not standard we did download this

date = dt.datetime.today()
print(date)
eastern = tz.timezone('US/Eastern')
print(eastern)

loc_time = dt.datetime.now(eastern)
print(loc_time)

fmt = '%Y-%m-%d %H:%M:%S %Z%z'
print(loc_time.strftime(fmt))

#from module import function
from collections import Counter

colors = ['red', 'blue', 'black', 'black','white','green', 'green', 'blue', 'orange', 'blue', 'green']

color_count = Counter(colors)
print(color_count)