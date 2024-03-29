from enum import *

# auto 會傳回遞增的二的整數次冪
class COLOR(Flag):
    NONE = 0
    WHITE = auto()
    BLACK = auto()
    # 因為 WHITE 為 1，BLACK 為 2，因此 3 是 WHITE 與 BLACK 的組合
    BLACK_AND_WHITE = 3
    RED = auto()
    BLUE = auto()
    GREEN = auto()

bw = COLOR.WHITE | COLOR.BLACK
# 顯示為 BLACK_AND_WHITE
print(f'{bw.name}={bw.value}')

# 這裏不會出現 NONE 和 BLACK_AND_WHITE
for i in COLOR:
	print(f'{i.name}={i.value}')

@verify(NAMED_FLAGS)
class DAY(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    # ERROR 9 不是二的整數次冪，也不是 1，2，4 的某種組合
    # THURSDAY = 9

import enum
print(enum.show_flag_values(COLOR.BLACK_AND_WHITE))

# COLOR 中的 NONE 和 BLACK_AND_WHITE 不會被計算
print(f'COLOR 正規化成員個數：{len(COLOR)}')

# 組合成員 WHITE，BLACK，RED
color = COLOR.WHITE | COLOR.BLACK | COLOR.RED

# 並不會顯示非正規化成員 BLACK_AND_WHITE
for i in COLOR.BLACK_AND_WHITE | COLOR.GREEN:
	print(i)

print(f'color 包含 GREEN？{COLOR.GREEN in color}')
print(f'color 包含 RED？{(COLOR.RED & color) == COLOR.RED}')
print(f'color 包含 BLACK_AND_WHITE？{COLOR.BLACK_AND_WHITE in color}')

# color 是 WHITE，BLACK，RED 的組合
print(f'color 組合中正規化成員的個數為：{len(color)}')

# color 是 WHITE，BLACK，RED 的組合
print(f'color 組合是否為空？{not bool(color)}')
print(f'NONE 是否為空？{not bool(COLOR.NONE)}')

# 從 color 中移除 WHITE 和 BLACK
print(color ^ COLOR.BLACK_AND_WHITE)
# 由於 color 不包含 GREEN，因此 GREEN 將被新增
print(color ^ COLOR.GREEN)

# 取得 WHITE，BLACK，RED 以外的成員
print(~color)
# 取得其他所有成員
print(~COLOR.NONE)

class CONFORMCOLOR(Flag, boundary=CONFORM):
    WHITE = auto()
    BLACK = auto()

# 值為 4 的成員將被移除
print(CONFORMCOLOR(5))

class EJECTCOLOR(Flag, boundary=EJECT):
    WHITE = auto()
    BLACK = auto()

# 結果為整數 5，不再是旗標成員
print(EJECTCOLOR(5))

class KEEPCOLOR(Flag, boundary=KEEP):
    WHITE = auto()
    BLACK = auto()

# 4 將被保留
print(KEEPCOLOR(5))

class STRICTCOLOR(Flag, boundary=STRICT):
    WHITE = auto()
    BLACK = auto()

print(STRICTCOLOR(3))
# ERROR 值為 4 的成員並未定義
# print(STRICTCOLOR(5))

class INTCOLOR(IntFlag):
    WHITE = auto()
    BLACK = auto()

# 參與比較
print(INTCOLOR.WHITE > 0)
# 參與算術運算，結果將不再是一個旗標成員
print(type(INTCOLOR.WHITE + INTCOLOR.BLACK))
