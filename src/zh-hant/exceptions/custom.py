# 定義一個新的例外狀況 NicknameError
class NicknameError(Exception):

    def __init__(self, *args):
        super().__init__(*args)
        # 將第一個和第二個位置參數作為使用者昵稱和提示資訊
        (nickname, msg) = args
        # 為例外狀況新增註解
        self.add_note(f'糟糕，昵稱“{nickname}”出問題了！{msg}')
        print(self.__notes__)

# 擲回例外狀況 NicknameError
raise NicknameError('Test', '不被允許的昵稱')
