""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# list.sort를 이용해 정렬
def fn_1():
    numbers = [93, 86, 11, 68, 70]
    numbers.sort()  # 오름차순 정렬
    print(numbers)

    numbers.sort(reverse=True)  # 내림차순 정렬
    print(numbers)
    pass


# Class의 내부 인자로 list를 정렬
def fn_2():
    class Tool:
        def __init__(self, name, weight):
            self.name = name
            self.weight = weight

        def __repr__(self):
            return f'Tool({self.name!r}, {self.weight})'

    tools = [
        Tool('수준계', 3.5),
        Tool('해머', 1.25),
        Tool('스크류드라이버', 0.5),
        Tool('끌', 0.25),
    ]

    print('미정렬:', repr(tools))
    tools.sort(key=lambda x: x.name)  # 각 행의 .name을 알파벳순으로 정렬
    print('tools정렬: ', tools)

    tools.sort(key=lambda x: x.weight)  # 각 행의 .weight을 알파벳순으로 정렬
    print('weight 정렬: ', tools)
    pass


# 대 소문자 구분 없이 정렬
def fn_3():
    places = ['home', 'work', 'New York', 'Paris']
    places.sort()  # ASCII : 'A' = 65, 'a' = 97 대문자가 더 작으므로 우선정렬된다. ☆
    print('대소문자 구분:', places)

    places.sort(key=lambda x: x.lower())  # ASCII값을 소문자로 변경하여 정렬한다.
    print('대소문자 무시:', places)
    pass


# 튜플을 이용해 2가지 인자를 순서대로 정렬한다.
def fn_4():
    class Tool:
        def __init__(self, name, weight):
            self.name = name
            self.weight = weight

        def __repr__(self):
            return f'Tool({self.name!r}, {self.weight})'

    power_tools = [
        Tool('드릴', 4),
        Tool('원형 톱', 5),
        Tool('착암기', 40),
        Tool('연마기', 4),
    ]

    # weight를 우선 오름차순 정렬 후 name을 오름차순 정렬 ☆
    power_tools.sort(key=lambda x: (x.weight, x.name))
    print(power_tools)

    # name을 우선 내림차순 정렬 후 weight를 내림차순 정렬 ☆
    power_tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
    print(power_tools)

    # weight를 우선 오름차순 정렬 후 name을 내림차순 정렬 ☆
    power_tools.sort(key=lambda x: (-x.weight, x.name))
    print(power_tools)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    pass
