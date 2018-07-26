                                     #-----------------FIRE LOG WATER-----------------------
# Developed By : Sanyam Sood ^-^

#  https://trinket.io/embed/python/33e5c3b81b#.W1lgZdUzbIU

print ('Welcome to THE GAME ^-^')
print ('Before We Begin Lets know the basics')
 
print('WATER extinguishes The FIRE !!!')
print('FIRE Burns The LOG !!!')
print('LOG cuts the WATER Power!!!')
 
from random import randint
player=input('Choose Fire (f) , Log (l) or Water(w) ')

while player!='f' and player!='l' and player!='w':
  print('ENTER A VALID OPTION !!')
  player=input('Choose Fire (f) , Log (l) or Water(w) ')
  
print(player)
print('vs')

chosen=randint(1,3)

if chosen==1:
  computer='f'
  
elif chosen==2:
  computer='l'
  
else:
  computer='w'
 
print (computer)

if player==computer:
  print('DRAW !!!')

elif player=='f' and computer=='l':
  print('FIRE Burns The LOG !!!')
  print('You WIN !!!')

elif player=='f'and computer=='w':
  print('WATER extinguishes The FIRE !!!')
  print('You LOSE !!!')

elif player=='w' and computer=='f':
  print('WATER extinguishes The FIRE !!!')
  print('You WIN !!!')
  
elif player=='w'and computer=='l':
  print('LOG cuts the WATER Power!!!')
  print('You LOSE!!!')

elif player=='l' and computer=='w':
  print('LOG cuts the WATER Power!!!')
  print('You WIN !!!')

elif player=='l'and computer=='f':
  print('FIRE Burns The LOG !!!')
  print('You LOSE !!!')
