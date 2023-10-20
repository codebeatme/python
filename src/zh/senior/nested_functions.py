'''
本节文章
https://learnscript.net/zh/python/senior/define-and-call-nested-functions/ 如何定义和调用嵌套函数
'''

###
def main():
    # 主函数 main，实现一个傻傻的聊天机器人

    ###
    def show_message(text):
        # 嵌套函数 show_message，显示来自机器人的消息
        # 加入时间信息
        import datetime
        time = datetime.datetime.now()

        print(f'{time} 机器人：“{text}”')

    ### 机器人问候用户
    show_message('你好，我是机器人！')

    # 用户输入消息和机器人对话
    while True:
        text = input('请输入消息：')

        if text:
            # 机器人只会傻傻的回答
            show_message('哦，这样啊！')
        else:
            # 用户输入内容为空，跳出循环
            break

    # 机器人说再见！
    show_message('谢谢使用，再见！')

main()

# ERROR 找不到函数 show_message
# show_message('你还在吗？')