
def decorate_with_args(arg):
    def decorate_it(function):
        def wrapper(*args, **kwargs):
            print('inside decorator: ', args, kwargs)
            print('Decorator arg', arg)
            res = function(*args, **kwargs)
            return res
        return wrapper
    return decorate_it


@decorate_with_args(1)
def function(variable):
    print(f'inside main function. Called with {variable}')
    return 'done'

print(function(1))



def decorator(func):
    def wrapper(*args, **kwargs):
        return func(args, kwargs)
    return wrapper



