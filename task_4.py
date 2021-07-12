def val_checker(callback):
    def _logger(func):
        def wrapper(*args, **kwargs):

            if args[0] > 0:
                result = func(*args, **kwargs)
                print(result)
                return result
            else:
                msg = f'ValueError: wrong val {args[0]}'
                raise ValueError(msg)
            return result

        return wrapper

    return _logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
a = calc_cube(-5)
