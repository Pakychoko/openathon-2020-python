# Crea varios personajes y crea un método lucha que recibirá dos parámetros, de tipo Hero y en base al nivel de poder mostrará un saludo o otro. 
# Por cierto comprueba que los parámetros no sean nulos.

from Hero import *

batman = Hero('Batman','Male', 'Soy batman', 80)
wolverine = Hero('Wolverine', 'Male', 'Que quereis capuyos', 95)
allmight = Hero('All Might', 'Male', 'All for one!', 100)

def fight(hero1, hero2):
    if hero1.nivel < hero2.nivel:
        print(hero2.nombre + ': ' + hero2.saludo)
    elif hero1.nivel > hero2.nivel:
        print(hero1.nombre + ': ' + hero1.saludo)
    else:
        print('La hostia, somos igual de fuertes!')

def selectHero(seleccion):
    if seleccion == '1':
        return batman
    elif seleccion == '2':
        return wolverine
    elif seleccion == '3':
        return allmight

print('Elige el primer heroe: \n 1. Batman \n 2. Wolverine \n 3. All Might')
hero1 = selectHero(input())

print('Elige el segundo heroe: \n 1. Batman \n 2. Wolverine \n 3. All Might')
hero2 = selectHero(input())

fight(hero1, hero2)