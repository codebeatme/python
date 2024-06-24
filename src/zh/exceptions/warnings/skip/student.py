import warnings
import os

def warn():
    # 获取 student 模块所在的目录
    filepath = os.path.dirname(__file__)
    warnings.warn(
        f'警告不会指向符合 {filepath} 的文件',
        skip_file_prefixes=(filepath,)
    )
