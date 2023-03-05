###
defence = 10

###
def hurt(damage):
    # defence = 14
    damage -= defence
    
    if damage <= 0:
        return

    def show(text):
        print(text)

    message = f'考虑防御值后的伤害为{damage}'
    show(message)

###
hurt(15)