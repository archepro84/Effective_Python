""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 반환 값을 2-튜플로 분리해 첫 번째 부분은 연산의 성공여부, 두 번째 부분은 실제 결괏값을 저장한다.
def fn_1():
    def careful_divide(a, b):
        try:
            return True, a / b
        except ZeroDivisionError:
            return False, None

    x, y = 1, 0
    success, result = careful_divide(x, y)
    if success is None:
        print('잘못된 입력')

    x, y = 0, 5
    success, result = careful_divide(x, y)
    if not success:
        print('잘못된 입력')
    pass


# 결코 None을 반환하지 않고, Exception을 발생시켜 호출자가 처리하게 한다.
def fn_2():
    def careful_divide(a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            raise ValueError('잘못된 입력')

    x, y = 5, 2
    try:
        result = careful_divide(x, y)
    except ValueError:
        print('잘못된 입력')
    else:
        print('결과는 %.1f 입니다' % result)
    pass


# 타입 애너테이션을 사용해 함수의 반환 타입을 지정해 None이 반환되지 않음을 알리는 것이 좋다.
def fn_3():
    # Docstring과 타입 애너테이션을 포함해 가독성이 좋아졌다.
    def careful_divide(a: float, b: float) -> float:
        """a를 b로 나눈다.

        Raises:
            ValueError: b가 0이어서 나눗셈을 할 수 없을 때
        """
        try:
            return a / b
        except ZeroDivisionError as e:
            raise ValueError('잘못된 입력')

    x, y = 5, 2
    try:
        result = careful_divide(x, y)
    except ValueError:
        print('잘못된 입력')
    else:
        print('결과는 %.1f 입니다' % result)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    pass
