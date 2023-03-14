# 视频内容：「Python」高级教程 什么是内置变量？__name__的作用，如何运用__name__变量
# 视频地址：https://www.bilibili.com/video/BV1FY4y1R7hG/

print(f'name_datetime模块的__name__变量为{__name__}')

if __name__ == '__main__':
    import datetime
    print(datetime.datetime.now())