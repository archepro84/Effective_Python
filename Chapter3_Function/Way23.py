""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 위치 기반 인자를 지정하려면 키워드 인자보다 앞에 지정해야 한다.
def fn_1():
    def remainder(number, divisor):
        return number % divisor

    # remainder(number=20, 7)
    pass


# 각 인자는 단 한번만 지정해야 한다.
def fn_2():
    def remainder(number, divisor):
        return number % divisor

    # remainder(20, number=7)
    pass


# 파이썬이 딕셔너리에 들어 있는 값을 함수에 전달하되 각 값에 대응하는 Key를 키워드로 사용하도록 명령한다.
def fn_3():
    def remainder(number, divisor):
        return number % divisor

    my_kwargs = {
        'number': 20,
        'divisor': 7,
    }

    assert remainder(**my_kwargs) == 6
    print(remainder(**my_kwargs))
    pass


# ** 연산자를 위치 인자나 키워드 인자와 섞어서 함수를 호출할 수 있다. / 중복되는 인자가 없어야한다.
def fn_4():
    def remainder(number, divisor):
        return number % divisor

    my_kwargs = {
        'divisor': 7,
    }

    assert remainder(number=20, **my_kwargs) == 6
    print(remainder(number=20, **my_kwargs))
    pass


# ** 연산자를 여러 번 사용할 수도 있다. 다만 여러 딕셔너리에 겹치는 키가 없어야 한다.
def fn_5():
    def remainder(number, divisor):
        return number % divisor

    my_kwargs = {
        'number': 20,
    }

    other_kwargs = {
        'divisor': 7,
    }

    assert remainder(**my_kwargs, **other_kwargs) == 6
    print(remainder(**my_kwargs, **other_kwargs))
    pass


# **kwargs 파라미터를 이용해 아무 키워드 인자를 받는 함수를 구현
def fn_6():
    def print_parameters(**kwargs):
        for key, value in kwargs.items():
            print(f'{key} = {value}')

    print_parameters(alpha=1.5, beta=9, 감마=4)
    pass


# 키워드 인자의 경우 함수 정의에서 Default 값을 지정할 수 있다.
def fn_7():
    def flow_rate(weight_diff, time_diff, period=1):
        return (weight_diff / time_diff) * period

    weight_diff = 0.5
    time_diff = 3

    flow_per_second = flow_rate(weight_diff, time_diff)
    flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)

    print(flow_per_second)
    print(flow_per_hour)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    # fn_6()
    # fn_7()
    pass
