# 檔案物件的 __enter__ 方法傳回自身
with open('with.txt', 'w', encoding='utf8') as file:
    file.write('with 陳述式')

# ERROR 檔案物件已經被關閉
file.write('又一條 with 陳述式')
file.__exit__