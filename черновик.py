from random import randint


def color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(100, 255)
    return (red, green, blue)


l1 = int()



class Privret:
    def __init__(self, colvo):
        self.colvo = colvo



import time
from threading import Thread
an = 1
ans = 0

def countdown():
  time.sleep (3)
  if not ans:
    print ('\nВремя вышло!')
    global an
    an = 0

def answer():
        global ans
        ans = int(input('Ваш вариант ответа:'))
        if ans == 1 and an:
            print('Вы ответили правильно!')
        elif ans == 2 and an:
            print('Вы ответили не правильно!')
        else:
            ans = 3
print('Вы не ответили')
print('Газон зеленый')
print('1 - Правда')
print('2 - Ложь')
