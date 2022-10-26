from datetime import datetime as dt


def path (path):
    def logger_decorator_path(func):

        def decorator(*args, **kwargs):
            result = func(*args, **kwargs)
            date = dt.now()
            with open(path, "a", encoding='utf-8') as f:
                f.write(f'\nДата / время вызова функции: {date.strftime("%d/%m/%Y %H:%M")}\n'
                        f'Имя вызываемой функции: {func.__name__}\n'
                        f'Аргументы при вызове функции: {args} {kwargs}\n'
                        f'Результат вызова функции: {result}\n')
                # записываем дату, время, имя функции и аргументы, записываем результат функции

            return result
        return decorator
    return logger_decorator_path


def logger_decorator(func):

    def decorator(*args, **kwargs):

        result = func(*args, **kwargs)
        date = dt.now()
        with open("logs.txt", "a", encoding='utf-8') as f:
            f.write(f'\nДата / время вызова функции: {date.strftime("%d/%m/%Y %H:%M")}\n'
                    f'Имя вызываемой функции: {func.__name__}\n'
                    f'Аргументы при вызове функции: {args} {kwargs}\n'
                    f'Результат вызова функции: {result}\n')
            # записываем дату, время, имя функции и аргументы, записываем результат функции

        return result
    return decorator
