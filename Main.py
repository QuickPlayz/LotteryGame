import random
import itertools

lott = ''.join((random.choice('1234567890') for i in range(2)))

print('-------------------')
print('Enter a Code for a Lottery Ticket')
print('(it is a 2 digit code)')
print('-------------------')
code = input()

print("".join(['The Winning Code Was ' , lott ]))
print('-------------------')

if code == lott:
  money = ''.join((random.choice('1234567890') for i in range(7)))
  
  print("".join(['YaY You Won $' , money ]))
  
else : 
    print('You Lost :(')
    
quit()
