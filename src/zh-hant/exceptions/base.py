import sys

try:
    sys.exit()
except BaseException as e:
    # 例外狀況 SystemExit 將被擷取
    print(f'擷取到了例外狀況 {type(e)}')

# 下面的陳述式會被執行
print('sys.exit() 似乎沒有作用哦！')