'''
本節文章
https://learnscript.net/zh-hant/python/senior/create-and-import-packages/ 如何建立，匯入，使用套件
'''

# 匯入套件 game
import game
# 匯入套件 game 內的模組 player，並設定了別名
import game.player as player

# 呼叫套件內的函式
game.welcome()
# 呼叫模組 player 內的函式
player.show_status()