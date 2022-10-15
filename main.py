# -*- coding: utf-8 -*-
import random

# основные параметры
lenght_bur = 10
health = 100
respect = 20
weight = 30
# ------------------

# Вес существ
weight_creature1 = 30
weight_creature2 = 50
weight_creature3 = 70
# ------------------

#! Функуии
def basic_value():
   print('Ваша текущаю длина норы:', lenght_bur)
   print('Ваше текущее здоровье:', health)
   print('Ваше текущее уважение:', respect)
   print('Ваш текущий вес:', weight)
# !---------------

# Начальное вступление
print('Добро пожаловать в игру')
print('Игра представляет собой текстовый квест, в котором вам предстоит управлять существом. Управление осуществляется в консоли при помощи цифр. То есть на каждом шаге вам выдаются все его параметры и задается вопрос, "что он собирается делать?", с вариантами ответа, пронумерованными цифрами.')
print('Ваша задача, играя за кролика, добиться уважения больше 100 и не дать основным параметрам упасть до нуля')
# --------------------


while respect < 101:
   if lenght_bur <= 0 or health <= 0 or respect <= 0 or weight <= 0:
      print('Вы проиграли')
      exit()
   else:
      print('Выберите действие:')
      user_choice = int(input()) # выбор действия
      if user_choice == 1: #копать норку
         print('Копает нору')
         print('Выберите с какой интенсивностью он копает норку. 1 - интенсивно; 2 - лениво')
         user_grow = int(input())
         if user_grow == 1:
            print('Копает интенсивно')
            lenght_bur += 5
            health -= 30
            basic_value()
            if health <= 0:
               print('Вы проиграли')
               exit()
         elif user_grow == 2:
            print('Копает лениво')
            lenght_bur += 2
            health -= 10
            basic_value()
            if health <= 0:
               print('Вы проиграли')
               exit()

      elif user_choice == 2: #поесть травки
         print('Ест травку')
         print('Выберите какую травку он ест. 1 - зеленая травка; 2 - жухлая травка')
         user_grass = int(input())
         if user_grass == 1:
            if health <= 30:
               print('Лохов на лужайку не пускают')
               health -= 30
               print('Вы погибли')
               exit()
            else:
               print('Ест зеленую травку')
               health += 30
               weight += 30
               basic_value()
         elif user_grass == 2:
            print('Ест жухлую травку')
            health += 10
            weight += 15
            basic_value()

      elif user_choice == 3: #борьба
         print('Идет драться')
         print('Выберете существо')
         user_creature = int(input())
# первое существо
         if user_creature == 1:
            win_chance1 = random.randint(1, weight + weight_creature1)
            if win_chance1 <= weight:
               print('Вы победили')
               if weight > weight_creature1:
                  respect += weight - weight_creature1
                  health -= 5
               elif weight < weight_creature1:
                  respect += weight_creature1 - weight
                  health -= 5
               else:
                  respect += random.randint(1, 10)
                  health -= 5
               basic_value()
            else:
               print('Вы проиграли')
               if weight > weight_creature1:
                  respect -= weight - weight_creature1
                  health -= 10
               elif weight < weight_creature1:
                  respect -= weight_creature1 - weight
                  health -= 10
               else:
                  respect -= random.randint(1, 10)
                  health -= 10
               basic_value()
               if health < 0 or respect < 0:
                  print('Вы проиграли')
                  exit()
# второе существо
         if user_creature == 2:
            win_chance2 = random.randint(1, weight + weight_creature2)
            if win_chance2 <= weight:
               print('Вы победили')
               if weight > weight_creature2:
                  respect += weight - weight_creature2
                  health -= 5
               elif weight < weight_creature2:
                  respect += weight_creature2 - weight
                  health -= 5
               else:
                  respect += random.randint(5, 15)
                  health -= 5
               basic_value()
            else:
               print('Вы проиграли')
               if weight > weight_creature2:
                  respect -= weight - weight_creature2
                  health -= 20
               elif weight < weight_creature2:
                  respect -= weight_creature2 - weight
                  health -= 20
               else:
                  respect -= random.randint(5, 15)
                  health -= 20
               basic_value()
               if health < 0 or respect < 0:
                  print('Вы проиграли')
                  exit()
# третье существо
         if user_creature == 3:
            win_chance3 = random.randint(1, weight + weight_creature3)
            if win_chance3 <= weight:
               print('Вы победили')
               if weight > weight_creature3:
                  respect += weight - weight_creature3
                  health -= 5
               elif weight < weight_creature3:
                  respect += weight_creature3 - weight
                  health -= 5
               else:
                  respect += random.randint(10, 20)
                  health -= 5
               basic_value()
            else:
               print('Вы проиграли в драке')
               if weight > weight_creature3:
                  respect -= weight - weight_creature3
                  health -= 30
               elif weight < weight_creature3:
                  respect -= weight_creature3 - weight
                  health -= 30
               else:
                  respect -= random.randint(10, 20)
                  health -= 20
               basic_value()
               if health < 0 or respect < 0:
                  print('Вы проиграли')
                  exit()

      elif user_choice == 4: #проспать весь день
         print('Кролик проспал весь день')
         lenght_bur -= 2
         health += 20
         respect -= 2
         weight -= 5
         basic_value()
         if lenght_bur <= 0 or  respect <= 0 or weight <= 0:
            print('Вы проиграли')
            exit()

   print('Наступила ночь')
   lenght_bur -= 2
   health += 20
   respect -= 2
   weight += 5
   basic_value()

if respect > 101:
   print('Вы победили!!!')
