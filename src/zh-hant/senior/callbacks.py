# 匯入關於執行緒的模組
import threading


def send(content, callback):
    # 函式 send 將在新的執行緒中執行，用於將內容發送至伺服器

    # 使用 Event 類別來模擬與伺服器通信所需的時間
    event = threading.Event()
    # 等待 3 秒
    event.wait(3)

    # 使用 callback 將發送結果告知執行緒建立者
    callback(f'OK！訊息 {content} 發送成功')


def sent(result):
    # sent 將作為回呼函式，用於顯示發送結果
    print(f'發送結果：{result}')


content = input('請輸入需要發送的訊息：')

# 如果使用者輸入為空，則不會發送
if content:
    print(f'將訊息 {content} 發送至伺服器')

    # 使用 Thread 類別開啟新執行緒，以執行 send，並將 sent 作為回呼函式
    thread = threading.Thread(None, send, None, (content, sent))
    thread.start()
