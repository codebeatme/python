'''
本节视频
https://www.bilibili.com/video/BV1FY4y1R7hG/ 「Python」高级教程 什么是内置变量？__name__的作用，如何运用__name__变量
内置变量是由Python自身定义的变量，每一个模块都有自己的__name__变量
* 如果模块是程序的入口，则__name__变量为'__main__'
* 如果模块被其他模块导入，则__name__变量为模块名

版本
Python 3.11.2
VSCode 1.76.1

相关视频
https://www.bilibili.com/video/BV1iY4y1U7FY/ 什么是模块？如何创建导入和使用模块

关于本系列教程的使用说明和相关问题解答，请参考文章 https://www.bilibili.com/read/cv23030766
'''

print(f'name_datetime模块的__name__变量为{__name__}')

if __name__ == '__main__':
    import datetime
    print(datetime.datetime.now())