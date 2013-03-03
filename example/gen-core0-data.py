#!/usr/bin/python

import random

NUM_ITEMS = 1000
print "id,item_id,name,year,month,shipping_method,us_sold,ca_sold,fr_sold,uk_sold"
for item_id in range(0, NUM_ITEMS):
    for year in range(1990, 2014):
        for month in range(1, 13):
	    for shipping_method in range(0, 4):
		id = (item_id - NUM_ITEMS / 2) * 1000000 + year * 1000 + month * 10 + shipping_method
		name = "item %d"%item_id
		us_sold = random.randint(0, 10000)
		ca_sold = random.randint(0, 10000)
		fr_sold = random.randint(0, 10000)
		uk_sold = random.randint(0, 10000)
		print "%d,%d,%s,%d,%d,%d,%d,%d,%d,%d"%(
		     id, item_id, name, year, month, shipping_method,
		     us_sold, ca_sold,fr_sold, uk_sold)
