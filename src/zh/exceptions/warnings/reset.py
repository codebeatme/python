import warnings

# 为警告过滤器添加匹配规则
# 忽略 message 参数开头符合正则表达式 Err_.+ 的警告
warnings.filterwarnings('ignore', 'Err_.+')

# 下面的警告不会显示，因为 message 的开头符合 Err_.+（不区分大小写）
warnings.warn('eRR_A 糟糕！我又吃瘪了？')
# 下面的警告会显示，因为 message 的开头含有一个空格，与 Err_.+ 不匹配
warnings.warn(' Err_A 拒绝吃瘪')

# 清空 Python 警告过滤器的规则
warnings.resetwarnings()
print(warnings.filters)

# 下面的警告会显示，因为清空了所有规则
warnings.warn('Err_A 糟糕！我又吃瘪了？')
