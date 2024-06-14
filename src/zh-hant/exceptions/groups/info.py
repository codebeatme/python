try:
    # 由於所包含的例外狀況均繼承自 Exception，因此會得到一個 ExceptionGroup 物件
    raise BaseExceptionGroup(
        '這僅僅是一個測試！',
        [NameError(), ValueError()]
    )
except ExceptionGroup as err:
    # 顯示例外狀況群組的相關內容
    print(f'來自例外狀況群組的資訊：{err.message}')
    print(f'例外狀況群組中的例外狀況：{err.exceptions}')
