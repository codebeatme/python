###
class Unit:
    count = 0

    def __init__(self, hp):
        self.hp = hp
        self.dead = False
        Unit.count += 1

###
u1 = Unit(10)
u2 = Unit(10)
print(f'Unit.count={Unit.count}')
print(f'u1.count={u1.count}')
print(f'u2.count={u2.count}')

u1.count = 0
u3 = Unit(10)
print(f'u1.count={u1.count}')
print(f'u2.count={u2.count}')
print(f'u3.count={u3.count}')
print(f'Unit.count={Unit.count}')
