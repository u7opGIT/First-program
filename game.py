import time
import random
from colorama import Fore, Back, Style, init
print("Могут быть ошибки в переводе")
time.sleep(2)
init()
q = "Камень"
w = "Ножницы"
e = "Бумага"
def go():
	print(Fore.BLUE + "Игра камень ножницы бумага")
	print(Fore.BLUE + "Выберите вещь")
	print(Fore.BLUE + " 1 -- Камень/ 2 -- Ножницы/ 3 -- Бумага")
	c = input("")
	while c != "1" and c != "2" and c != "3":
		print(Back.RED + Fore.WHITE + "Необходимо вводить число!")
		print(Back.RED + Fore.WHITE + "Попробуй снова!")
		print(Back.BLACK)
		print(Fore.WHITE)
		c = input("")

	b = int(c)

	a = random.randint(1, 3)
	time.sleep(0.3)
	if b == 1:
		if a == 1:
			print(Fore.WHITE + "Вы:                  Камень")
			time.sleep(0.5)
			print(Fore.WHITE + "Противник:           Камень")
			print(Back.BLUE + Fore.WHITE + "Результат игры:      Ничья!")
		elif a == 2:
			print(Fore.WHITE + "Вы                   Камень")
			time.sleep(0.5)
			print(Fore.WHITE + "Противник:           Ножницы")
			print(Back.GREEN + Fore.WHITE + "Результат игры       Вы победили!")
		elif a == 3:
			print(Fore.WHITE + "Вы:                  Камень")
			time.sleep(0.5)
			print(Fore.WHITE + "Противник:           Бумага")
			print(Back.RED + Fore.WHITE + "Результат игры:      Ви проиграли!")
 
	elif b == 2:
		if a == 1:
			print(Fore.WHITE + "Вы:                  Ножницы")
			time.sleep(0.5)
			print(Fore.WHITE + "Противник:           Камень")
			print(Back.RED + Fore.WHITE + "Результат игры:      Ви проирали!")

		elif a == 2:
			print(Fore.WHITE + "Вы:                  Ножницы")
			time.sleep(0.5)
			print(Fore.WHITE + "Противник:           Ножницы")
			print(Back.BLUE + Fore.WHITE + "Результат игры:      Ничья!")

		elif a == 3:
			print(Fore.WHITE + "Вы:                  Ножницы")
			time.sleep(0.5)
			print(Fore.WHITE + "Противник:           Бумага")
			print(Back.GREEN + Fore.WHITE + "Результат игры:      Ви проиграли!")
	elif b == 3:
		if a == 1:
			print(Fore.WHITE + "Вы:                  Бумага")
			time.sleep(0.5)
			print(Fore.WHITE + "Противник:           Камень")
			print(Back.GREEN + Fore.WHITE + "Результат игры:      Ви победили!")
		elif a == 2:
			print(Fore.WHITE + "Вы:                  Бумага")
			time.sleep(0.5)
			print(Fore.WHITE + "Противник:           Ножницы")
			print(Back.RED + Fore.WHITE + "Результат игры:      Ви проиграли!")
		elif a == 3:
			print(Fore.WHITE + "Вы:                  Бумага")
			time.sleep(0.5)
			print(Fore.WHITE + "Противник:           Бумага")
			print(Back.BLUE + Fore.WHITE + "Результат игры       Ничья!")



go()
time.sleep(1)

while True:
	print(Back.BLACK)
	print(Fore.WHITE)
	print("Ещё раз?")
	print("y/n")
	v = input("")
	h = v.title()
	if h == "Y":
		go()
	else:
		break