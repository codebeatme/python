import warnings
import os

def warn():
    # 取得 student 模組所在的目錄
    filepath = os.path.dirname(__file__)
    warnings.warn(
        f'警告不會指向符合 {filepath} 的檔案',
        skip_file_prefixes=(filepath,)
    )
