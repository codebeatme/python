from enum import *

# auto 会返回递增的二的整数次幂
class COLOR(Flag):
    NONE = 0
    WHITE = auto()
    BLACK = auto()
    # 因为 WHITE 为 1，BLACK 为 2，因此 3 是 WHITE 与 BLACK 的组合
    BLACK_AND_WHITE = 3
    RED = auto()
    BLUE = auto()
    GREEN = auto()

bw = COLOR.WHITE | COLOR.BLACK
# 显示为 BLACK_AND_WHITE
print(f'{bw.name}={bw.value}')

# 这里不会出现 NONE 和 BLACK_AND_WHITE
for i in COLOR:
	print(f'{i.name}={i.value}')

@verify(NAMED_FLAGS)
class DAY(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    # ERROR 9 不是二的整数次幂，也不是 1，2，4 的某种组合
    # THURSDAY = 9

import enum
print(enum.show_flag_values(COLOR.BLACK_AND_WHITE))

# COLOR 中的 NONE 和 BLACK_AND_WHITE 不会被计算
print(f'COLOR 规范化成员个数：{len(COLOR)}')

# 组合成员 WHITE，BLACK，RED
color = COLOR.WHITE | COLOR.BLACK | COLOR.RED

# 并不会显示非规范化成员 BLACK_AND_WHITE
for i in COLOR.BLACK_AND_WHITE | COLOR.GREEN:
	print(i)

print(f'color 包含 GREEN？{COLOR.GREEN in color}')
print(f'color 包含 RED？{(COLOR.RED & color) == COLOR.RED}')
print(f'color 包含 BLACK_AND_WHITE？{COLOR.BLACK_AND_WHITE in color}')

# color 是 WHITE，BLACK，RED 的组合
print(f'color 组合中规范化成员的个数为：{len(color)}')

# color 是 WHITE，BLACK，RED 的组合
print(f'color 组合是否为空？{not bool(color)}')
print(f'NONE 是否为空？{not bool(COLOR.NONE)}')

# 从 color 中移除 WHITE 和 BLACK
print(color ^ COLOR.BLACK_AND_WHITE)
# 由于 color 不包含 GREEN，因此 GREEN 将被添加
print(color ^ COLOR.GREEN)

# 获取 WHITE，BLACK，RED 以外的成员
print(~color)
# 获取其他所有成员
print(~COLOR.NONE)

class CONFORMCOLOR(Flag, boundary=CONFORM):
    WHITE = auto()
    BLACK = auto()

# 值为 4 的成员将被移除
print(CONFORMCOLOR(5))

class EJECTCOLOR(Flag, boundary=EJECT):
    WHITE = auto()
    BLACK = auto()

# 结果为整数 5，不再是标志成员
print(EJECTCOLOR(5))

class KEEPCOLOR(Flag, boundary=KEEP):
    WHITE = auto()
    BLACK = auto()

# 4 将被保留
print(KEEPCOLOR(5))

class STRICTCOLOR(Flag, boundary=STRICT):
    WHITE = auto()
    BLACK = auto()

print(STRICTCOLOR(3))
# ERROR 值为 4 的成员并未定义
# print(STRICTCOLOR(5))

class INTCOLOR(IntFlag):
    WHITE = auto()
    BLACK = auto()

# 参与比较
print(INTCOLOR.WHITE > 0)
# 参与算术运算，结果将不再是一个标志成员
print(type(INTCOLOR.WHITE + INTCOLOR.BLACK))
