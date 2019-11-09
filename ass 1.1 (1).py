import sys
import os
from random import seed, randrange
from collections import Counter

filename = input('Which data file do you want to use?')
if not os.path.exists(filename):
    print('Sorry, there is no such file.')
    sys.exit()
try:
   linesize  = int(input('Enter a non-negative integer: '))
   if linesize < 0:
      raise ValueError
except ValueError:
    print('Sorry, it is not a valid input')
    sys.exit()
quantity = []
with open(filename) as f:
    quantity = [line.strip() for line in f]    
min_level = 10
all1 = []
c = 0
water = int(input('How many decilitres of water do you want to pour down? '))
water_remaining = water
for i in range(len(quantity)):
    all1 += quantity[i]
level = 1
addition = 0.0

while(water_remaining > 0):
    c += all1.count(level)
    iquantity water_remaining < c:
    
        addition = water_remaining/c
       
        level += addition
        water_remaining = 0
        
    else:
        
        level += 1
        water_remaining = water_remaining - c
        

print("The water rises to {:.2f}".format(level))
