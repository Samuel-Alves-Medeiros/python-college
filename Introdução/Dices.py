import random

lista = [1,2,3,4,5,6,7,8, ]

ROLL = input('Selet a Dice (RollDx) ')
bonus = int(input('Bonus: '))

if bonus == '':
   bonus == 0


def RollD4(bonus = 0):
   res = random.randint(1,4)
   return f'Dice: {res}, Bonus: {bonus}, FinalRes: {res + bonus}'

def RollD6(bonus = 0):
   res = random.randint(1,6)
   return f'Dice: {res}, Bonus: {bonus}, FinalRes: {res + bonus}'

def RollD8(bonus = 0):
   res = random.randint(1,8)
   return f'Dice: {res}, Bonus: {bonus}, FinalRes: {res + bonus}'

def RollD10(bonus = 0):
   res = random.randint(1,10)
   return f'Dice: {res}, Bonus: {bonus}, FinalRes: {res + bonus}'

def RollD12(bonus = 0):
   res = random.randint(1,12)
   return f'Dice: {res}, Bonus: {bonus}, FinalRes: {res + bonus}'

def RollD20(bonus = 0):
   res = random.randint(1,20)
   return f'Dice: {res}, Bonus: {bonus}, FinalRes: {res + bonus}'

match ROLL:
   case 'RollD4':
      print(RollD4(bonus))

   case 'RollD6':
      print(RollD6(bonus))

   case 'RollD8':
      print(RollD8(bonus))

   case 'RollD10':
      print(RollD10(bonus))

   case 'RollD12':
      print(RollD12(bonus))

   case 'RollD20':
      print(RollD20(bonus))

