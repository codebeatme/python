import json

# 函式 hook，檢查分數是否小於 0，如果是，則將其轉換為正數
def hook(result):
    # 當字典包含 id 時，說明這是分數資訊
    if 'id' in result and result['value'] < 0:
        result['value'] = -result['value']

    # 這裏一定要傳回一個物件，否則最終的解析結果將出現 None
    return result


# 使用函式 hook 來處理轉換的 Python 物件
o = json.loads(
    '{"name": "Jack", "scores": [{"id": "A", "value": -100}, {"id": "B", "value": 200}]}',
    object_hook=hook
)
print(f'object_hook {o}')


# 函式 pairs_hook，計算所有分數之和
sum = 0
def pairs_hook(pairs):
    global sum

    # 檢查所有鍵值組，計算所有的分數
    for i, pair in enumerate(pairs):
        key, value = pair

        # 鍵為 value，則累計分數，鍵為 scores 則寫入分數
        if key == 'value':
            sum += value
        elif key == 'scores':
            pair = ('scores', sum)
        
        pairs[i] = pair
    
    # 這裏使用鍵值組建置新的字典物件
    return dict(pairs)

# 使用函式 pairs_hook 來處理轉換的鍵值組
o = json.loads(
    '{"name": "Jack", "scores": [{"id": "A", "value": 100}, {"id": "B", "value": 200}]}',
    object_pairs_hook=pairs_hook
)
print(f'object_pairs_hook {o}')
