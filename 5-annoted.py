"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object): # Make a class named Character that inherits an object
    def alive(self): # Method alive takes self
        return self.health > 0

    def attack(self, enemy): #Method attack takes self and enemy
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power) # From the enemy, take the method called receive_damage and call it with parametes self and self.power
        time.sleep(1.5) #From time get the sleep method and call it with parameters self and 1.5

    def receive_damage(self, points): #  Method receive_damage takes parameters self and oints
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self): #Method print_Status takes parameters self
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character): # Make a class called Hero that inherits Character
    def __init__(self): # Class Hero has a dunder-init that takes self
        self.name = 'hero' #From self get the name attribute and set it to hero
        self.health = 10 # From self get the health attribute and set it to 10
        self.power = 5 # From self get the power attribute and set it to 5

        self.coins = 20 #From self get the coins attribute and set it to 20

    def restore(self): #Method restore takes parameter self
        self.health = 10 #From self get the health attribute and set it to 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item): # Method Buy takes parameters self and items
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character): #Make a class called Goblin that inherits Character

# Class Gobline has a dunder-init that takes self
    def __init__(self): # Dunder-init takes self
        self.name = 'goblin' # From self take name attribute and set it to goblin
        self.health = 6 #From self take the health attribute and set it to 6
        self.power = 2 #From self take the power attribute and set it to 2

class Wizard(Character): #Make a class called Wizard that inherits the Character

# Class Wizard has a dunder -init that takes self
    def __init__(self): # dunder init takes self
        self.name = 'wizard' # #From self take the name attribute and set it to wizard
        self.health = 8 # From the self, take the health attribte and set it to 8
        self.power = 1 # From the self take the power attribute and set it to 1

    def attack(self, enemy): # Method attack takes parameters self and enemy
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object): #class Battle inherits an object
    def do_battle(self, hero, enemy): # Method do_battle takes parameters serlf, hero, enemy
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object): #Make a class called Tonic that inherits object
    cost = 5
    name = 'tonic'
    def apply(self, character): #Method apply takes parameters self and character
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object): #Class Sword inherits object
    cost = 10
    name = 'sword'
    def apply(self, character): #Method apply takes parameters self and character
        character.power += 2
        print "%s's power increased to %d." % (character.name, character.power)

class Shopping(object): #Make a class called shopping that inherits object
    items = [Tonic, Sword]
    def do_shopping(self, hero): #Method do_shopping takes parameters self and hero
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Shopping.items)):
                item = Shopping.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Shopping.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Wizard()]
battle_engine = Battle()
shopping_engine = Shopping()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
