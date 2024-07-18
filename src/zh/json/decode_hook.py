import json

# 函数 hook，检查分数是否小于 0，如果是，则将其转换为正数
def hook(result):
    # 当字典包含 id 时，说明这是分数信息
    if 'id' in result and result['value'] < 0:
        result['value'] = -result['value']

    # 这里一定要返回一个对象，否则最终的解析结果将出现 None
    return result


# 使用函数 hook 来处理转换的 Python 对象
o = json.loads(
    '{"name": "Jack", "scores": [{"id": "A", "value": -100}, {"id": "B", "value": 200}]}',
    object_hook=hook
)
print(f'object_hook {o}')


# 函数 pairs_hook，计算所有分数之和
sum = 0
def pairs_hook(pairs):
    global sum

    # 检查所有键值对，计算所有的分数
    for i, pair in enumerate(pairs):
        key, value = pair

        # 键为 value，则累计分数，键为 scores 则写入分数
        if key == 'value':
            sum += value
        elif key == 'scores':
            pair = ('scores', sum)
        
        pairs[i] = pair
    
    # 这里使用键值对生成新的字典对象
    return dict(pairs)

# 使用函数 pairs_hook 来处理转换的键值对
o = json.loads(
    '{"name": "Jack", "scores": [{"id": "A", "value": 100}, {"id": "B", "value": 200}]}',
    object_pairs_hook=pairs_hook
)
print(f'object_pairs_hook {o}')
