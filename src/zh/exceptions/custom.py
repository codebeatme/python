# 定义一个新的异常 NicknameError
class NicknameError(Exception):

    def __init__(self, *args):
        super().__init__(*args)
        # 将第一个和第二个位置参数作为用户昵称和提示信息
        (nickname, msg) = args
        # 为异常添加注释
        self.add_note(f'糟糕，昵称“{nickname}”出问题了！{msg}')
        print(self.__notes__)

# 抛出异常 NicknameError
raise NicknameError('Test', '不被允许的昵称')
