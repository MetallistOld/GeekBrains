def type_logger(func):
    def wrapper(*args, **kwargs):
        print(f'{args[0]}: {type(args[0])}')
        result = func(*args, **kwargs)
        return result

    return wrapper


@type_logger
def calc_cube(a: int) -> int:
    return a ** 3


a = calc_cube(5)
