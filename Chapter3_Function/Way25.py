""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# * 기호 인자 : 위치 인자의 마지막과 키워드만 사용하는 인자의 시작을 구분해준다.
def fn_1():
    def safe_division_c(number, divisor, *,
                        ignore_overflow=False,
                        ignore_zero_division=False):
        try:
            return number / divisor
        except OverflowError:
            if ignore_overflow:
                return 0
            else:
                raise
        except ZeroDivisionError:
            if ignore_zero_division:
                return float('inf')
            else:
                raise

    # * 기호 인자를 사용해 위치 인자로 호출하게 될 경우 에러가 발생한다.
    # safe_division_c(1.0, 10**500, True, False)

    result = safe_division_c(1.0, 0, ignore_zero_division=True)
    assert result == float('inf')
    print(result)

    try:
        result = safe_division_c(1.0, 0)
    except ZeroDivisionError as e:
        print(e)
    pass


# / 기호 인자 : 위치로만 지정하는 인자의 끝을 표시한다.
def fn_2():
    def safe_division_d(numerator, denominator, /, *,
                        ignore_overflow=False,
                        ignore_zero_division=False):
        try:
            return numerator / denominator
        except OverflowError:
            if ignore_overflow:
                return 0
            else:
                raise
        except ZeroDivisionError:
            if ignore_zero_division:
                return float('inf')
            else:
                raise

    # / 기호 인자를 사용한 함수에 키워드 인자로 호출할 경우 에러가 발생한다.
    # safe_division_d(numerator=2, denominator=5)

    assert safe_division_d(2, 5) == 0.4
    pass


# / 와 * 기호사이에 있는 모든 파라미터는 위치를 사용하거나 키워드를 사용해 전달할 수 있다. ☆
def fn_3():
    def safe_division_e(numerator, denominator, /,
                        ndigits=10, *,
                        ignore_overflow=False,
                        ignore_zero_division=False):
        try:
            fraction = numerator / denominator
            return round(fraction, ndigits)
        except OverflowError:
            if ignore_overflow:
                return 0
            else:
                raise
        except ZeroDivisionError:
            if ignore_zero_division:
                return float('inf')
            else:
                raise

    result = safe_division_e(22, 7)
    print(result)

    result = safe_division_e(22, 7, 5)  # ndigits를 위치 인자로 호출한다.
    print(result)

    result = safe_division_e(22, 7, ndigits=2)  # ndigits를 키워드 인자로 호출한다.
    print(result)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    pass
