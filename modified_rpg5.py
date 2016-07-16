"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)



class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armorpoints = 0
        self.evadepoints = 2

    def attack(self, enemy):
        if not self.alive():
            return
        double_power = random.random() > .8 # this happens 20% chance to double power points
        if double_power:
            print "%s doubles power with %s during attack" % (self.name, enemy.name)
            enemy.receive_damage(self.power*2)

        super(Hero, self).attack(enemy)

    def receive_damage(self, points):
        if self.armorpoints >0:
            points = points - self.armorpoints
            print "With Armor, your received damage is now %d" % (points)
        else:
            self.health -= points
            print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name
    # def prize(self, enemy):
    #     if enemy.health <= 0:
    #         self.coins += 5
    #         print "%s you defeated %s and gained %d coins! Spend it wisely" % (self.name, enemy.name, self.coins)


    #Making new method for prize_drop to pick up coints
    def receive_coins(self, coins):
        if enemy.health <= 0:
            self.coins += coins


    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)





class Goblin(Character):
    def __init__(self):
        self.name = 'GoblinGoon'
        self.health = 6
        self.power = 2
        self.coins = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'Voldemort'
        self.health = 15
        self.power = 1
        self.coins = 3

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power



#new character, Medic:
class Medic(Character):
    def __init__(self):
        self.name = 'HealingHydra'
        self.health = 5
        self.power = 2
        self.coins = 7

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage" % (self.name, points)
        recuperate_health = random.random() > 0.8
        if recuperate_health:
            self.health = self.health + 2
            print "%s received +2 health points!" % self.name
        if self.health <= 0:
            print "%s is dead. rip." % self.name



#new character, Shadow:
class Shadow(Character):
    def __init__(self):
        self.name = 'Noob Saibot'
        self.health = 1
        self.power = 7
        self.coins = 5

    def receive_damage(self, points):
        chaos_survival = random.random() > 0.9
        if chaos_survival:
            self.health = self.health
            print "Received no damage muawahahhaaaa"
        else:
            self.health-= points
            print "%s received %d damage" % (self.name, points)

        if self.health <= 0:
            print "%s is dead. rip." % self.name

#new character that doesn't die, Zombie
class Zombie(Character):
    def __init__(self):
        self.name = 'th3_Und3ad-R1s3s'
        self.health = 4
        self.power = 1

    def alive(self):
        return True



class Witch(Character):
    def __init__(self):
        self.name = 'Rita Repulsa'
        self.health = 20
        self.power = 1
        self.coins = 10

    def attack(self, hero):
        swap_health = random.random() > 0.6
        if swap_health:
            print "%s swaps health with %s during attack" % (self.name, hero.name)
            self.health, hero.health = hero.health, self.health
        super(Witch, self).attack(hero)
        if swap_health:
            self.health, hero.health = hero.health, self.health

class Chimera(Character):
    def __init__(self):
        self.name = 'Chimera'
        self.health = 30
        self.power = 2
        self.coins = 30

    def attack(self, hero):
        double_vulnerability = random.random() > 0.8 # this happens 20% chance to double power points
        if double_vulnerability:
            print "%s doubles weakness with %s during attack" % (self.name, hero.name)
            hero.receive_damage(self.power*2)
        super(Chimera, self).attack(hero)

    def receive_damage(self, points):
        chaos_survival = random.random() > 0.4
        if chaos_survival:
            self.health = self.health
            print "Received no damage, prepare to meet your doom!"
        else:
            self.health-= points
            print "%s received %d damage" % (self.name, points)

        if self.health <= 0:
            print "%s is dead. rip." % self.name


class Battle(object):
    def do_battle(self, hero, enemy):
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
#evadepoints factored
            if hero.evadepoints > 0:
                print "Hero evade points are %d" % (hero.evadepoints)
                evade_chances = hero.evadepoints * 0.05
                print "Evade chances are %f" % (evade_chances)
                evade_or_not = random.random() > evade_chances
                print "Evade prob is %s" % evade_or_not
                if evade_or_not:
                    print "%s evaded attack!" % hero.name
                else:
                    print "Too bad, you weren't able to evade attack"
                    enemy.attack(hero)
            else:
                enemy.attack(hero)


        if hero.alive():
            print "You defeated the %s" % enemy.name
            hero.receive_coins(enemy.coins)
            print "%s received %d coins." % (hero.name, enemy.coins)
            return True
        else:
            print "YOU LOSE!"
            return False








class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class SuperTonic(object):
    cost = 10
    name = 'tonic'
    def apply(self, character):
        character.health += 10
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, character):
        character.power += 2
        print "%s's power increased to %d." % (character.name, character.power)

class StoneArmor(object):
    cost = 8
    name = 'StoneArmor'
    def apply(self, character):
        character.armorpoints += 2
        print "%s's armor defense increases to %d." % (character.name, character.armorpoints)

class ProbabilityArmor(object):
    cost = 13
    name = 'ProbabilityArmor'
    def apply(self, character):
        armorpower = random.random() > 0.6
        if armorpower:
            character.armorpoints += 5
            print "Congrats! %s's armor defense increases to %d." % (character.name, character.armorpoints)
        else:
            character.armorpoints += 0
            print "Too bad, %s's armor defense doesn't increase at all" % (character.name)

class Evade(object):
    cost = 7
    name = 'Evade'
    def apply(self, character):
        character.evadepoints += 2
        print "%s's evade points have increased to %d" % (character.name, character.evadepoints)



class Shopping(object):
    items = [Tonic, Sword, StoneArmor, ProbabilityArmor, Evade]
    def do_shopping(self, hero):
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
enemies = [Goblin(), Wizard(), Medic(), Shadow(), Witch(), Chimera()]
# enemies = [Chimera()]
battle_engine = Battle()
shopping_engine = Shopping()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
