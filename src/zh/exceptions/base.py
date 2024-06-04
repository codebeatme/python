import sys

try:
    sys.exit()
except BaseException as e:
    # 异常 SystemExit 将被捕获
    print(f'捕获到了异常 {type(e)}')

# 下面的语句会被执行
print('sys.exit() 似乎没有作用哦！')