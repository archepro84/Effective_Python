""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 동일한 print를 사용하는 방법
def fn_1():
    my_value = 'foo 푸푸'
    print(my_value)
    print(str(my_value))
    print('%s' % my_value)
    print(f'{my_value}')
    print(format(my_value))
    print(my_value.__format__('s'))
    print(my_value.__str__())
    pass


# repr 내장 함수의 활용방법
def fn_2():
    a = '\x07'
    print(repr(a))

    # repr이 반환한 값을 eval 내장 함수에 넘기면 repr에 넘겼던 객체와 같은 객체가 생겨야 한다.
    b = eval(repr(a))
    print(a == b)

    # print를 사용해 디버깅할 때는 값을 출력하기 전에 repr을 호출해서 타입이 다른 경우에도 명확히 차이를 볼 수 있게 만들어야 한다.
    print(repr(5))
    print(repr('5'))

    # repr을 호출하는 것은 % 연산자에 %r 형식화 문자열을 사용하는 것이나 f-String에 !r 타입 변환을 사용하는 것과 같다.
    print('%r' % 5)
    print('%r' % '5')

    int_value = 5
    str_value = '5'
    print(f'{int_value!r} != {str_value!r}')
    pass


# Class의 특별 메서드
def fn_3():
    # Class의 __repr__을 호출하였을 때 알 수 없는 정보가 출력된다.
    class OpaqueClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    obj = OpaqueClass(1, 'foo')
    print(obj)

    # __dict__ Attribute를 통해 객체의 인스턴스 딕셔너리에 접근할 수 있다.
    obj = OpaqueClass(4, 'baz')
    print(obj.__dict__)

    # Class의 __repr__을 설정했을 때 출력값을 설정할 수 있다.
    class BetterClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f'BetterClass({self.x!r}, {self.y!r})'

    obj = BetterClass(2, '뭐시기')
    print(obj)
    pass



if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    pass
