def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("在调用bar之前: ", x)
    print("立即调用bar")
    bar()
    print("在调用bar之后: ", x)

foo()
print("x在主体内: ", x)