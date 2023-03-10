###
class Unit:
    count = 0

    ###
    @staticmethod
    def random_id():
        import random
        return f'id_{random.randint(1,10000000)}'

    ###
    @classmethod
    def show_board(cls):
        print(f'总计{cls.count}个单位')

    ###
    def __init__(self, hp):
        self.id = Unit.random_id()
        self.hp = hp
        Unit.count += 1

###
u1 = Unit(100)
print(f'u1.id={u1.id}')
u1.show_board()