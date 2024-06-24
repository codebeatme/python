import warnings

# 為警告過濾器新增比對規則
# 忽略 message 參數開頭符合規則運算式 Err_.+ 的警告
warnings.filterwarnings('ignore', 'Err_.+')

# 下面的警告不會顯示，因為 message 的開頭符合 Err_.+（不區分大小寫）
warnings.warn('eRR_A 糟糕！我又吃癟了？')
# 下面的警告會顯示，因為 message 的開頭含有一個空格，與 Err_.+ 不相符
warnings.warn(' Err_A 拒絕吃癟')

# 清空 Python 警告過濾器的規則
warnings.resetwarnings()
print(warnings.filters)

# 下面的警告會顯示，因為清空了所有規則
warnings.warn('Err_A 糟糕！我又吃癟了？')
