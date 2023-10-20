'''
本节文章
https://learnscript.net/zh/python/senior/create-and-import-packages/ 如何创建，导入，使用包
'''

# 导入包 game
import game
# 导入包 game 内的模块 player，并设置了别名
import game.player as player

# 调用包内的函数
game.welcome()
# 调用模块 player 内的函数
player.show_status()