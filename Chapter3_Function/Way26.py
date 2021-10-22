""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 데코레이터를 호출한 후 반환값을 fibonacci에 등록한다.
def fn_1():
    def trace(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'{func.__name__}({args!r}, {kwargs!r}) '
                  f'-> {result!r}')
            return result

        return wrapper

    @trace
    def fibonacci(n):
        """Return n 번째 피보나치 수"""
        if n in (0, 1):
            return n
        return (fibonacci(n - 2) + fibonacci(n - 1))

    # wrapper의 코드를 원래의 fibonacci 함수가 실행되기 전과 후에 실행한다.
    fibonacci = trace(fibonacci)
    fibonacci(4)

    # print(fibonacci)
    help(fibonacci)
    pass


# wraps를 wrapper 함수에 적용하면 데코레이터 내부에 들어가는 함수에서 중요한 메타데이터를 복사해 wrapper 함수에 적용한다.
def fn_2():
    from functools import wraps

    def trace(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'{func.__name__}({args!r}, {kwargs!r}) '
                  f'-> {result!r}')
            return result

        return wrapper

    @trace
    def fibonacci(n):
        """n번째 피보나치 수를 반환한다."""
        if n in (0, 1):
            return n
        return (fibonacci(n - 2) + fibonacci(n - 1))

    # functools.wraps를 이용해 데코레이터가 적용되기 전 원본 함수의 정보가 반환된다,
    help(fibonacci)
    pass


def fn_3():
    import pickle
    # 메서드 안에 정의된함수를 pickle 할 수 없기 때문에 외부에 정의 한다.
    print(pickle.dumps(fibonacci))
    pass


"""메서드 안에 정의된함수를 pickle 할 수 없기 때문에 외부에 정의 한다. """
from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result

    return wrapper


@trace
def fibonacci(n):
    """n번째 피보나치 수를 반환한다."""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


"""메서드 안에 정의된함수를 pickle 할 수 없기 때문에 외부에 정의 한다. """

if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    pass
