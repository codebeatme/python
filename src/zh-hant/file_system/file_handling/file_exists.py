# 請將命令列跳躍至腳本檔案 file_exists.py 所在的目錄，然後執行他
# 使用 r 模式開啟不存在的檔案 no.md
try: open('no.md', 'r')
except FileNotFoundError as e: print(e)

# 使用 a 模式將自動建立不存在的檔案 no.md
open('no.md', 'a')

# 使用 x 模式開啟已經存在的檔案 no.md
try: open('no.md', 'x')
except FileExistsError as e: print(e)