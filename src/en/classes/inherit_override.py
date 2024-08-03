# A game unit
class Unit:
    # The method used to launch the attack
    def attack(self):
        print('Unit launch an attack')

class Hero(Unit):
    # This method will be overridden by the attack defined later
    def attack(self, times):
        while times > 0:
            print('Hero launch an attack')
            times -= 1

    # This overrides the Unit's attack method and overrides the previously defined attack
    def attack(self, times):
        print(f'Hero will launch {times} attacks')

Unit().attack()
Hero().attack(5)
# ERROR Unable to call the attack method defined by the Unit class
Hero().attack()