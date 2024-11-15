# 請將命令列跳躍至腳本檔案 writelines.py 所在的目錄，然後執行他
# 將多個行寫入檔案
with open('writelines.txt', 'w', encoding='utf8') as file:
    file.writelines(('第一行\n', '第二行'))

# 將多個行寫入檔案
with open('writelinesb.txt', 'wb') as file:
    file.writelines(('第一行\n'.encode(), '第二行'.encode()))
