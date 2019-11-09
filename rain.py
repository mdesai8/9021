import sys
import os

filename = input('Which data file do you want to use?')
if filename != "land.txt":
    print('Sorry, there is no such file.')
    sys.exit()
try:
   water = int(input('How many decilitres of water do you want to pour down? '))
   if water < 0:
      raise ValueError
except ValueError:
    print('Sorry, it is not a valid input')
    sys.exit()
quantity = []
lines = []
with open("land.txt") as f:
    lines = [line.split() for line in f]
for i in lines:
    for j in range(len(i)):
        quantity.append(i[j])
min_level = 10
c = 0

water_remaining = water
level = 1
addition = 0.0

while(water_remaining > 0):
    c += quantity.count(level)
    if water_remaining < c:
        addition = water_remaining/c
        level += addition
        water_remaining = 0
        
    else:
        
        level += 1
        water_remaining = water_remaining - c
        

print("The water rises to {:.2f} centimeters".format(level))
