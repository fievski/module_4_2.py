def test_function(x):
    a = x ** 2
    def inner_function(x):
        a = x * 2
        if a % 2 == 0:
            print('Я в области видимости функции test_function')

    inner_function(x)
    return a

b = test_function(2)
print(b)


