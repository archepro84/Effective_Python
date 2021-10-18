""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 스타 인자를 지정하지 않아 값이 없을 때도 빈 리스트를 넣어야한다.
def fn_1():
    def log(message, values):
        if not values:
            print(message)
        else:
            values_str = ', '.join(str(x) for x in values)
            print(f'{message}: {values_str}')

    log('내 숫자는 ', [1, 2])
    log('안녕 ', [])

    pass


# 위치 인자를 가변적으로 받을 수 있으면 함수 호출이 더 깔끔해지고 시각적 잡음도 줄어든다.
def fn_2():
    def log(message, *values):  # values 변수를 스타 인자로 지정했다.
        if not values:
            print(message)
        else:
            values_str = ', '.join(str(x) for x in values)
            print(f'{message}: {values_str}')

    log('내 숫자는 ', [1, 2])
    log('안녕 빈리스트! ', [])
    log('안녕 Null! ')
    pass


# 위치 인자가 함수에 전달되기 전에 항상 튜플로 변환된다. ☆
def fn_3():
    def my_generator():
        for i in range(10):
            yield i

    def my_func(*args):
        print(type(args))
        print(args)

    it = my_generator()
    my_func(*it)
    pass


# 이미 위치인자가 존재하는 함수에 인자 목록 앞부분에 추가하려고 시도하면, 코드가 미묘하게 깨질 수 있다.
def fn_4():
    def log(sequence, message, *values):
        if not values:
            print(f'{sequence} - {message}')
        else:
            values_str = ', '.join(str(x) for x in values)
            print(f'{sequence} - {message}: {values_str}')

    log(1, '좋아하는 숫자는', 7, 33)  # 새 코드에서 가변 인자를 사용. 문제 없음
    log(1, '안녕')  # 새 코드에서 가변 인자 없이 메시지만 사용. 문제 없음
    log('좋아하는 숫자는', 7, 33)  # 예전 방식 코드는 깨짐
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    pass
