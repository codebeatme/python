'''
本節文章
https://learnscript.net/zh-hant/python/senior/define-and-call-nested-functions/ 如何定義和呼叫巢狀函式
'''

###
def main():
    # 主函式 main，實現一個傻傻的聊天機器人

    ###
    def show_message(text):
        # 巢狀函式 show_message，顯示來自機器人的訊息
        # 加入時間資訊
        import datetime
        time = datetime.datetime.now()

        print(f'{time} 機器人：“{text}”')

    ### 機器人問候使用者
    show_message('你好，我是機器人！')

    # 使用者輸入訊息和機器人對話
    while True:
        text = input('請輸入訊息：')

        if text:
            # 機器人只會傻傻的回答
            show_message('哦，這樣啊！')
        else:
            # 使用者輸入內容為空，跳出迴圈
            break

    # 機器人說再見！
    show_message('謝謝使用，再見！')

main()

# ERROR 找不到函式 show_message
# show_message('你還在嗎？')