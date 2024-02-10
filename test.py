b = 1

def a(a1: str|int, **aaa) -> int:
    '''nihao
    nihao
        sdfd'''
    
    print(aaa)

a(111,abc=123)

dd= lambda x=1,*a,**y: return x
print(dd())
