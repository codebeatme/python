###
defence = 10

###
def hurt(damage):
    # defence = 14
    global defence
    damage -= defence
    defence -= 1
    
    if damage <= 0:
        return

    def show(text):
        print(text)

    message = f'考虑防御值后的伤害为{damage}'
    show(message)

    global health_point
    health_point = 100

###
hurt(15)
hurt(15)
print(health_point)