# 视频内容：「Python」高级教程 什么是内部函数？内部函数的作用，如何定义内部函数
# 视频地址：https://www.bilibili.com/video/BV1J54y1u7Vo/

###
def main():

    ###
    def show_message(text):
        import datetime
        now = datetime.datetime.now()
        print(f'{now} 机器人：“{text}”')

    ###
    show_message('你好，我是机器人！')

    while True:
        text = input('请输入消息：')

        if text:
            show_message('哦，这样啊！')
        else:
            break

    show_message('谢谢使用！')

main()