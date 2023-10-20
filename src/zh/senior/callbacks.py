'''
本节文章
https://learnscript.net/zh/python/senior/implementing-callbacks/ 如何实现回调
'''

# 导入关于线程的模块
import threading


def send(content, callback):
    # 函数 send 将在新的线程中执行，用于将内容发送至服务器

    # 使用 Event 类来模拟与服务器通信所需的时间
    event = threading.Event()
    # 等待 3 秒
    event.wait(3)

    # 使用 callback 将发送结果告知线程创建者
    callback(f'OK！消息 {content} 发送成功')


def sent(result):
    # sent 将作为回调函数，用于显示发送结果
    print(f'发送结果：{result}')


content = input('请输入需要发送的消息：')

# 如果用户输入为空，则不会发送
if content:
    print(f'将消息 {content} 发送至服务器')

    # 使用 Thread 类开启新线程，以执行 send，并将 sent 作为回调函数
    thread = threading.Thread(None, send, None, (content, sent))
    thread.start()
